# Grille de scoring des annonces

Document utilisé pour évaluer toute annonce d'emploi par rapport à mon profil (`profil.md`) et mon CV (`cv.md`).

## Principe — système à 2 axes

Chaque annonce est notée sur **deux axes indépendants** :

- **Axe 1 — Désirabilité** : est-ce que ce poste me convient ? (10 dimensions pondérées → note **A à F**)
- **Axe 2 — Probabilité d'embauche** : ai-je des chances réelles de l'obtenir ? (6 dimensions pondérées → tier **Élevée / Moyenne / Faible**)

Les deux axes se croisent dans une **matrice de priorisation** (voir plus bas) qui détermine où mettre mon énergie. Un poste parfait que je n'obtiendrai jamais ne vaut pas mieux qu'un bon poste accessible.

Le scoring doit être **brutalement honnête** sur les deux axes. Mieux vaut 5 candidatures bien ciblées (désirables ET atteignables) que 50 candidatures envoyées en masse.

---

# AXE 1 — DÉSIRABILITÉ (est-ce que ce poste me convient ?)

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

# AXE 2 — PROBABILITÉ D'EMBAUCHE (ai-je des chances de l'obtenir ?)

Cet axe note **mes chances réelles d'être recruté**, indépendamment de mon envie. Il répond à : "si je candidate, ai-je une vraie chance, ou est-ce que je perds mon temps ?"

Noté sur **6 dimensions pondérées**, score sur 5 → tier **Élevée / Moyenne / Faible**.

### P1. Couverture des compétences obligatoires (poids : 35%)

À quel point je coche les "must-have" explicites de l'annonce (pas les "nice-to-have") ?

- **5/5** — Je coche tous les must-have, certains au niveau expert
- **4/5** — Je coche tous les must-have de base, quelques-uns juste suffisants
- **3/5** — Je coche la majorité, un must-have me manque mais rattrapable
- **2/5** — Plusieurs must-have me manquent
- **1/5** — La compétence centrale du poste n'est pas la mienne
- **0/5** — Je ne coche presque rien

### P2. Adéquation séniorité / années exigées (poids : 20%)

Mon niveau d'expérience correspond-il à ce qui est demandé ?

- **5/5** — Pile dans la fourchette demandée
- **4/5** — Légèrement en-dessous/au-dessus mais crédible (ex : 3,5 ans pour "4 ans")
- **3/5** — Un cran en-dessous, à argumenter (ex : 3,5 ans pour "5 ans")
- **2/5** — Net décalage (junior pour un senior, ou l'inverse)
- **1/5** — Très loin du niveau attendu
- **0/5** — Hors-jeu (ex : 8+ ans + management formel exigé)

### P3. Formation vs filtre diplôme (poids : 10%)

L'annonce impose-t-elle un filtre diplôme que je ne coche pas ?

- **5/5** — Aucun filtre, ou je coche exactement (ex : "Master" → j'ai un Master)
- **4/5** — Filtre large que je coche (Bac+5 toutes filières)
- **3/5** — Filtre "grande école / ingé idéalement" mais ouvert (mon profil passe en compensant par l'expérience)
- **2/5** — Filtre "école d'ingénieur" strict que je ne coche pas (parcours Finance/Marketing)
- **1/5** — Double filtre fermé (ex : ingénieur + MBA top)
- **0/5** — Diplôme spécifique obligatoire que je n'ai pas (PhD, certif réglementée)

### P4. Différenciation / rareté de mon profil (poids : 15%)

Est-ce que j'apporte quelque chose de rare qui me fait sortir du lot ?

- **5/5** — Mon angle unique (consultant Meta officiel, CAPI early adopter 2022) est exactement ce qu'ils cherchent
- **4/5** — Forte différenciation utile au poste
- **3/5** — Profil correct mais interchangeable avec d'autres candidats
- **2/5** — Rien ne me distingue, marché de candidats fourni
- **1/5** — Je suis en bas de la pile des candidats crédibles
- **0/5** — Profil clairement hors-cible pour eux

### P5. Sélectivité de l'employeur (poids : 10%) — *inversé*

Plus l'employeur est sélectif et convoité, plus c'est dur. (Note haute = accessible.)

- **5/5** — PME/scale-up qui peine à recruter ce profil, peu de candidats
- **4/5** — Entreprise correcte, sélectivité normale
- **3/5** — Marque attractive, beaucoup de candidatures
- **2/5** — Très convoité (grand groupe tech, conseil prestige) — fort volume, barre haute
- **1/5** — FAANG / MBB / process ultra-sélectif avec viviers d'écoles cibles
- **0/5** — Quasi inaccessible sans pedigree spécifique

### P6. Accessibilité & signaux favorables (poids : 10%)

Langue, localisation, réseau, ouverture du poste.

- **5/5** — Langue maîtrisée, localisation idéale, recommandation interne possible, poste ouvert largement
- **4/5** — Bons signaux, pas d'obstacle d'accès
- **3/5** — Neutre
- **2/5** — Un obstacle d'accès (langue exigée limite, process très long, poste presque pourvu)
- **1/5** — Plusieurs obstacles
- **0/5** — Barrière rédhibitoire (mobilité, langue non maîtrisée)

## Calcul de la probabilité

```
Score proba sur 5 = somme des (note × poids) / 100
```

| Tier | Score | Signification |
|---|---|---|
| **Élevée** | 4,0 à 5,0 | Je suis un candidat évident/fort. Ça vaut largement l'effort. |
| **Moyenne** | 2,5 à 3,9 | J'ai une chance réelle mais pas gagnée. Soigner la candidature pour lever les doutes. |
| **Faible** | < 2,5 | Peu de chances. Ne candidater que si la désirabilité est très haute (stretch assumé) ou réseau. |

### Malus de probabilité (plafonnent la proba à "Faible")

- Compétence centrale du poste totalement absente de mon profil (ex : data engineering, PhD requis)
- Filtre diplôme fermé non négociable (ex : "ingénieur exclusivement")
- Exigence d'années très au-dessus (ex : 7+ ans quand j'en ai 3,5)

### Bonus de probabilité (+ un demi-tier)

- Mon expérience plateforme (Meta officiel) explicitement préférée dans l'annonce
- Recommandation interne identifiée
- Entreprise dont j'ai géré le compte annonceur chez Concentrix
- Pénurie connue sur ce type de profil (ex : experts tracking/CAPI)

---

# DRAPEAU TIMING — Compatibilité date de démarrage

**Disponibilité cible : septembre 2026** — contrainte logistique (retour de Berlin, logement à sécuriser à Paris), PAS contractuelle. Severance Concentrix reçue fin mai 2026 → déjà libre côté emploi, disponible pour les process dès maintenant. Septembre = scénario confortable ; démarrage anticipé négociable pour une offre forte (logement temporaire, hybride au départ).

Pour chaque annonce, évaluer un **drapeau** (pas une note pondérée) selon la date de démarrage / l'urgence affichée :

| Drapeau | Quand | Effet |
|---|---|---|
| 🟢 **Compatible** | Pas de date imposée, date ≥ septembre, "selon profil", ou poste de création | Aucun impact, candidater normalement |
| 🟡 **À négocier** | Démarrage été ou "ASAP" mais poste pointu/senior où ils peuvent attendre le bon profil | Candidater en annonçant clairement ma dispo septembre dès le call RH |
| 🔴 **Risqué / incompatible** | Démarrage immédiat impératif, remplacement urgent, "ASAP" sur un poste très demandé avec vivier de candidats dispo | **Plafonne la probabilité d'embauche à "Faible"** — ils choisiront probablement un candidat dispo tout de suite |

**Calendrier de candidature optimal** (pour une prise de poste septembre, en comptant 4-8 semaines de process + préavis) : candidater entre **juin et juillet**. Ne pas attendre septembre. Lancer dès maintenant les process longs (grands groupes, plateformes type Microsoft) et caler les démarrages "ASAP" plutôt en juillet.

---

# MATRICE DE PRIORISATION (croisement des 2 axes)

C'est elle qui décide de l'action finale.

| Désirabilité ↓ \\ Proba → | **Élevée** | **Moyenne** | **Faible** |
|---|---|---|---|
| **A / B** (4,0+) | 🎯 **Priorité 1** — fonce, candidature soignée sous 24-48h | ✅ **Priorité 2** — candidate, soigne la LM pour lever les doutes | ⚡ **Stretch** — candidate si vraiment motivé, sans surinvestir |
| **C** (3,0-3,9) | 🟡 **Plan B utile** — candidate, c'est accessible et correct | 🤔 **Optionnel** — seulement si peu d'autres pistes | ❌ **Laisse** — effort > retour |
| **D / F** (<3,0) | 🟢 **Alimentaire** — seulement si besoin urgent de job | ❌ **Laisse** | ❌ **Laisse** |

**Règle d'or si l'objectif = décrocher un poste vite** : prioriser la colonne "Proba Élevée", lignes A/B/C. Ce sont les postes que je veux ET que je peux obtenir.

---

## Format de sortie attendu

Pour chaque annonce évaluée, retourne un bloc structuré comme ceci :

```
## [Nom du poste] — [Entreprise]
**URL** : [lien]
**Date d'annonce** : [date]

### Axe 1 — Désirabilité
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

**Désirabilité : x,x / 5 → Note [A/B/C/D/F]**

### Axe 2 — Probabilité d'embauche
| Dimension | Note | Poids | Commentaire |
|---|---|---|---|
| Compétences obligatoires | x/5 | 35% | ... |
| Séniorité / années | x/5 | 20% | ... |
| Formation / filtre diplôme | x/5 | 10% | ... |
| Différenciation | x/5 | 15% | ... |
| Sélectivité employeur | x/5 | 10% | ... |
| Accessibilité | x/5 | 10% | ... |

**Probabilité : x,x / 5 → Tier [Élevée / Moyenne / Faible]**

**Drapeau timing : [🟢 Compatible / 🟡 À négocier / 🔴 Risqué] — [date de démarrage de l'annonce + commentaire dispo septembre]**

### Verdict croisé
**Désirabilité [A-F] × Proba [tier] (drapeau timing) → [case de la matrice : Priorité 1 / Priorité 2 / Stretch / Plan B / Optionnel / Laisse]**

### Synthèse
- ✅ Points forts du match : ...
- ⚠️ Points faibles / gaps à anticiper : ...
- 🔑 Leviers pour augmenter mes chances : [ce qu'il faut soigner dans la candidature pour lever les doutes recruteur]
- 🎯 Recommandation : [action issue de la matrice]

### Mots-clés à injecter dans le CV
[liste des termes exacts de l'annonce à reprendre dans la version adaptée]

### Angle de la lettre de motivation
[en 2-3 lignes : quel angle privilégier pour cette annonce spécifiquement]
```
