# 📱📺 Evolution des usages de consommation médias chez les jeunes adultes

> 🇫🇷 **[Français](#français)** · 🇬🇧 **[English](#english)**

---

## Français

### 📌 Présentation du projet

Ce projet de recherche data examine la relation entre la montée en puissance des réseaux sociaux numériques et des plateformes de streaming, et le déclin structurel de la consommation des médias traditionnels chez les jeunes adultes (18–34 ans).

Il s'inscrit dans une démarche scientifique combinant :
- **Collecte de données multi-sources** (scraping, APIs, open data)
- **Analyse exploratoire des données** (EDA) via Python
- **Visualisation de données** avancée

---

### 🔬 Problématique

> *"Dans quelle mesure la montée en puissance des réseaux sociaux numériques et des plateformes de streaming est-elle associée au déclin structurel de la consommation des médias traditionnels (télévision, cinéma, presse) chez les jeunes adultes (18–34 ans)
> Nous réaliserons ici une analyse temporelle et comparatrice couvrant dix ans de données (2013–2024)."*

---

### 📐 Hypothèses de recherche

| Hypothèse | Énoncé |
|---|---|
| **H1** | La progression du temps passé sur les réseaux sociaux est corrélée négativement avec la durée d'écoute TV chez les 18-34 ans |
| **H2** | Le streaming joue un rôle médiateur : il capte d'abord l'audience TV avant d'être lui-même concurrencé par les réseaux sociaux |
| **H3** | L'effet est générationnel et s'accentue dans le temps - le fossé entre jeunes et seniors se creuse chaque année |

---

### 🗂️ Structure du projet

```
📦 social-media-vs-traditional-media/
│
├── README.md                          ← Ce fichier
├── RESEARCH_FRAMEWORK.md              ← Cadre scientifique complet
│
├── 01_data_collection/                ← Scripts de collecte
│   ├── scrape_ourworldindata.py       ← API Our World in Data
│   ├── scrape_reuters_dnr.py          ← Reuters Institute DNR
│   └── collect_cnc_mediametrie.py     ← Données France (CNC)
│
├── 02_data/
│   ├── raw/                           ← Données brutes (non modifiées)
│   └── processed/                     ← Données nettoyées
│
├── 03_notebooks/
│   ├── 01_cleaning_wrangling.ipynb    ← Nettoyage & préparation
│   ├── 02_eda_exploratory.ipynb       ← Analyse exploratoire
│   └── 03_dataviz_final.ipynb         ← Visualisations finales
│
├── 04_dashboard/
│   └── dashboard_media_trends.pbix    ← Dashboard Power BI
│
└── 05_outputs/
    ├── graphs/                        ← Exports graphiques
    └── report_summary.md              ← Synthèse des résultats
```

---

### 🛠️ Stack technique

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat)
![PowerBI](https://img.shields.io/badge/Power_BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)

**Librairies Python :** `pandas`, `numpy`, `matplotlib`, `seaborn`, `requests`, `beautifulsoup4`, `scipy`

---

### 📊 Sources de données

| Source | Contenu | Couverture |
|---|---|---|
| Our World in Data | Temps passé sur médias numériques / TV | Multi-pays, 2013–2024 |
| Reuters Institute DNR | Usage réseaux sociaux vs TV par âge | 47 pays, 2013–2025 |
| DataReportal / GWI | Temps social media vs streaming mondial | Mondial, 2017–2024 |
| CNC / Médiamétrie | TV France 15-49/50+ (série longue) | France, 2009–2023 |
| CNC Chiffres clés 2024 + Médiamat 2018 | TV France **15-34 ans** (série fine, multi-sources) | France, 2013–2023 |

> ⚠️ **Note 2024 :** Médiamétrie a adopté une nouvelle méthodologie au 01/01/2024 (tous foyers, tous lieux, tous écrans — population élargie de 57,3M → 62,6M). Les données 2024 **ne sont pas comparables** à la série historique et sont encodées comme `NaN` documenté dans tous les datasets TV.

---

### 👩‍💻 Auteure

**Inès Amdjahed** — Data analyst spécialisée en sciences sociales & études médias
📧 amdjahedines@gmail.com · 💼 [LinkedIn](https://linkedin.com/in/ines-amdjahed)

---
---

## English

### 📌 Project overview

This data research project examines the relationship between the rise of social media and streaming platforms, and the structural decline of traditional media consumption among young adults (18–34).

It follows a rigorous scientific approach combining:
- **Multi-source data collection** (scraping, APIs, open data)
- **Exploratory Data Analysis** (EDA) via Python
- **Advanced data visualization**
- **Interactive dashboard** via Power BI

---

### 🔬 Research Question

> *"To what extent is the rise of social media and streaming platforms associated with the structural decline of traditional media consumption (linear TV, cinema, print press) among young adults (18–34)? A longitudinal, multi-country comparative analysis (2013–2024)."*

---

### 📐 Research Hypotheses

| Hypothesis | Statement |
|---|---|
| **H1** | Growth in social media time spent is negatively correlated with linear TV viewing among 18-34s |
| **H2** | Streaming acts as a mediator: it first captures TV audiences before being itself displaced by social media |
| **H3** | The effect is generational and widening — the gap between youth and seniors grows each year |

---

### 🛠️ Tech Stack

**Languages & Libraries:** Python (pandas, numpy, matplotlib, seaborn, requests, bs4, scipy)
**Tools:** Jupyter Notebook, VS Code, Power BI, GitHub

---

### 📊 Data Sources

| Source | Content | Coverage |
|---|---|---|
| Our World in Data | Time spent on digital media / TV | Multi-country, 2013–2024 |
| Reuters Institute DNR | Social media vs TV usage by age | 47 countries, 2013–2025 |
| DataReportal / GWI | Social media vs streaming time | Global, 2017–2024 |
| CNC / Médiamétrie | TV France 15-49/50+ long series | France, 2009–2023 |
| CNC Chiffres clés 2024 + Médiamat 2018 | TV France **15-34 age bracket** (multi-source) | France, 2013–2023 |

---

### 👩‍💻 Author

**Inès Amdjahed** — M2 Information & Communication: Data and Society
Université Paris Nanterre · 2024
📧 ines.amdjahed@email.com · 💼 [LinkedIn](https://linkedin.com/in/ines-amdjahed)
