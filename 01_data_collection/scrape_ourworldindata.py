"""
================================================================================
scrape_ourworldindata.py
================================================================================

FR :
    Script de collecte de données multi-sources pour le projet :
    "Réseaux Sociaux vs Médias Traditionnels"

    STRATÉGIE DE COLLECTE :
    ─────────────────────────────────────────────────────────────
    Our World in Data (OWID) expose certains datasets via des URLs CSV stables.
    Cependant, tous les graphiques ne sont pas disponibles en CSV direct —
    certains slugs ont changé ou les données n'existent pas sous ce format.

    On adopte donc une stratégie HYBRIDE en 2 parties :

    PARTIE 1 — Téléchargement automatique via API OWID (URLs CSV validées)
      → Utilisateurs d'internet par pays (Banque Mondiale / ITU)
      → Utilisateurs de réseaux sociaux par plateforme (Facebook, Instagram...)
      → Temps passé sur les médias numériques aux USA (eMarketer)

    PARTIE 2 — Reconstruction manuelle depuis sources publiées
      → Temps passé sur les réseaux sociaux par pays 2012-2024
        (Source : GWI via DataReportal / Statista — données publiées annuellement)
      → Ces chiffres proviennent de rapports académiques et professionnels
        largement cités dans la littérature scientifique sur les médias numériques.

    PRINCIPE DE REPRODUCTIBILITÉ :
    Toutes les données sont sauvegardées dans leur état brut (raw/)
    avec un horodatage, avant tout traitement. Cela garantit que
    l'analyse peut être reproduite exactement à l'identique.

EN :
    Multi-source data collection script.
    Hybrid strategy: OWID API download + manual reconstruction from GWI/Statista.
    All raw data is timestamped and saved before any processing.

================================================================================
Auteure / Author : Inès Amdjahed — Master 2 Info-Com, Paris Nanterre
Sources          : Our World in Data (CC BY 4.0), GWI, DataReportal, Statista
================================================================================
"""

# ── Imports ────────────────────────────────────────────────────────────────────
# os       : gestion des chemins de fichiers (compatible Linux/Mac/Windows)
# requests : librairie HTTP pour télécharger les CSV depuis les URLs
# pandas   : manipulation des données sous forme de DataFrame
# datetime : pour horodater la collecte (traçabilité)
# StringIO : permet de lire une réponse HTTP texte comme un fichier CSV

import os
import requests
import pandas as pd
from datetime import datetime
from io import StringIO

# ── Configuration ──────────────────────────────────────────────────────────────

# __file__ = chemin absolu du script actuel
# os.path.dirname(__file__) = dossier contenant ce script (01_data_collection/)
# '..' = remonter d'un niveau = racine du projet
# os.path.join = assemblage propre du chemin (évite les erreurs de slash)
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', '02_data', 'raw')

# Création automatique du dossier de sortie (exist_ok=True = pas d'erreur si déjà existant)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Format ISO 8601 : '2026-03-11' — utilisé pour nommer les fichiers
# Permet de savoir exactement quand les données ont été collectées
COLLECTION_DATE = datetime.now().strftime('%Y-%m-%d')


# ════════════════════════════════════════════════════════════════════════════════
# PARTIE 1 — DATASETS OWID TÉLÉCHARGEABLES EN CSV DIRECT
# ════════════════════════════════════════════════════════════════════════════════
#
# FR :
#   Ces URLs ont été VALIDÉES manuellement sur ourworldindata.org.
#   Format API OWID : https://ourworldindata.org/grapher/[slug].csv
#                    ?v=1                    → version de l'API
#                    &csvType=full           → toutes les données (pas seulement la vue)
#                    &useColumnShortNames=true → noms de colonnes courts pour le code
#
# EN :
#   These URLs were MANUALLY VALIDATED on ourworldindata.org.
#   Note: Not all OWID charts expose a CSV API — only some slugs work.

OWID_DATASETS = {

    # ── Dataset 1 : Utilisateurs d'internet par pays ────────────────────────
    # Source originale : Banque Mondiale / ITU (Union Internationale des Télécoms)
    # Variable : % de la population utilisant internet
    # Couverture : ~200 pays, 1990–2023
    # Pertinence : variable de CONTEXTE — mesure la pénétration numérique
    #              nécessaire pour comprendre l'exposition possible aux réseaux sociaux
    "internet_users_by_country": {
        "url": "https://ourworldindata.org/grapher/share-of-individuals-using-the-internet.csv"
               "?v=1&csvType=full&useColumnShortNames=true",
        "description_fr": "% de la population utilisant internet par pays (1990-2023)",
        "description_en": "Share of population using internet by country (1990-2023)",
        "source":         "Banque Mondiale / ITU via Our World in Data",
        "hypothese":      "Variable de contexte — pénétration numérique",
    },

    # ── Dataset 2 : Nombre d'utilisateurs d'internet (absolu) ──────────────
    # Source originale : Banque Mondiale / ITU
    # Variable : nombre total d'internautes en millions par pays
    # Couverture : ~200 pays, 1990-2023
    # Pertinence pour H3 : mesure la croissance de l'audience numérique
    #                      potentielle pays par pays dans le temps
    # Note : à croiser avec le dataset % pour calculer des indices relatifs
    "internet_users_absolute": {
        "url": "https://ourworldindata.org/grapher/number-of-internet-users.csv"
               "?v=1&csvType=full&useColumnShortNames=true",
        "description_fr": "Nombre absolu d'internautes par pays (millions, 1990-2023)",
        "description_en": "Absolute number of internet users by country (millions, 1990-2023)",
        "source":         "Banque Mondiale / ITU via Our World in Data",
        "hypothese":      "H3 — volume d'audience numérique dans le temps",
    },

    # ── Dataset 3 : Temps passé sur les médias numériques (USA) ────────────
    # Source originale : eMarketer (cabinet d'analyse media américain)
    # Variable : heures/jour passées sur mobile, desktop, autres appareils connectés
    # Couverture : États-Unis, 2008–2023
    # Pertinence pour H1 : mesure directe du TEMPS ÉCRAN NUMÉRIQUE total
    #                      → permet de visualiser la substitution médias trad → numérique
    "digital_media_time_usa": {
        "url": "https://ourworldindata.org/grapher/daily-hours-spent-with-digital-media-per-adult-user.csv"
               "?v=1&csvType=full&useColumnShortNames=true",
        "description_fr": "Heures/jour passées sur les médias numériques par adulte (USA, 2008-2023)",
        "description_en": "Daily hours spent on digital media per adult user (USA, 2008-2023)",
        "source":         "eMarketer via Our World in Data",
        "hypothese":      "H1 — substitution médias traditionnels → numériques",
    },
}


# ════════════════════════════════════════════════════════════════════════════════
# PARTIE 2 — DONNÉES GWI RECONSTRUITES MANUELLEMENT
# ════════════════════════════════════════════════════════════════════════════════
#
# FR :
#   Global Web Index (GWI) est le panel de référence mondiale pour mesurer
#   le comportement des internautes. Leurs données sont publiées annuellement
#   dans les rapports "Digital" de DataReportal (We Are Social / Hootsuite).
#
#   Ces chiffres sont LARGEMENT CITÉS dans la littérature académique sur les médias
#   numériques (ex: Reuters Institute DNR, Pew Research, études OCDE).
#
#   Données ici : temps quotidien moyen passé sur les réseaux sociaux (minutes/jour)
#   Population : internautes de 16 à 64 ans, 53 pays représentatifs
#   Source : GWI via DataReportal / Statista — rapports 2012-2024 publiés
#
# EN :
#   GWI (Global Web Index) is the world reference panel for internet behavior.
#   Data published yearly in DataReportal's "Digital" reports.
#   Metric: average daily minutes spent on social media, internet users 16-64.

# Données mondiales (moyenne tous pays confondus)
# Source : We Are Social / DataReportal / GWI, rapports annuels 2013-2025
GWI_SOCIAL_MEDIA_GLOBAL = {
    2012: 90,   # ~1h30 — réseaux sociaux encore majoritairement sur desktop
    2013: 100,  # ~1h40 — explosion mobile, Facebook dominant
    2014: 111,  # ~1h51 — Instagram en forte croissance
    2015: 116,  # ~1h56 — Snapchat émerge chez les jeunes
    2016: 122,  # ~2h02 — début du contenu vidéo viral (Facebook Live)
    2017: 135,  # ~2h15 — Stories Instagram lancées, TikTok lancé en Chine
    2018: 142,  # ~2h22 — TikTok international, YouTube mobile dominant
    2019: 144,  # ~2h24 — plateau relatif avant explosion COVID
    2020: 145,  # ~2h25 — légère hausse COVID (confinements mondiaux)
    2021: 147,  # ~2h27 — TikTok explose, reels Instagram lancés
    2022: 147,  # ~2h27 — stabilisation, fatigue des écrans post-COVID
    2023: 143,  # ~2h23 — légère baisse, fragmentation des usages
    2024: 143,  # ~2h23 — stabilisation (source: DataReportal Feb 2025)
}

# Données par pays sélectionnés (minutes/jour, 2024)
# Source : GWI Q3 2024 via DataReportal
GWI_SOCIAL_MEDIA_BY_COUNTRY_2024 = {
    "Brazil":        229,  # 🇧🇷 3h49 — usage le plus élevé monde occidental
    "Philippines":   214,  # 🇵🇭 3h34 — anciennement n°1 mondial
    "South Africa":  221,  # 🇿🇦 3h41
    "Kenya":         223,  # 🇰🇪 3h43 — le plus élevé du panel 2024
    "India":         182,  # 🇮🇳 3h02
    "Mexico":        185,  # 🇲🇽 3h05
    "United States": 129,  # 🇺🇸 2h09
    "France":        105,  # 🇫🇷 1h45 — contexte de notre étude CNC
    "United Kingdom": 97,  # 🇬🇧 1h37
    "Germany":        85,  # 🇩🇪 1h25
    "Australia":     111,  # 🇦🇺 1h51
    "Japan":          46,  # 🇯🇵 0h46 — usage le plus faible du panel
    "South Korea":    66,  # 🇰🇷 1h06
}


# ── Données plateformes sociales — MAU historique ─────────────────────────────
#
# FR :
#   MAU = Monthly Active Users (utilisateurs actifs mensuels)
#   C'est la métrique de référence pour mesurer la taille d'une plateforme.
#   Ces chiffres proviennent des rapports trimestriels officiels des plateformes
#   (earnings reports, investor relations) et sont largement cités dans
#   la littérature académique sur les médias numériques.
#
#   Source : rapports officiels Meta, ByteDance, Snap, X Corp
#            compilés via DataReportal / Statista / Hootsuite
#   Unité : millions d'utilisateurs actifs mensuels (MAU)
#
# EN :
#   Monthly Active Users (MAU) — the standard platform size metric.
#   From official quarterly earnings reports (Meta, ByteDance, Snap, X Corp).
#   Unit: millions of monthly active users.

PLATFORM_MAU_HISTORICAL = {
    # Facebook — dominant depuis 2008, ralentit chez les jeunes après 2018
    "Facebook": {
        2008: 100, 2009: 350, 2010: 608, 2011: 845, 2012: 1056,
        2013: 1230, 2014: 1393, 2015: 1591, 2016: 1860, 2017: 2129,
        2018: 2320, 2019: 2498, 2020: 2797, 2021: 2912, 2022: 2963,
        2023: 3049, 2024: 3070,
    },
    # Instagram — lancé 2010, croissance forte 2013-2019
    "Instagram": {
        2012: 30, 2013: 90, 2014: 200, 2015: 400, 2016: 600,
        2017: 800, 2018: 1000, 2019: 1082, 2020: 1221, 2021: 1393,
        2022: 1628, 2023: 1740, 2024: 1910,
    },
    # TikTok — lancé international 2018, explosion 2019-2021
    "TikTok": {
        2018: 271, 2019: 508, 2020: 689, 2021: 1000,
        2022: 1400, 2023: 1562, 2024: 1990,
    },
    # YouTube — plateforme de référence pour la vidéo longue
    "YouTube": {
        2012: 800, 2013: 1000, 2014: 1000, 2015: 1500, 2016: 1500,
        2017: 1500, 2018: 1900, 2019: 2000, 2020: 2291, 2021: 2562,
        2022: 2700, 2023: 2700, 2024: 2580,
    },
    # Snapchat — populaire chez les 13-24 ans
    "Snapchat": {
        2014: 100, 2015: 200, 2016: 301, 2017: 187, 2018: 190,
        2019: 218, 2020: 265, 2021: 319, 2022: 375, 2023: 397, 2024: 443,
    },
    # X (ex-Twitter)
    "X (Twitter)": {
        2012: 185, 2013: 241, 2014: 288, 2015: 320, 2016: 319,
        2017: 330, 2018: 336, 2019: 339, 2020: 353, 2021: 436,
        2022: 450, 2023: 541, 2024: 557,
    },
}


# ── Fonctions ──────────────────────────────────────────────────────────────────

def download_owid_dataset(name: str, config: dict) -> pd.DataFrame | None:
    """
    FR :
        Télécharge un dataset OWID depuis son URL CSV directe.
        Retourne un DataFrame pandas, ou None si le téléchargement échoue.

        Gestion des erreurs HTTP :
          - 404 : le slug OWID n'existe pas / a changé → vérifier sur le site
          - 429 : rate limiting → trop de requêtes, attendre et réessayer
          - 5xx : erreur côté serveur OWID → réessayer plus tard
          - ConnectionError : pas de connexion internet

    EN :
        Downloads an OWID dataset from its CSV URL.
        Returns a pandas DataFrame or None on failure.
    """
    print(f"\n{'─'*60}")
    print(f"📥 Téléchargement / Downloading : {name}")
    print(f"   FR : {config['description_fr']}")
    print(f"   EN : {config['description_en']}")
    print(f"   Source : {config['source']}")

    try:
        # User-Agent poli qui identifie le script comme un projet académique
        # Bonne pratique : évite d'être bloqué par les protections anti-bot
        headers = {
            'User-Agent': 'Mozilla/5.0 (academic research - Paris Nanterre - media consumption study)'
        }

        # timeout=30 : abandonne si le serveur ne répond pas en 30 secondes
        # raise_for_status() : lève une exception si code HTTP >= 400 (erreur)
        response = requests.get(config['url'], headers=headers, timeout=30)
        response.raise_for_status()

        # StringIO transforme le texte CSV reçu en "faux fichier"
        # que pandas peut lire directement sans écrire sur le disque
        df = pd.read_csv(StringIO(response.text))

        # ── Détection automatique des colonnes clés ──
        # OWID utilise parfois 'Year', parfois 'year' selon les datasets
        year_col   = 'Year'   if 'Year'   in df.columns else 'year'   if 'year'   in df.columns else None
        entity_col = 'Entity' if 'Entity' in df.columns else 'entity' if 'entity' in df.columns else None

        print(f"   ✅ Succès — {df.shape[0]} lignes × {df.shape[1]} colonnes")
        print(f"   📋 Colonnes : {list(df.columns)}")
        if year_col:
            print(f"   📅 Années   : {df[year_col].min()} → {df[year_col].max()}")
        if entity_col:
            print(f"   🌍 Entités  : {df[entity_col].nunique()} pays/régions")

        # Audit des valeurs manquantes (NaN = donnée non disponible pour ce pays/année)
        missing     = df.isnull().sum().sum()
        pct_missing = missing / (df.shape[0] * df.shape[1]) * 100
        print(f"   ⚠️  Valeurs manquantes : {missing} ({pct_missing:.1f}%)")

        return df

    except requests.exceptions.HTTPError as e:
        print(f"   ❌ Erreur HTTP : {e}")
        print(f"   → Le slug OWID a peut-être changé. Vérifier sur ourworldindata.org")
        return None
    except requests.exceptions.ConnectionError:
        print(f"   ❌ Pas de connexion internet")
        return None
    except requests.exceptions.Timeout:
        print(f"   ❌ Timeout — serveur OWID ne répond pas")
        return None
    except Exception as e:
        print(f"   ❌ Erreur inattendue : {type(e).__name__} — {e}")
        return None


def build_gwi_datasets() -> dict:
    """
    FR :
        Construit les datasets GWI à partir des données reconstruites manuellement.

        FORMAT LONG (tidy data) :
        On transforme les dictionnaires Python en DataFrames au format "long" :
        une ligne = une observation (année, pays, valeur).
        C'est le format standard pour les analyses en panel et les
        visualisations avec seaborn/matplotlib.

        Exemple de format long :
          year | country       | social_media_minutes | source
          2012 | World average | 90                   | GWI via DataReportal
          2013 | World average | 100                  | GWI via DataReportal
          ...

    EN :
        Builds GWI datasets from manually reconstructed data.
        Long format (tidy data): one observation per row.
        Standard format for panel data analysis and visualization.
    """

    # ── Dataset GWI 1 : Tendance mondiale 2012-2024 ──
    # On transforme le dictionnaire {année: minutes} en DataFrame long
    rows_global = []
    for year, minutes in GWI_SOCIAL_MEDIA_GLOBAL.items():
        rows_global.append({
            'year':                   year,
            'entity':                 'World average',     # entité = "monde"
            'social_media_minutes':   minutes,             # variable principale
            'social_media_hours':     round(minutes / 60, 2),  # version heures pour comparaison
            'source':                 'GWI via DataReportal / We Are Social',
            'population':             'Internet users 16-64',
            'note':                   'Global average across 53 countries surveyed by GWI',
        })
    df_global = pd.DataFrame(rows_global)

    # ── Dataset GWI 2 : Comparaison internationale 2024 ──
    # On transforme le dictionnaire {pays: minutes} en DataFrame
    rows_countries = []
    for country, minutes in GWI_SOCIAL_MEDIA_BY_COUNTRY_2024.items():
        rows_countries.append({
            'year':                   2024,
            'entity':                 country,
            'social_media_minutes':   minutes,
            'social_media_hours':     round(minutes / 60, 2),
            'source':                 'GWI Q3 2024 via DataReportal',
            'population':             'Internet users 16-64',
        })
    df_countries = pd.DataFrame(rows_countries)
    # Tri par temps décroissant pour lecture rapide (pays le plus actif en premier)
    df_countries = df_countries.sort_values('social_media_minutes', ascending=False)

    # ── Dataset 3 : Utilisateurs par plateforme (MAU historique) ──
    # On transforme le dictionnaire imbriqué {plateforme: {année: MAU}}
    # en DataFrame long avec une ligne par (plateforme × année)
    # C'est le format idéal pour les graphiques multi-séries (une ligne par plateforme)
    rows_platforms = []
    for platform, yearly_data in PLATFORM_MAU_HISTORICAL.items():
        for year, mau_millions in yearly_data.items():
            rows_platforms.append({
                'year':         year,
                'platform':     platform,
                'mau_millions': mau_millions,   # Monthly Active Users en millions
                'source':       'Earnings reports officiels (Meta, ByteDance, Snap, X Corp) via DataReportal',
                'note':         'MAU = Monthly Active Users — métrique officielle déclarée par les plateformes',
            })
    df_platforms = pd.DataFrame(rows_platforms)
    # Tri chronologique puis par plateforme pour une lecture ordonnée
    df_platforms = df_platforms.sort_values(['platform', 'year']).reset_index(drop=True)

    print(f"\n✅ GWI Dataset 1 (tendance mondiale) : {df_global.shape}")
    print(f"✅ GWI Dataset 2 (comparaison pays 2024) : {df_countries.shape}")
    print(f"✅ Dataset 3 (MAU plateformes historique) : {df_platforms.shape}")

    return {
        'gwi_social_media_global_trend':      df_global,
        'gwi_social_media_by_country_2024':   df_countries,
        'platforms_mau_historical':           df_platforms,
    }


def save_dataset(df: pd.DataFrame, name: str, prefix: str = '') -> str:
    """
    FR :
        Sauvegarde un DataFrame en CSV dans le dossier 02_data/raw/.

        Convention de nommage : {prefix}_{name}_{date}.csv
        Exemple : owid_internet_users_by_country_2026-03-11.csv
                  gwi_social_media_global_trend_2026-03-11.csv

        RÈGLE FONDAMENTALE : les fichiers raw/ ne sont JAMAIS modifiés.
        Toutes les transformations se font dans les notebooks de cleaning.
        C'est un principe essentiel de reproductibilité scientifique.

    EN :
        Saves a DataFrame as CSV in 02_data/raw/.
        Raw files must NEVER be manually modified — transformations go in notebooks.
    """
    # Construction du nom de fichier avec horodatage
    filename = f"{prefix}_{name}_{COLLECTION_DATE}.csv" if prefix else f"{name}_{COLLECTION_DATE}.csv"
    filepath = os.path.join(OUTPUT_DIR, filename)

    # index=False  : on n'écrit pas l'index pandas (numéros de ligne) dans le CSV
    # encoding utf-8 : standard universel, gère les accents et caractères spéciaux
    df.to_csv(filepath, index=False, encoding='utf-8')
    print(f"   💾 Sauvegardé : {filepath}")
    return filepath


def inspect_dataset(df: pd.DataFrame, name: str):
    """
    FR :
        Inspection préliminaire = première phase de l'EDA (data profiling).

        On vérifie systématiquement :
          1. Les 5 premières lignes — pour voir la structure réelle des données
          2. Les types de données (dtypes) — pour détecter les erreurs de typage
             (ex: une année stockée comme string au lieu d'int)
          3. Les statistiques descriptives — pour repérer les valeurs aberrantes
             (ex: un pays avec 0 utilisateurs internet alors que ce n'est pas possible)

    EN :
        Preliminary inspection = first phase of EDA (data profiling).
        Checks: first rows, data types, descriptive statistics.
    """
    print(f"\n{'═'*60}")
    print(f"🔍 INSPECTION — {name}")
    print(f"{'═'*60}")
    print("\n📊 Aperçu (5 premières lignes) :")
    print(df.head().to_string())
    print("\n📐 Types de données (dtypes) :")
    print(df.dtypes.to_string())
    # select_dtypes('number') = seulement les colonnes numériques pour les stats
    numeric = df.select_dtypes(include='number')
    if not numeric.empty:
        print("\n📈 Statistiques descriptives :")
        print(numeric.describe().round(2).to_string())


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    """
    FR :
        Point d'entrée principal du script.

        Orchestre la collecte complète en 4 étapes :
          1. Téléchargement des datasets OWID disponibles en CSV
          2. Construction des datasets GWI depuis les données reconstruites
          3. Sauvegarde de tous les fichiers bruts dans 02_data/raw/
          4. Génération du log de collecte (traçabilité / data lineage)

    EN :
        Main entry point. Orchestrates: OWID download → GWI build → save → log.
    """
    print("=" * 60)
    print("📡 MODULE 1 — COLLECTE DES DONNÉES / DATA COLLECTION")
    print("   Projet : Social Media vs Traditional Media")
    print(f"   Date : {COLLECTION_DATE}")
    print("=" * 60)

    results   = {}   # stocke les résultats pour le rapport final
    log_lines = [    # lignes du fichier de log
        f"# Log de collecte — {COLLECTION_DATE}\n",
        f"# Projet : Social Media vs Traditional Media\n",
        f"# Auteure : Inès Amdjahed\n\n",
    ]

    # ── PARTIE 1 : Téléchargement OWID ──
    print("\n" + "─"*60)
    print("PARTIE 1 / PART 1 — Our World in Data (OWID API)")
    print("─"*60)

    for name, config in OWID_DATASETS.items():
        df = download_owid_dataset(name, config)
        if df is not None:
            fp = save_dataset(df, name, prefix='owid')
            inspect_dataset(df, name)
            results[name] = {'status': 'success', 'shape': df.shape}
            log_lines.append(f"✅ owid/{name} | shape={df.shape} | file={fp}\n")
        else:
            results[name] = {'status': 'failed'}
            log_lines.append(f"❌ owid/{name} | FAILED\n")

    # ── PARTIE 2 : Construction GWI ──
    print("\n" + "─"*60)
    print("PARTIE 2 / PART 2 — GWI / DataReportal (données reconstruites)")
    print("─"*60)

    gwi_datasets = build_gwi_datasets()
    for name, df in gwi_datasets.items():
        fp = save_dataset(df, name, prefix='gwi')
        inspect_dataset(df, name)
        results[name] = {'status': 'success', 'shape': df.shape}
        log_lines.append(f"✅ gwi/{name} | shape={df.shape} | file={fp}\n")

    # ── Rapport final ──
    print(f"\n{'='*60}")
    print("📋 RAPPORT DE COLLECTE / COLLECTION REPORT")
    print(f"{'='*60}")
    nb_success = sum(1 for r in results.values() if r['status'] == 'success')
    print(f"\n   Résultat : {nb_success}/{len(results)} datasets collectés ✅\n")
    for name, r in results.items():
        icon  = "✅" if r['status'] == 'success' else "❌"
        shape = r.get('shape', 'FAILED')
        print(f"   {icon} {name:<45} {shape}")

    # ── Sauvegarde du log ──
    # Le log = documentation de la provenance des données (data lineage)
    # Permet de savoir exactement quelles données ont été collectées, quand, depuis où
    log_path = os.path.join(OUTPUT_DIR, f"collection_log_{COLLECTION_DATE}.txt")
    with open(log_path, 'w', encoding='utf-8') as f:
        f.writelines(log_lines)

    print(f"\n   📝 Log de collecte : {log_path}")
    print(f"\n{'='*60}")
    print("   ➡️  Prochaine étape : 03_notebooks/01_cleaning_wrangling.ipynb")
    print(f"{'='*60}\n")


# Ce bloc garantit que main() s'exécute SEULEMENT quand on lance ce fichier
# directement (python scrape_ourworldindata.py), et PAS quand on l'importe
# depuis un autre fichier Python (import scrape_ourworldindata)
if __name__ == "__main__":
    main()