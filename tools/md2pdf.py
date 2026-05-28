#!/usr/bin/env python3
"""Minimal Markdown -> PDF converter (reportlab). Handles headings, bold,
bullet lists, pipe tables, blockquotes. Built for career-ops evaluation reports.
Usage: python3 tools/md2pdf.py input.md output.pdf
"""
import sys, re, html
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, ListFlowable, ListItem)

BLUE = colors.HexColor("#0b5394")
AMBER = colors.HexColor("#856404")

def inline(text):
    text = html.escape(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'`(.+?)`', r'<font face="Courier">\1</font>', text)
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<link href="\2" color="blue">\1</link>', text)
    return text

def color_note(cell):
    m = re.match(r'\s*(\d)\s*/\s*5', cell)
    if not m:
        return inline(cell)
    n = int(m.group(1))
    c = "#c0392b" if n <= 2 else ("#d68910" if n == 3 else "#1e8449")
    return f'<b><font color="{c}">{html.escape(cell)}</font></b>'

def build(md, out):
    styles = getSampleStyleSheet()
    body = ParagraphStyle('body', parent=styles['Normal'], fontSize=10, leading=14)
    h1 = ParagraphStyle('h1', parent=styles['Heading1'], fontSize=16, textColor=BLUE, spaceAfter=4)
    h2 = ParagraphStyle('h2', parent=styles['Heading2'], fontSize=12.5, textColor=BLUE, spaceBefore=12, spaceAfter=4)
    h3 = ParagraphStyle('h3', parent=styles['Heading3'], fontSize=10.5, spaceBefore=8, spaceAfter=2)
    quote = ParagraphStyle('quote', parent=body, leftIndent=10, backColor=colors.HexColor("#fff3cd"),
                           borderColor=AMBER, borderWidth=0, spaceBefore=6, spaceAfter=6)
    cell = ParagraphStyle('cell', parent=body, fontSize=8.5, leading=11)
    cellh = ParagraphStyle('cellh', parent=cell, textColor=colors.white)

    doc = SimpleDocTemplate(out, pagesize=A4, topMargin=1.6*cm, bottomMargin=1.6*cm,
                            leftMargin=1.8*cm, rightMargin=1.8*cm,
                            author="Arthur Pawlowski", creator="Arthur Pawlowski")
    flow = []
    lines = md.split('\n')
    i = 0
    bullets = []

    def flush_bullets():
        nonlocal bullets
        if bullets:
            items = [ListItem(Paragraph(inline(b), body), leftIndent=12) for b in bullets]
            flow.append(ListFlowable(items, bulletType='bullet', start='•', leftIndent=14))
            flow.append(Spacer(1, 4))
            bullets = []

    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            flush_bullets(); i += 1; continue
        if line.startswith('# '):
            flush_bullets(); flow.append(Paragraph(inline(line[2:]), h1))
        elif line.startswith('## '):
            flush_bullets(); flow.append(Paragraph(inline(line[3:]), h2))
        elif line.startswith('### '):
            flush_bullets(); flow.append(Paragraph(inline(line[4:]), h3))
        elif line.startswith('> '):
            flush_bullets(); flow.append(Paragraph(inline(line[2:]), quote))
        elif line.lstrip().startswith('- '):
            bullets.append(line.lstrip()[2:])
        elif line.startswith('|'):
            flush_bullets()
            tbl = []
            while i < len(lines) and lines[i].startswith('|'):
                row = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                tbl.append(row); i += 1
            tbl = [r for r in tbl if not all(set(c) <= set('-: ') for c in r)]
            if tbl:
                ncol = len(tbl[0])
                data = []
                for ri, row in enumerate(tbl):
                    cells = []
                    for ci, c in enumerate(row):
                        if ri == 0:
                            cells.append(Paragraph(f'<b>{inline(c)}</b>', cellh))
                        elif ci == 1:
                            cells.append(Paragraph(color_note(c), cell))
                        else:
                            cells.append(Paragraph(inline(c), cell))
                    data.append(cells)
                widths = None
                if ncol == 4:
                    widths = [3.0*cm, 1.4*cm, 1.2*cm, 11.0*cm-1.0*cm]
                t = Table(data, colWidths=widths, repeatRows=1)
                t.setStyle(TableStyle([
                    ('BACKGROUND',(0,0),(-1,0),BLUE),
                    ('GRID',(0,0),(-1,-1),0.5,colors.HexColor("#cccccc")),
                    ('VALIGN',(0,0),(-1,-1),'TOP'),
                    ('TOPPADDING',(0,0),(-1,-1),3),
                    ('BOTTOMPADDING',(0,0),(-1,-1),3),
                ]))
                flow.append(t); flow.append(Spacer(1,6))
            continue
        elif set(line) <= set('-') and len(line) >= 3:
            pass  # hr
        else:
            flush_bullets(); flow.append(Paragraph(inline(line), body))
        i += 1
    flush_bullets()
    doc.build(flow)

if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding='utf-8') as f:
        build(f.read(), dst)
    print("wrote", dst)
