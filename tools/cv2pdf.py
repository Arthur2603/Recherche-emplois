#!/usr/bin/env python3
"""CV markdown -> PDF, reproducing Arthur's preferred one-column design
(navy section headers, centered header block, right-aligned dates, bullets).

Markdown convention:
  # NAME                       -> centered navy 20pt bold
  (lines until first '## ')     -> centered gray (1st = subtitle 11pt, rest = contact 9pt)
  ## SECTION                    -> navy uppercase section header + rule
  ### Job Title @@ Date         -> bold navy title (left) + gray date (right)
  _Company line_                -> gray company/context line (wrap in _underscores_)
  - bullet                      -> bullet item
  **Label** — text              -> skill line (bold label + normal)
  plain paragraph               -> justified body

Usage: python3 tools/cv2pdf.py input.md output.pdf
"""
import sys, re, html
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable, ListFlowable, ListItem)

NAVY = colors.HexColor("#1F2A44")
GRAY = colors.HexColor("#555555")

def inline(t):
    t = html.escape(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'__(.+?)__', r'<b>\1</b>', t)
    return t

def build(md, out):
    name = ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=20,
                          textColor=NAVY, alignment=TA_CENTER, spaceAfter=2, leading=23)
    subtitle = ParagraphStyle('sub', fontName='Helvetica', fontSize=11,
                              textColor=GRAY, alignment=TA_CENTER, spaceAfter=1, leading=14)
    contact = ParagraphStyle('contact', fontName='Helvetica', fontSize=9,
                             textColor=GRAY, alignment=TA_CENTER, spaceAfter=2, leading=12)
    section = ParagraphStyle('section', fontName='Helvetica-Bold', fontSize=11,
                             textColor=NAVY, spaceBefore=10, spaceAfter=2, leading=13)
    jobtitle = ParagraphStyle('job', fontName='Helvetica-Bold', fontSize=11,
                              textColor=NAVY, leading=13)
    jobdate = ParagraphStyle('jobdate', fontName='Helvetica', fontSize=10,
                             textColor=GRAY, alignment=2, leading=13)  # 2 = right
    company = ParagraphStyle('company', fontName='Helvetica', fontSize=10,
                            textColor=GRAY, spaceAfter=2, leading=12)
    body = ParagraphStyle('body', fontName='Helvetica', fontSize=10,
                          alignment=TA_JUSTIFY, leading=13, spaceAfter=2)
    bullet = ParagraphStyle('bullet', fontName='Helvetica', fontSize=10,
                            alignment=TA_JUSTIFY, leading=12.5)
    skill = ParagraphStyle('skill', fontName='Helvetica', fontSize=10,
                          leading=13, spaceAfter=1)

    doc = SimpleDocTemplate(out, pagesize=A4, topMargin=1.3*cm, bottomMargin=1.2*cm,
                            leftMargin=1.9*cm, rightMargin=1.9*cm,
                            title="CV Arthur Pawlowski", author="Arthur Pawlowski",
                            creator="Arthur Pawlowski", subject="Curriculum Vitae")
    flow = []
    lines = md.split('\n')
    i = 0
    n = len(lines)
    bullets = []

    def flush_bullets():
        nonlocal bullets
        if bullets:
            items = [ListItem(Paragraph(inline(b), bullet), leftIndent=10,
                              value='•') for b in bullets]
            flow.append(ListFlowable(items, bulletType='bullet', start='•',
                                     leftIndent=12, bulletFontSize=9,
                                     spaceBefore=0, spaceAfter=0))
            flow.append(Spacer(1, 3))
            bullets = []

    # Header block: name + centered lines until first '## '
    # find name
    while i < n and not lines[i].startswith('# '):
        i += 1
    if i < n:
        flow.append(Paragraph(inline(lines[i][2:].strip()), name))
        i += 1
    header_lines = []
    while i < n and not lines[i].startswith('## ') and not lines[i].startswith('# '):
        if lines[i].strip():
            header_lines.append(lines[i].strip())
        i += 1
    for idx, hl in enumerate(header_lines):
        flow.append(Paragraph(inline(hl), subtitle if idx == 0 else contact))
    flow.append(Spacer(1, 4))

    while i < n:
        line = lines[i].rstrip()
        s = line.strip()
        if not s:
            i += 1; continue
        if line.startswith('## '):
            flush_bullets()
            flow.append(Paragraph(inline(line[3:].strip().upper()), section))
            flow.append(HRFlowable(width='100%', thickness=0.6, color=NAVY,
                                   spaceBefore=1, spaceAfter=3))
        elif line.startswith('### '):
            flush_bullets()
            content = line[4:].strip()
            if '@@' in content:
                left, right = content.split('@@', 1)
                tbl = Table([[Paragraph(inline(left.strip()), jobtitle),
                              Paragraph(inline(right.strip()), jobdate)]],
                            colWidths=[11.6*cm, 5.6*cm])
                tbl.setStyle(TableStyle([
                    ('VALIGN',(0,0),(-1,-1),'BOTTOM'),
                    ('LEFTPADDING',(0,0),(-1,-1),0),
                    ('RIGHTPADDING',(0,0),(-1,-1),0),
                    ('TOPPADDING',(0,0),(-1,-1),0),
                    ('BOTTOMPADDING',(0,0),(-1,-1),0),
                ]))
                flow.append(tbl)
            else:
                flow.append(Paragraph(inline(content), jobtitle))
        elif s.startswith('_') and s.endswith('_'):
            flush_bullets()
            flow.append(Paragraph(inline(s[1:-1]), company))
        elif line.lstrip().startswith('- '):
            bullets.append(line.lstrip()[2:])
        elif s.startswith('**') and ('—' in s or ':' in s):
            flush_bullets()
            flow.append(Paragraph(inline(s), skill))
        else:
            flush_bullets()
            flow.append(Paragraph(inline(s), body))
        i += 1
    flush_bullets()
    doc.build(flow)

if __name__ == '__main__':
    with open(sys.argv[1], encoding='utf-8') as f:
        build(f.read(), sys.argv[2])
    print("wrote", sys.argv[2])
