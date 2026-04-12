# Cadre de recherche / Research framework

> **[Français](#français)** ·  **[English](#english)**

---

## Français

### 1. Contexte & justification

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

=======
# Cadre de recherche

**[English](#english)** · **[Français](#français)**

---

## English

### 1. Context

The transformation of media habits is one of the most documented social phenomena of the last decade. Since the emergence of smartphones (2007) and the rise of social platforms (2010–2015), media consumption behaviors have undergone a profound shift, particularly among young adults.

Two simultaneous and potentially related trends are observed:

1. Exponential growth in time spent on social media (Instagram, TikTok, YouTube, X/Twitter)
2. Structural decline in traditional media consumption: linear TV, cinema, print press

This project aims to quantify and characterize the relationship between these two phenomena using empirical, multi-source, multi-country data.

---

### 2. Research question

> "To what extent is the rise of social media platforms associated with the structural decline of traditional media consumption among young adults (15–34)?"

Three sub-questions:

- **SQ1** : Is there a statistically significant correlation between social media growth and declining TV viewing among 15–34s?
- **SQ2** : Does the explosion of short-form platforms (TikTok, Instagram Reels) temporally coincide with the sharpest TV decline period, suggesting a direct attention substitution effect?
- **SQ3** : Is the effect generational and widening over time?

---

### 3. Research hypotheses

#### H1 : Direct substitution hypothesis
*Growth in time spent on social media is negatively correlated with linear TV viewing among 15–34s.*

**Measurable indicators:**
- Average daily time on social media (min/day) by age group
- Linear TV viewing duration (min/day) by age group
- Pearson correlation coefficient between the two time series

**Expected result:** r < -0.6, p < 0.05

---

#### H2 : Platform concomitance hypothesis
*The explosion of short-form social platforms (TikTok, Instagram Reels) temporally coincides with the sharpest TV decline period among 15–34s (2018–2023), suggesting a direct attention substitution effect.*

**Measurable indicators:**
- Monthly active user (MAU) growth of major social platforms (2012–2024)
- Overlap with the period of strongest TV decline among 15–34s (−52% over 5 years)
- Breakpoint analysis (2018 inflection / COVID 2020 anomaly)

**Expected result:** Temporal correlation between TikTok MAU explosion (+1.7B, 2018–2021) and accelerated TV decline among 15–34s.

**Methodological note:** This hypothesis rests on a temporal concomitance analysis rather than a formally tested mediation model, due to the absence of SVOD viewing time data in long time series.

---

#### H3 : Generational gap hypothesis
*The effect is generational and widening : the gap in TV consumption between 50+ and 15–34s grows each year.*

**Measurable indicators:**
- Gap in TV viewing duration between 15–34s and 50+ (delta in minutes)
- Evolution of this gap from 2013 to 2023
- Linear trend test (regression)

**Expected result:** Statistically significant positive slope in the generational gap.

---

### 4. Methodology

#### 4.1 Research type
Quantitative study based on aggregated secondary data.

#### 4.2 Scope
- **Temporal:** 2013–2023 (2024 = documented NaN, Médiamétrie methodology break)
- **Geographic:** France (primary), with international comparison via GWI 2024
- **Target population:** Young adults 15–34, compared to 50+

**Note on age brackets:** The main bracket is 15–34 (multi-source reconstruction from CNC and Médiamat). The CNC official series publishes 15–49, which is retained for comparison to demonstrate the dilution effect of over-aggregation. Data at the 18–24 level are not available in long series from French institutional sources (CNC/Médiamétrie); punctual 18–24 data from Reuters Institute DNR and GWI are used for international comparison only.

#### 4.3 Data processing pipeline

```
Collection (scraping / API)
    |
Cleaning and harmonization (pandas)
    |
Exploratory data analysis (Python)
    |
Statistical tests (correlation, regression)
    |
Final visualizations (matplotlib / seaborn)
    |
Interactive dashboard (Power BI)
```

#### 4.4 Methodological limitations
- Aggregated data cannot establish causality, only correlation
- Methodological breaks in time series must be flagged (2024 Médiamétrie break documented as NaN)
- Self-reported data (surveys) may be subject to social desirability bias
- International comparability is limited by differences in data collection methods
- GWI social media data are global averages, not France-specific

---

### 5. Theoretical framework

**Theory of media displacement (Neuman, 1991)**
Adoption of a new medium tends to reduce time devoted to pre-existing media, particularly when they satisfy similar needs (information, entertainment).

**Uses and gratifications theory (Katz, Blumler & Gurevitch, 1974)**
Individuals actively choose media based on expected gratifications. Social networks offer additional gratifications (social interaction, content creation) absent from traditional media.

**Digital native vs digital immigrant (Prensky, 2001)**
Cohorts born after 1995 developed natively digital media habits, making their disengagement from traditional media structurally different from previous generations.

---

### 6. Variables

| Variable | Type | Source | Measure |
|---|---|---|---|
| Social media time | Continuous, independent | GWI via DataReportal | Min/day |
| TV viewing duration | Continuous, dependent | CNC / Médiamétrie | Min/day |
| Platform MAU | Continuous, contextual | Meta, ByteDance, Snap, Alphabet earnings | Millions |
| Age group | Categorical | All sources | 15-34 / 15-49 / 50+ |
| Country | Categorical | GWI | ISO 3166 |
| Year | Temporal | All sources | 2013–2023 |

---
---

## Français

### 1. Contexte

La transformation des habitudes médiatiques constitue l'un des phénomènes sociaux les plus documentés de la dernière décennie. Depuis l'émergence des smartphones (2007) et l'essor des plateformes sociales (2010–2015), les comportements de consommation médiatique ont connu une mutation profonde, particulièrement marquée chez les jeunes adultes.

Deux tendances simultanées et potentiellement liées sont observées :

1. Une croissance exponentielle du temps passé sur les réseaux sociaux numériques (Instagram, TikTok, YouTube, X/Twitter)
2. Un déclin structurel de la consommation des médias traditionnels : télévision linéaire, cinéma, presse papier

Ce projet vise à quantifier et caractériser la relation entre ces deux phénomènes à partir de données empiriques multi-sources et multi-pays.

---

### 2. Problématique

> "Dans quelle mesure la montée en puissance des réseaux sociaux numériques est-elle associée au déclin structurel de la consommation des médias traditionnels chez les jeunes adultes (15–34 ans) ?"

Cette problématique se décline en trois sous-questions :

- **SQ1** : Existe-t-il une corrélation statistiquement significative entre la croissance du temps passé sur les réseaux sociaux et la baisse de consommation TV chez les 15–34 ans ?
- **SQ2** : L'explosion des plateformes courtes (TikTok, Instagram Reels) coïncide-t-elle avec la période de chute TV la plus prononcée, suggérant un effet de substitution directe de l'attention ?
- **SQ3** : L'effet est-il générationnel et s'accentue-t-il dans le temps ?

---

### 3. Hypothèses de recherche

#### H1 : Hypothèse de substitution directe
*La progression du temps passé sur les réseaux sociaux est corrélée négativement avec la durée d'écoute TV linéaire chez les 15–34 ans.*

**Indicateurs mesurables :**
- Temps moyen quotidien sur réseaux sociaux (min/jour) par tranche d'âge
- Durée d'écoute TV linéaire (min/jour) par tranche d'âge
- Coefficient de corrélation de Pearson entre les deux séries temporelles

**Résultat attendu :** r < -0,6, p < 0,05

---

#### H2 : Hypothèse de concomitance plateformes / chute TV
*L'explosion des plateformes sociales courtes (TikTok, Instagram Reels) coïncide temporellement avec la période de chute TV la plus prononcée chez les 15–34 ans (2018–2023), ce qui suggère un effet de substitution directe de l'attention.*

**Indicateurs mesurables :**
- Croissance des utilisateurs actifs mensuels (MAU) des principales plateformes sociales (2012–2024)
- Superposition avec la période de chute TV 15–34 ans la plus forte (−52% en 5 ans)
- Analyse des ruptures de tendance (inflexion 2018 / anomalie COVID 2020)

**Résultat attendu :** corrélation temporelle entre l'explosion MAU de TikTok (+1,7 milliard, 2018–2021) et l'accélération du décrochage TV chez les 15–34 ans.

**Note méthodologique :** cette hypothèse repose sur une analyse de concomitance temporelle, et non sur un modèle de médiation statistiquement testé, faute de données de temps de visionnage SVOD disponibles en série longue.

---

#### H3 : Hypothèse de fracture générationnelle
*L'effet est générationnel et s'accentue dans le temps : le fossé de consommation TV entre les 50 ans+ et les 15–34 ans se creuse chaque année.*

**Indicateurs mesurables :**
- Écart de durée d'écoute TV entre 15–34 ans et 50+ (delta en minutes)
- Évolution de cet écart de 2013 à 2023
- Test de tendance linéaire (régression)

**Résultat attendu :** pente positive significative de l'écart générationnel.

---

### 4. Méthodologie

#### 4.1 Type de recherche
Étude quantitative longitudinale basée sur des données secondaires agrégées.

#### 4.2 Périmètre
- **Temporel :** 2013–2023 (2024 = NaN documenté, rupture méthodologique Médiamétrie)
- **Géographique :** France (principal), comparaison internationale via GWI 2024
- **Population cible :** jeunes adultes 15–34 ans, comparés aux 50 ans+

**Note sur les tranches d'âge :** la tranche principale est les 15–34 ans (reconstruction multi-sources CNC et Médiamat). La série officielle CNC publie en 15–49, conservée en comparaison pour mettre en évidence l'effet de dilution de l'agrégation. Les données à la granularité 18–24 ans ne sont pas disponibles en série longue auprès des sources institutionnelles françaises (CNC/Médiamétrie) ; des données ponctuelles 18–24 issues du Reuters Institute DNR et de GWI sont utilisées uniquement pour la comparaison internationale.

#### 4.3 Pipeline de traitement des données

```
Collecte (scraping / API)
    |
Nettoyage et harmonisation (pandas)
    |
Analyse exploratoire (Python)
    |
Tests statistiques (corrélation, régression)
    |
Visualisations finales (matplotlib / seaborn)
    |
Dashboard interactif (Power BI)
```

#### 4.4 Limites méthodologiques
- Les données agrégées ne permettent pas d'inférer la causalité, seulement la corrélation
- Les ruptures méthodologiques dans les séries doivent être signalées (2024 documenté comme NaN)
- Les données auto-déclarées (sondages) peuvent être soumises à des biais de désirabilité sociale
- La comparabilité internationale reste limitée par les différences de méthodes de collecte
- Les données GWI sur le temps passé sur les réseaux sociaux sont des moyennes mondiales, non spécifiques à la France

---

### 5. Cadre théorique

**Théorie du déplacement médiatique (Neuman, 1991)**
L'adoption d'un nouveau média tend à réduire le temps consacré aux médias préexistants, notamment lorsqu'ils satisfont des besoins similaires (information, divertissement).

**Théorie des usages et des gratifications (Katz, Blumler et Gurevitch, 1974)**
Les individus choisissent activement les médias en fonction des gratifications qu'ils en attendent. Les réseaux sociaux offrent des gratifications supplémentaires (interaction sociale, production de contenu) absentes des médias traditionnels.

**Natif numérique vs immigrant numérique (Prensky, 2001)**
Les cohortes nées après 1995 ont développé des habitudes médiatiques nativement numériques, rendant leur décrochage des médias traditionnels structurellement différent de celui des générations précédentes.

---

### 6. Variables

| Variable | Type | Source | Mesure |
|---|---|---|---|
| Temps réseaux sociaux | Continue, indépendante | GWI via DataReportal | Min/jour |
| Durée d'écoute TV | Continue, dépendante | CNC / Médiamétrie | Min/jour |
| MAU des plateformes | Continue, contextuelle | Rapports financiers Meta, ByteDance, Snap, Alphabet | Millions |
| Tranche d'âge | Catégorielle | Toutes sources | 15-34 / 15-49 / 50+ |
| Pays | Catégorielle | GWI | ISO 3166 |
| Année | Temporelle | Toutes sources | 2013–2023 |