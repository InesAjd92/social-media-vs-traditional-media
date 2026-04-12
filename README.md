## English

### Project overview

This data research project quantifies the relationship between the rise of social media platforms and the structural decline of linear TV consumption among young adults (15–34) in France, over a ten-year period (2013–2023).

Three hypotheses are tested and confirmed on empirical data from primary institutional sources (CNC, Médiamétrie, GWI).

---

### Research Question

> "To what extent is the rise of social media platforms associated with the structural decline of linear TV consumption among young adults (15–34)?"

---

### Research Hypotheses

| Hypothesis | Statement | Result |
|---|---|---|
| H1 | Growth in social media time is negatively correlated with linear TV viewing among 15–34s | Confirmed : r = -0.784, p < 0.01 |
| H2 | The explosion of short-form platforms (TikTok, Reels) coincides with the sharpest TV decline period among 15–34s (2018–2023) | Confirmed : temporal concomitance |
| H3 | The generational gap in TV consumption between 50+ and 15–34s widens each year | Confirmed : +10.7 min/year, p < 0.001 |

---

### Tech Stack

- TV viewing among 15–34s fell by **52%** between 2013 and 2023 (155 to 74 min/day)
- Pearson correlation: **r = -0.784** (vs -0.674 with the broader 15–49 bracket, demonstrating the dilution effect of over-aggregation)
- Generational gap reached **4 hours 2 minutes per day** in 2023 (50+ vs 15–34s)
- TikTok growth (+1.7B MAU, 2018–2021) temporally coincides with the steepest phase of TV decline

---

### Data Sources

| Source | Content | Coverage |
|---|---|---|
| GWI via DataReportal | Daily time on social media | Global averages, 2013–2024 |
| Reuters Institute DNR | Social media vs TV usage by age group | 47 countries, 2013–2024 |
| CNC Chiffres clés 2024 | TV France 15–34 (multi-source reconstruction) | France, 2013–2023 |
| CNC / Médiamétrie | TV France 15–49 / 50+ long series | France, 2009–2023 |
| Meta, ByteDance, Snap, Alphabet earnings | Platform MAU | Global, 2012–2024 |

> **Note on 2024 data:** Médiamétrie adopted a new methodology on 01/01/2024 (all households, all locations, all screens). 2024 data are not comparable to the historical series and are documented as `NaN` across all TV datasets.

> **Note on age brackets:** The main bracket is 15–34 (multi-source reconstruction). The 15–49 series is retained for comparison to demonstrate the dilution effect of over-aggregation. Data at the 18–24 level are not available in long series from French institutional sources.

---

### Author

**Inès Amdjahed** : Data analyst
amdjahedines@gmail.com · [LinkedIn](https://linkedin.com/in/ines-amdjahed) · [Portfolio](https://inesajd92.github.io/)

---
---

## Français

### Présentation du projet

Ce projet de recherche data quantifie la relation entre la montée en puissance des réseaux sociaux et le déclin structurel de la consommation TV chez les jeunes adultes (15–34 ans) en France, sur une période de dix ans (2013–2023).

Trois hypothèses sont testées et confirmées sur des données empiriques issues de sources institutionnelles primaires (CNC, Médiamétrie, GWI).

---

### Problématique

> "Dans quelle mesure la montée en puissance des réseaux sociaux est-elle associée au déclin structurel de la consommation TV linéaire chez les jeunes adultes (15–34 ans) ?"

---

### Hypothèses

| Hypothèse | Énoncé | Résultat |
|---|---|---|
| H1 | La progression du temps passé sur les réseaux sociaux est corrélée négativement avec la durée d'écoute TV chez les 15–34 ans | Confirmée : r = -0,784, p < 0,01 |
| H2 | L'explosion des plateformes courtes (TikTok, Reels) coïncide avec la période de chute TV la plus prononcée chez les 15–34 ans (2018–2023) | Confirmée : concomitance temporelle |
| H3 | Le fossé de consommation TV entre les 50 ans+ et les 15–34 ans se creuse chaque année | Confirmée : +10,7 min/an, p < 0,001 |

---

### Résultats clés

- La consommation TV des 15–34 ans a chuté de **52 %** entre 2013 et 2023 (155 à 74 min/jour)
- Corrélation de Pearson : **r = -0,784** (vs -0,674 avec la tranche 15–49, ce qui illustre l'effet de dilution de l'agrégation)
- Le fossé générationnel atteint **4 heures 2 minutes par jour** en 2023 (50 ans+ vs 15–34 ans)
- L'explosion de TikTok (+1,7 milliard de MAU, 2018–2021) coïncide temporellement avec la phase de décrochage TV la plus prononcée

---

### Structure du projet

```
social-media-vs-traditional-media/
|
|-- README.md
|-- RESEARCH_FRAMEWORK.md          <- Cadre scientifique complet
|
|-- 01_data_collection/
|   |-- scrape_ourworldindata.py
|   |-- scrape_reuters_dnr.py
|   `-- collect_cnc_mediametrie.py
|
|-- 02_data/
|   |-- raw/
|   `-- processed/
|
|-- 03_notebooks/
|   |-- 01_cleaning_wrangling.ipynb
|   |-- 02_eda_exploratory.ipynb
|
`-- 05_outputs/
    |-- graphs/
    `-- report_summary.md
```

---

### Stack technique

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Scipy](https://img.shields.io/badge/Scipy-8CAAE6?style=flat&logo=scipy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat)
![PowerBI](https://img.shields.io/badge/Power_BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)

`pandas` · `numpy` · `matplotlib` · `seaborn` · `scipy` · `requests` · `beautifulsoup4`

---

### Sources de données

| Source | Contenu | Couverture |
|---|---|---|
| GWI via DataReportal | Temps quotidien sur les réseaux sociaux | Moyennes mondiales, 2013–2024 |
| Reuters Institute DNR | Usage réseaux sociaux vs TV par tranche d'âge | 47 pays, 2013–2024 |
| CNC Chiffres clés 2024 | TV France 15–34 ans (reconstruction multi-sources) | France, 2013–2023 |
| CNC / Médiamétrie | TV France 15–49 / 50+ (série longue) | France, 2009–2023 |
| Rapports financiers Meta, ByteDance, Snap, Alphabet | MAU des plateformes | Mondial, 2012–2024 |

> **Note 2024 :** Médiamétrie a adopté une nouvelle méthodologie au 01/01/2024 (tous foyers, tous lieux, tous écrans). Les données 2024 ne sont pas comparables à la série historique et sont documentées comme `NaN` dans tous les datasets TV.

> **Note sur les tranches d'âge :** la tranche principale est les 15–34 ans (reconstruction multi-sources). La série 15–49 est conservée en comparaison pour illustrer l'effet de dilution de l'agrégation. Les données à la granularité 18–24 ans ne sont pas disponibles en série longue auprès des sources institutionnelles françaises.

---

### Auteure

**Inès Amdjahed** : Data analyst
amdjahedines@gmail.com · [LinkedIn](https://linkedin.com/in/ines-amdjahed) · [Portfolio](https://inesajd92.github.io/)