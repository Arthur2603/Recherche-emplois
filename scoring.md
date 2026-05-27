# Grille de scoring des annonces

Document utilisé pour évaluer toute annonce d'emploi par rapport à mon profil (`profil.md`) et mon CV (`cv.md`).

## Principe

Chaque annonce est notée sur **10 dimensions pondérées**. Le score final est une **note A à F** qui détermine si je candidate ou pas.

Le scoring doit être **brutalement honnête**. Une annonce notée C ou en dessous ne mérite probablement pas une candidature personnalisée. Mieux vaut 5 candidatures A bien préparées que 50 candidatures D envoyées en masse.

---

## Les 10 dimensions

### 1. Match technique cœur de métier (poids : 25%)

À quel point les compétences techniques demandées recoupent mon expertise centrale ?

- **5/5** — Tracking, GTM, CAPI, server-side, Consent Mode explicitement mentionnés et centraux
- **4/5** — Paid Media Meta + analytics/data, sans le tracking pur mais très proche
- **3/5** — Marketing digital large avec une composante data significative
- **2/5** — Marketing digital généraliste, data secondaire
- **1/5** — Pas de lien clair avec mon expertise
- **0/5** — Hors-sujet total

### 2. Niveau d'expérience demandé (poids : 10%)

Le poste correspond-il à mes 3,5 ans d'expérience ?

- **5/5** — 3 à 5 ans demandés, "Expert" ou "Senior" sans exiger >5 ans
- **4/5** — 2 à 4 ans, ou junior à confirmé avec montée en compétences possible
- **3/5** — 4 à 7 ans (un peu au-dessus, mais accessible avec mon profil pointu)
- **2/5** — Lead/Manager exigeant 5+ ans avec management formel
- **1/5** — Directeur, 8+ ans, management d'équipe formel exigé
- **0/5** — Junior pur ou stage

### 3. Salaire (poids : 15%)

Le salaire affiché ou estimé est-il compatible avec mon minimum (40k€) et ma cible (50-55k€) ?

- **5/5** — 50k€+ explicitement mentionné, ou fourchette qui inclut 50k€+
- **4/5** — 45-50k€ explicite, ou contexte d'entreprise qui suggère ce niveau
- **3/5** — 40-45k€, ou pas mentionné mais le poste/entreprise suggère ≥40k€
- **2/5** — Pas mentionné et le contexte rend incertain (PME, secteur peu rémunérateur)
- **1/5** — 35-40k€ probable
- **0/5** — <40k€ mentionné ou très probable

### 4. Localisation (poids : 10%)

- **5/5** — Paris intra-muros, accessible en métro
- **4/5** — Petite couronne (92, 93, 94) bien desservie
- **3/5** — Grande couronne accessible en transport (RER)
- **2/5** — IDF mais éloigné / mauvaise desserte
- **1/5** — Full remote depuis Paris autorisé
- **0/5** — Hors IDF, sauf si full remote France OK

### 5. Type de contrat (poids : 10%)

- **5/5** — CDI confirmé
- **3/5** — CDD long (12 mois+) avec perspective CDI
- **1/5** — CDD court / mission freelance
- **0/5** — Alternance, stage, intérim

### 6. Télétravail (poids : 5%)

- **5/5** — Hybride 2-3j de bureau / semaine explicite
- **4/5** — Hybride flexible
- **3/5** — 1 jour de télétravail / semaine
- **2/5** — Télétravail ponctuel uniquement
- **1/5** — 100% présentiel
- **0/5** — 100% remote (pas ce que je cherche)

### 7. Entreprise & secteur (poids : 5%)

- **5/5** — Scale-up tech, éditeur média digital, e-commerce premium, agence reconnue
- **4/5** — Grand groupe avec une vraie équipe data structurée
- **3/5** — PME en croissance avec ambitions digitales
- **2/5** — Entreprise traditionnelle peu mature digitalement
- **1/5** — Boîte avec mauvaise réputation employeur (Glassdoor <3/5)
- **0/5** — Red flags (procédures en cours, plans sociaux récents)

### 8. Évolution & apprentissage (poids : 5%)

Le poste m'apprend-il quelque chose de nouveau ou élargit-il mon scope ?

- **5/5** — Passage côté éditeur, structurer une stack data en interne, ou intégration IA appliquée
- **4/5** — Périmètre élargi par rapport à aujourd'hui (lead tracking, multi-canal, etc.)
- **3/5** — Périmètre équivalent mais nouveau secteur ou nouvelle techno
- **2/5** — Même périmètre dans un nouveau cadre
- **1/5** — Régression de périmètre
- **0/5** — Retour au support pur ou exécution répétitive

### 9. Posture conseil vs exécution (poids : 10%)

Le rôle est-il consultatif/expert ou purement exécutant ?

- **5/5** — "Expert", "Lead", autonomie complète sur la roadmap tracking/paid media
- **4/5** — Manager avec ownership d'un domaine
- **3/5** — Mix conseil/exécution équilibré
- **2/5** — Plutôt exécutant avec quelques recommandations
- **1/5** — Exécutant pur sous supervision
- **0/5** — Support / hotline / opérations répétitives

### 10. Feu de cœur (poids : 5%)

À l'instinct, est-ce que cette annonce me donne envie ?

- **5/5** — Je veux ce poste, je vois le pitch d'entretien dans ma tête
- **4/5** — Très intéressé, je verrais bien évoluer là
- **3/5** — Pourquoi pas, à creuser
- **2/5** — Mouais, ça dépanne
- **1/5** — Pas envie mais ça paie les factures
- **0/5** — Je ne candidaterais que par désespoir

---

## Calcul du score final

```
Score brut = somme des (note × poids)
Score sur 5 = score brut / 100 × 5
```

Le score sur 5 détermine la note finale.

## Échelle des notes

| Note | Score | Action |
|---|---|---|
| **A** | 4,5 à 5,0 | Top priorité. Candidature personnalisée approfondie. CV adapté + LM ciblée + recherche du recruteur sur LinkedIn. À envoyer dans les 24h. |
| **B** | 4,0 à 4,4 | Bonne cible. Candidature personnalisée. CV adapté + LM. À envoyer dans les 48h. |
| **C** | 3,0 à 3,9 | Mitigé. Candidature seulement si je n'ai pas d'autres priorités en cours, et avec CV peu adapté. |
| **D** | 2,0 à 2,9 | Faible. Ne pas candidater sauf circonstance exceptionnelle (réseau, recommandation). |
| **F** | <2,0 | Non. Ne pas perdre de temps. |

## Red flags qui font tomber à F automatiquement

Indépendamment du score :

- Alternance, stage, ou intérim
- Salaire <40k€ mentionné ou évident
- Hors IDF sans full remote France
- Annonce qui demande explicitement 7+ ans d'expérience avec management formel d'équipe
- Entreprise avec note Glassdoor < 2,5/5 sur 20+ avis
- Annonce qui sent le "stagiaire déguisé" (intitulé pompeux, missions juniors)

## Bonus qui font remonter d'une demi-note

- Annonce qui mentionne **explicitement** la CAPI ou le server-side tagging
- Annonce qui mentionne un transfert annonceur → éditeur (mon angle storytelling fort)
- Entreprise dont j'ai déjà eu un compte annonceur chez Concentrix
- Recommandation interne possible (à creuser sur LinkedIn)

---

## Format de sortie attendu

Pour chaque annonce évaluée, retourne un bloc structuré comme ceci :

```
## [Nom du poste] — [Entreprise]
**URL** : [lien]
**Date d'annonce** : [date]

### Scoring détaillé
| Dimension | Note | Poids | Commentaire |
|---|---|---|---|
| Match technique | x/5 | 25% | ... |
| Expérience | x/5 | 10% | ... |
| Salaire | x/5 | 15% | ... |
| Localisation | x/5 | 10% | ... |
| Contrat | x/5 | 10% | ... |
| Télétravail | x/5 | 5% | ... |
| Entreprise | x/5 | 5% | ... |
| Évolution | x/5 | 5% | ... |
| Posture | x/5 | 10% | ... |
| Feu de cœur | x/5 | 5% | ... |

**Score final** : x,x / 5 → **Note [A/B/C/D/F]**

### Synthèse
- ✅ Points forts du match : ...
- ⚠️ Points faibles / gaps à anticiper : ...
- 🎯 Recommandation : [candidate / passe ton chemin / à creuser]

### Mots-clés à injecter dans le CV
[liste des termes exacts de l'annonce à reprendre dans la version adaptée]

### Angle de la lettre de motivation
[en 2-3 lignes : quel angle privilégier pour cette annonce spécifiquement]
```
