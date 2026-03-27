# Cadre de Recherche / Research Framework

> **[Français](#français)** ·  **[English](#english)**

---

## Français

### 1. Contexte & Justification

La transformation des habitudes médiatiques constitue l'un des phénomènes sociaux les plus documentés de la dernière décennie. Depuis l'émergence des smartphones (2007) et l'essor des plateformes sociales (2010–2015), les comportements de consommation médiatique ont connu une mutation profonde, particulièrement marquée chez les jeunes adultes.

Deux tendances simultanées et potentiellement liées sont observées :
1. Une **croissance exponentielle** du temps passé sur les réseaux sociaux numériques (Instagram, TikTok, YouTube, X/Twitter)
2. Un **déclin structurel** de la consommation des médias traditionnels — télévision linéaire, cinéma, presse papier

Ce projet vise à **quantifier et caractériser** la relation entre ces deux phénomènes à partir de données empiriques multi-sources et multi-pays.

---

### 2. Problématique

> *"Dans quelle mesure la montée en puissance des réseaux sociaux numériques et des plateformes de streaming est-elle associée au déclin structurel de la consommation des médias traditionnels (télévision linéaire, cinéma, presse) chez les jeunes adultes (18–34 ans) ? Une analyse longitudinale et comparative multi-pays (2013–2024)."*

Cette problématique se décline en trois sous-questions :

- **SQ1** — Existe-t-il une corrélation statistiquement significative entre la croissance du temps passé sur les réseaux sociaux et la baisse de consommation TV chez les 18-34 ans ?
- **SQ2** — Le streaming (Netflix, Disney+, YouTube) constitue-t-il une étape intermédiaire dans ce décrochage, ou un phénomène distinct ?
- **SQ3** — L'effet est-il uniforme selon les pays, les générations, et les types de médias traditionnels ?

---

### 3. Hypothèses de recherche

#### H1 — Hypothèse de substitution directe
*La progression du temps passé sur les réseaux sociaux est corrélée négativement avec la durée d'écoute TV linéaire chez les 18-34 ans.*

**Indicateurs mesurables :**
- Temps moyen quotidien sur réseaux sociaux (minutes/jour) par tranche d'âge
- Durée d'écoute TV linéaire (minutes/jour) par tranche d'âge
- Coefficient de corrélation de Pearson entre les deux séries temporelles

**Résultat attendu :** r < -0.6, p < 0.05

---

H2 — Hypothèse de concomitance plateformes / chute TV
*L'explosion des plateformes sociales courtes (TikTok, Instagram Reels) coïncide temporellement avec la période de chute TV la plus prononcée chez les 15-34 ans (2018–2023), suggérant un effet de substitution directe de l'attention.*

**Indicateurs mesurables :**
- Croissance MAU des principales plateformes sociales (2012–2024)
- Superposition avec la période de chute TV 15-34 ans la plus forte (−52% en 5 ans)
- Analyse des ruptures de tendance (breakpoint 2018 / COVID 2020)

**Résultat attendu :** Corrélation temporelle entre explosion MAU TikTok (+1.7B, 2018–2021) et accélération du décrochage TV 15-34
---

#### H3 — Hypothèse de fracture générationnelle
*L'effet est générationnel et s'accentue dans le temps — le fossé entre jeunes (18-34) et seniors (50+) se creuse chaque année.*

**Indicateurs mesurables :**
- Écart de durée d'écoute TV entre 18-34 ans et 50+ ans (delta en minutes)
- Évolution de cet écart de 2013 à 2024
- Test de tendance linéaire (régression)

**Résultat attendu :** Pente positive significative de l'écart générationnel

---

### 4. Méthodologie

#### 4.1 Type de recherche
Étude **quantitative longitudinale et comparative** basée sur des données secondaires agrégées.

#### 4.2 Périmètre
- **Temporel :** 2013–2024 (période couvrant l'essor des smartphones et réseaux sociaux)
- **Géographique :** Multi-pays (France, États-Unis, Royaume-Uni, Allemagne, pays nordiques)
- **Population cible :** Jeunes adultes 18–34 ans, comparés aux 35-49 ans et 50+ ans

#### 4.3 Pipeline de traitement des données

```
Collecte (scraping/API)
        ↓
Nettoyage & harmonisation (pandas)
        ↓
Analyse exploratoire — EDA (Python)
        ↓
Tests statistiques (corrélation, régression)
        ↓
Visualisations finales (matplotlib/seaborn)
        ↓
Dashboard interactif (Power BI)
```

#### 4.4 Limites méthodologiques
- Les données agrégées ne permettent pas d'inférer la causalité, seulement la corrélation
- Les ruptures méthodologiques dans les séries (changements de périmètre de mesure) doivent être signalées
- Les données auto-déclarées (sondages) peuvent être soumises à des biais de désirabilité sociale
- La comparabilité internationale reste limitée par les différences de méthodes de collecte

---

### 5. Cadre théorique

Ce projet s'appuie sur trois courants théoriques :

**Theory of Media Displacement (Neuman, 1991)**
L'adoption d'un nouveau média tend à réduire le temps consacré aux médias préexistants, notamment lorsqu'ils satisfont des besoins similaires (information, divertissement).

**Uses and Gratifications Theory (Katz, Blumler & Gurevitch, 1974)**
Les individus choisissent activement les médias en fonction des gratifications qu'ils en attendent. Les réseaux sociaux offrent des gratifications supplémentaires (interaction sociale, production de contenu) absentes des médias traditionnels.

**Digital Native vs Digital Immigrant (Prensky, 2001)**
Les cohortes nées après 1995 ont développé des habitudes médiatiques nativement numériques, rendant leur décrochage des médias traditionnels structurellement différent de celui des générations précédentes.

---

### 6. Variables

| Variable | Type | Source | Mesure |
|---|---|---|---|
| Temps réseaux sociaux | Continue, indépendante | GWI / OWID | Minutes/jour |
| Durée écoute TV | Continue, dépendante | Médiamétrie / OWID | Minutes/jour |
| Temps streaming | Continue, médiatrice | Netflix IR / OWID | Minutes/jour |
| Tranche d'âge | Catégorielle | Toutes sources | 18-34 / 35-49 / 50+ |
| Pays | Catégorielle | Toutes sources | ISO 3166 |
| Année | Temporelle | Toutes sources | 2013–2024 |

---
---

## English

### 1. Context & Rationale

The transformation of media habits is one of the most documented social phenomena of the last decade. Since the emergence of smartphones (2007) and the rise of social platforms (2010–2015), media consumption behaviors have undergone a profound shift, particularly among young adults.

Two simultaneous and potentially related trends are observed:
1. **Exponential growth** in time spent on social media (Instagram, TikTok, YouTube, X/Twitter)
2. **Structural decline** in traditional media consumption — linear TV, cinema, print press

This project aims to **quantify and characterize** the relationship between these two phenomena using empirical, multi-source, multi-country data.

---

### 2. Research Question

> *"To what extent is the rise of social media and streaming platforms associated with the structural decline of traditional media consumption (linear TV, cinema, print press) among young adults (18–34)? A longitudinal, multi-country comparative analysis (2013–2024)."*

Three sub-questions:
- **SQ1** — Is there a statistically significant correlation between social media growth and declining TV consumption among 18-34s?
- **SQ2** — Does streaming act as an intermediate step in this disengagement, or is it a distinct phenomenon?
- **SQ3** — Is the effect uniform across countries, generations, and types of traditional media?

---

### 3. Research Hypotheses

#### H1 — Direct Substitution Hypothesis
*Growth in social media time spent is negatively correlated with linear TV viewing among 18-34s.*

**Expected result:** r < -0.6, p < 0.05

#### H2 — Streaming Mediation Hypothesis
*Streaming acts as a mediator: it first captures TV audiences before being itself displaced by social media.*

**Expected result:** Streaming peaks ~2018-2020, then stabilizes as social media dominates

#### H3 — Generational Gap Hypothesis
*The effect is generational and widening — the gap between youth (18-34) and seniors (50+) grows each year.*

**Expected result:** Statistically significant positive trend in generational gap

---

### 4. Methodology

#### 4.1 Research Type
**Quantitative longitudinal and comparative study** based on aggregated secondary data.

#### 4.2 Scope
- **Temporal:** 2013–2024
- **Geographic:** Multi-country (France, US, UK, Germany, Nordic countries)
- **Target population:** Young adults 18–34, compared to 35-49 and 50+

#### 4.3 Data Processing Pipeline

```
Collection (scraping/API)
        ↓
Cleaning & harmonization (pandas)
        ↓
Exploratory Data Analysis (Python)
        ↓
Statistical tests (correlation, regression)
        ↓
Final visualizations (matplotlib/seaborn)
        ↓
Interactive dashboard (Power BI)
```

#### 4.4 Methodological Limitations
- Aggregated data cannot establish causality, only correlation
- Methodological breaks in time series must be flagged
- Self-reported data (surveys) may be subject to social desirability bias
- International comparability is limited by differences in collection methods

---

### 5. Theoretical Framework

**Theory of Media Displacement (Neuman, 1991)**
Adoption of a new medium tends to reduce time devoted to pre-existing media, particularly when they satisfy similar needs.

**Uses and Gratifications Theory (Katz, Blumler & Gurevitch, 1974)**
Individuals actively choose media based on expected gratifications. Social networks offer additional gratifications (social interaction, content creation) absent from traditional media.

**Digital Native vs Digital Immigrant (Prensky, 2001)**
Cohorts born after 1995 developed natively digital media habits, making their disengagement from traditional media structurally different from previous generations.

---

### 6. Variables

| Variable | Type | Source | Measure |
|---|---|---|---|
| Social media time | Continuous, independent | GWI / OWID | Min/day |
| TV viewing duration | Continuous, dependent | Médiamétrie / OWID | Min/day |
| Streaming time | Continuous, mediator | Netflix IR / OWID | Min/day |
| Age group | Categorical | All sources | 18-34 / 35-49 / 50+ |
| Country | Categorical | All sources | ISO 3166 |
| Year | Temporal | All sources | 2013–2024 |
