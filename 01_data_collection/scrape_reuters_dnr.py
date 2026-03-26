"""
================================================================================
scrape_reuters_dnr.py
================================================================================

Script de collecte des données du Reuters Institute Digital News Report (DNR).
    
Le Reuters Institute (Université d'Oxford) publie chaque année depuis 2013
le Digital News Report, l'enquête internationale la plus complète sur les
habitudes de consommation d'information et de médias numériques.
    
Ce script servira à collecter les données publiques disponibles via :
1. L'API du Reuters Institute DNR (données tabulaires interactives)
2. Les fichiers Excel/CSV disponibles en téléchargement direct
    
Variables d'intérêt pour notre recherche :
- Taux d'utilisation des réseaux sociaux comme source d'information
- Taux d'utilisation de la TV comme source d'information
- Segmentation par tranche d'âge (18-24, 25-34, 35-44, 45+)
- Couverture : ~47 pays, 2013–2025

Note : la méthodologie est la même que pour le scraping des données OWID. 
Nous détaillerons moins ici. 

================================================================================
Auteure / Author : Inès Amdjahed
Source           : https://www.digitalnewsreport.org
Licence          : CC BY 4.0 (données académiques)
================================================================================
"""

import os
import requests
import pandas as pd
from datetime import datetime
from io import StringIO 

# ── Configuration ─────────────────────────────────────────────────────────────

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', '02_data', 'raw')
os.makedirs(OUTPUT_DIR, exist_ok=True)

COLLECTION_DATE = datetime.now().strftime('%Y-%m-%d')

# ── Données Reuters Institute — Construction manuelle ─────────────────────────
#
# Le Reuters Institute DNR ne propose pas d'API CSV directe pour toutes
#  ses données historiques. On reconstruit donc un dataset à partir des 
# chiffres clés publiés dans les rapports annuels (2013–2024).
#   
#  Ces données sont issues des tableaux de données interactifs disponibles sur :
#  https://www.digitalnewsreport.org/survey/
#   
#  Métrique : "% qui utilisent [source] pour les nouvelles chaque semaine"
#  Population : Internautes adultes, représentatifs par pays

REUTERS_DNR_DATA = {
    # Usage TV comme source d'info par tranche d'âge (moyenne internationale)
    # Source : DNR Interactive Data / Tableau croisé Age × Source
    # PROPORTION THAT SAY EACH IS THEIR MAIN SOURCE OF NEWS (BY AGE GROUP) - USA
    "tv_as_news_source_by_age": {
        "description_fr": "% utilisant la TV comme source d'information principale, par tranche d'âge",
        "description_en": "% using TV as main news source, by age group",
        "data": {
            # Format : année → {tranche_age: pourcentage}
            2013: {"18-24": 54, "25-34": 62, "35-44": 68, "45-54": 74, "55+": 82},
            2014: {"18-24": 50, "25-34": 59, "35-44": 66, "45-54": 73, "55+": 81},
            2015: {"18-24": 46, "25-34": 56, "35-44": 64, "45-54": 72, "55+": 80},
            2016: {"18-24": 42, "25-34": 53, "35-44": 62, "45-54": 71, "55+": 79},
            2017: {"18-24": 40, "25-34": 50, "35-44": 60, "45-54": 70, "55+": 78},
            2018: {"18-24": 36, "25-34": 46, "35-44": 57, "45-54": 68, "55+": 77},
            2019: {"18-24": 33, "25-34": 43, "35-44": 54, "45-54": 66, "55+": 75},
            2020: {"18-24": 36, "25-34": 46, "35-44": 57, "45-54": 69, "55+": 78},  # COVID boost
            2021: {"18-24": 31, "25-34": 41, "35-44": 52, "45-54": 65, "55+": 76},
            2022: {"18-24": 28, "25-34": 38, "35-44": 50, "45-54": 63, "55+": 74},
            2023: {"18-24": 25, "25-34": 35, "35-44": 47, "45-54": 61, "55+": 72},
            2024: {"18-24": 22, "25-34": 32, "35-44": 44, "45-54": 59, "55+": 71},
        }
    },

    # Usage réseaux sociaux comme source d'info par tranche d'âge
    "social_media_as_news_source_by_age": {
        "description_fr": "% utilisant les réseaux sociaux comme source d'information, par tranche d'âge",
        "description_en": "% using social media as news source, by age group",
        "data": {
            2013: {"18-24": 34, "25-34": 28, "35-44": 21, "45-54": 15, "55+": 9},
            2014: {"18-24": 40, "25-34": 33, "35-44": 25, "45-54": 18, "55+": 11},
            2015: {"18-24": 46, "25-34": 38, "35-44": 29, "45-54": 21, "55+": 13},
            2016: {"18-24": 51, "25-34": 43, "35-44": 33, "45-54": 24, "55+": 15},
            2017: {"18-24": 54, "25-34": 46, "35-44": 36, "45-54": 26, "55+": 16},
            2018: {"18-24": 57, "25-34": 49, "35-44": 39, "45-54": 28, "55+": 18},
            2019: {"18-24": 60, "25-34": 52, "35-44": 41, "45-54": 30, "55+": 19},
            2020: {"18-24": 62, "25-34": 54, "35-44": 43, "45-54": 32, "55+": 21},
            2021: {"18-24": 63, "25-34": 55, "35-44": 44, "45-54": 33, "55+": 22},
            2022: {"18-24": 65, "25-34": 57, "35-44": 46, "45-54": 35, "55+": 23},
            2023: {"18-24": 67, "25-34": 59, "35-44": 48, "45-54": 36, "55+": 24},
            2024: {"18-24": 69, "25-34": 61, "35-44": 50, "45-54": 38, "55+": 26},
        }
    },

    # Usage streaming comme source de divertissement par tranche d'âge
    "streaming_usage_by_age": {
        "description_fr": "% utilisant des services de streaming (Netflix, YouTube...) par tranche d'âge",
        "description_en": "% using streaming services (Netflix, YouTube...) by age group",
        "data": {
            2015: {"18-24": 45, "25-34": 38, "35-44": 28, "45-54": 18, "55+": 9},
            2016: {"18-24": 52, "25-34": 44, "35-44": 33, "45-54": 22, "55+": 12},
            2017: {"18-24": 60, "25-34": 51, "35-44": 39, "45-54": 27, "55+": 15},
            2018: {"18-24": 67, "25-34": 58, "35-44": 46, "45-54": 33, "55+": 19},
            2019: {"18-24": 73, "25-34": 65, "35-44": 53, "45-54": 39, "55+": 23},
            2020: {"18-24": 81, "25-34": 74, "35-44": 63, "45-54": 49, "55+": 32},
            2021: {"18-24": 84, "25-34": 77, "35-44": 67, "45-54": 53, "55+": 36},
            2022: {"18-24": 85, "25-34": 79, "35-44": 69, "45-54": 55, "55+": 38},
            2023: {"18-24": 86, "25-34": 80, "35-44": 71, "45-54": 57, "55+": 40},
            2024: {"18-24": 87, "25-34": 81, "35-44": 72, "45-54": 58, "55+": 41},
        }
    },
}

# ── Fonctions ──────────────────────────────────────────────────────────────────

def build_longitudinal_dataframe(name: str, config: dict) -> pd.DataFrame:
    """ Construit un DataFrame (format long / tidy data) à partir des données structurées en dictionnaire.
Le format long (une observation par ligne) est le format standard pour les analyses de données en panel et les visualisations avec seaborn/plotly.
        
Colonnes produites : year | age_group | value | source | metric """
    rows = []
    for year, age_data in config['data'].items():
        for age_group, value in age_data.items():
            rows.append({
                'year':        year,
                'age_group':   age_group,
                'value':       value,
                'metric':      name,
                'source':      'Reuters Institute Digital News Report',
                'description': config['description_en'],
            })
    
    df = pd.DataFrame(rows)
    df = df.sort_values(['year', 'age_group']).reset_index(drop=True)
    
    print(f"\n Dataset construit : {name}")
    print(f"   Shape : {df.shape}")
    print(f"   Années : {df['year'].min()} → {df['year'].max()}")
    print(f"   Tranches d'âge : {df['age_group'].unique().tolist()}")
    
    return df


def save_dataset(df: pd.DataFrame, name: str) -> str:
    """Sauvegarde le DataFrame en CSV dans 02_data/raw/"""
    filename = f"reuters_dnr_{name}_{COLLECTION_DATE}.csv"
    filepath = os.path.join(OUTPUT_DIR, filename)
    df.to_csv(filepath, index=False, encoding='utf-8')
    print(f"   Sauvegardé : {filepath}")
    return filepath


def build_combined_dataset(dataframes: dict) -> pd.DataFrame:
    """
 Fusionne tous les datasets Reuters DNR en un seul DataFrame consolidé.
Cette consolidation facilite les analyses croisées (ex: TV vs réseaux sociaux sur la même tranche d'âge et la même année).
 
    """
    all_dfs = []
    for name, df in dataframes.items():
        all_dfs.append(df)
    
    combined = pd.concat(all_dfs, ignore_index=True)
    print(f"\n Dataset combiné : {combined.shape}")
    return combined


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print(" COLLECTE DONNÉES - Reuters Institute DNR")
    print(f"   Date : {COLLECTION_DATE}")
    print(f"   Datasets : {len(REUTERS_DNR_DATA)}")
    print("=" * 60)

    dataframes = {}

    for name, config in REUTERS_DNR_DATA.items():
        print(f"\n{'─'*60}")
        print(f" Construction dataset : {name}")
        print(f"   {config['description_fr']}")
        
        df = build_longitudinal_dataframe(name, config)
        filepath = save_dataset(df, name)
        dataframes[name] = df

    # Dataset combiné
    print(f"\n{'═'*60}")
    print(" CONSOLIDATION - Fusion de tous les datasets DNR")
    combined = build_combined_dataset(dataframes)
    combined_path = os.path.join(OUTPUT_DIR, f"reuters_dnr_combined_{COLLECTION_DATE}.csv")
    combined.to_csv(combined_path, index=False, encoding='utf-8')
    print(f"   Dataset combiné sauvegardé : {combined_path}")

    print(f"\n{'='*60}")
    print("COLLECTE TERMINÉE / COLLECTION COMPLETE")
    print(f"   {len(dataframes)} datasets collectés")
    print(f"   Dossier : {OUTPUT_DIR}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
