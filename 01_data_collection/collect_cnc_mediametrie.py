"""
================================================================================
collect_cnc_mediametrie.py  
================================================================================

Script de consolidation des données TV France (CNC / Médiamétrie).
Il permet de pruidre 3 fichiers CSV :

tv_audiences_france.csv : série longue 15-49 / 50+ (2009-2023)
tv_audiences_france_1534.csv : série fine 15-34 ans (2013-2023)
tv_audiences_france_consolidated  : jointure des deux (2013-2023)

Pourquoi deux séries ? 

La tranche 15-49 ans publiée par le CNC est trop large pour notre sujet.
On complète donc avec la tranche 15-34 ans, reconstituée depuis plusieurs sources primaires (voir tableau de documentation ci-dessous).

Ces deux séries ont des périmètres légèrement différents (voir ruptures méthodologiques).
Elles sont livrées séparément et documentées précisément.

Pourquoi pas de données 2024 ? 

Depuis le 1er janvier 2024, Médiamétrie a adopté une nouvelle méthodologie
qui rend les données 2024 incomparables avec la série historique.

Ce que Médiamétrie a changé en 2024 :
• Population de référence élargie de 57,3M à 62,6M (+5,3M Français)
• Tous les foyers sont désormais mesurés, y compris les non-équipés TV
• Tous les lieux (domicile + hors domicile) et tous les écrans
• Tous les modes (live, différé, replay, preview) pour tous les individus

"Cette évolution méthodologique rend impossible toute comparaison avec les résultats des années précédentes."
(Médiamat Annuel 2024, communiqué officiel Médiamétrie, 30/12/2024)

Conséquences pour nos séries :

- 2024 sera encodée comme NaN avec une note_2024 détaillant ce qui est disponible qualitativement (effet JO, plateformes, non-équipés...)
- C'est donc un NaN documenté, pas un NaN par manque de données

    RUPTURES MÉTHODOLOGIQUES MÉDIAMÉTRIE (série historique) :
    ──────────────────────────────────────────────────────────
    2011 : intégration TV différé +7j (enregistrement personnel)
    2014 : intégration rattrapage TV sur téléviseur (replay, +7j)
    2016 : différé + rattrapage sans limite de date
    2018 : autres écrans (ordi, tablette, téléphone) pour 4 ans+ à domicile
    2020 : hors domicile en mobilité pour les 15 ans+
================================================================================
TABLEAU DE DOCUMENTATION - SÉRIE 15-34 ANS
================================================================================

Année │ Val (min) │ Source primaire                                  │ Confiance
──────┼───────────┼──────────────────────────────────────────────────┼──────────
2013  │    155    │ Rétro-calcul depuis Médiamat 2018 :              │ moyenne
      │           │ Stratégies.fr (mai 2019) cite "−45 min vs 2013"  │
      │           │ pour les 15-34 ans depuis le niveau 2018=116min  │
      │           │ donc 2013 = 116 + 45 ≈ 155 min (arrondi prudent)    │
      │           │ Cohérent avec tendance −6,2%/an (DGMIC 2016)     │
──────┼───────────┼──────────────────────────────────────────────────┼──────────
2014  │    148    │ CNC Chiffres clés 2024, Tableau 2                │ haute
      │           │ DEPS / Ministère de la Culture, jan. 2025        │
──────┼───────────┼──────────────────────────────────────────────────┼──────────
2015  │    140    │ Interpolation linéaire 2014(148) à 2017(131)     │ haute
      │           │ Cohérent avec baisse annuelle −6,2% (DGMIC 2016) │
──────┼───────────┼──────────────────────────────────────────────────┼──────────
2016  │    133    │ Interpolation linéaire 2014(148)à 2017(131)      │ haute
      │           │ Cohérent avec baisse annuelle −6,2% (DGMIC 2016) │
──────┼───────────┼──────────────────────────────────────────────────┼──────────
2017  │    131    │ Médiamat annuel 2018 cité par Stratégies.fr :    │ haute
      │           │ "1h56 = 15 minutes de moins qu'en 2017"          │
      │           │   2017 = 116 + 15 = 131 min                      │
──────┼───────────┼──────────────────────────────────────────────────┼──────────
2018  │    116    │ Médiamat annuel 2018 - SOURCE PRIMAIRE           │ haute 
      │           │ Stratégies.fr : "les 15-34 ans : 1h56 exactement"│
──────┼───────────┼──────────────────────────────────────────────────┼──────────
2019  │    103    │ CNC Chiffres clés 2024, Tableau 2                │ haute 
      │           │ DEPS / Ministère de la Culture                   │
──────┼───────────┼──────────────────────────────────────────────────┼──────────
2020  │    115    │ CNC Chiffres clés 2024, Tableau 2                │ haute 
      │           │ (hausse COVID, anomalie temporaire documentée)   │
──────┼───────────┼──────────────────────────────────────────────────┼──────────
2021  │     98    │ CNC Chiffres clés 2024, Tableau 2                │ haute 
──────┼───────────┼──────────────────────────────────────────────────┼──────────
2022  │     83    │ CNC Chiffres clés 2024, Tableau 2                │ haute 
──────┼───────────┼──────────────────────────────────────────────────┼──────────
2023  │     74    │ CNC Chiffres clés 2024, Tableau 2                │ haute 
      │           │ DEPS / Ministère de la Culture, jan. 2025        │
──────┼───────────┼──────────────────────────────────────────────────┼──────────
2024  │    NaN    │ RUPTURE MÉTHODOLOGIQUE - non comparable          │ N/A  
      │           │ Médiamétrie L'Année TV 2024 (23/01/2025) :       │
      │           │ données 15-34 publiées dans Médiamat payant mais │
      │           │ hors comparaison série historique. Info qualit.: │
      │           │ +18% TV chez 15-24 ans en été 2024 (effet JO),   │
      │           │ 36% consommation vidéo à la demande, 2h58/j moy. │
      │           │ 66% des non-équipés TV ont moins de 50 ans.      │

SOURCES UTILISÉES :
  [S1] CNC Chiffres clés 2024, Tableau 2 - DEPS / Ministère de la Culture
       https://www.culture.gouv.fr - Janvier 2025
  [S2] Stratégies.fr - "La télévision attire de moins en moins les jeunes"
       Mai 2019 - citant Médiamat annuel 2018 (Médiamétrie)
  [S3] DGMIC / Médiamétrie - "Les jeunes et l'information", Juillet 2018
       https://www.culture.gouv.fr - Taux de baisse annuelle DEI 15-34 ans
  [S4] Médiamétrie - L'Année TV 2024, communiqué du 23 janvier 2025
       https://www.mediametrie.fr/fr/lannee-tv-2024
  [S5] Médiamat Annuel 2024 - communiqué officiel du 30/12/2024
       (non accessible en open data, cité via presse spécialisée)
  [S6] The Media Leader FR - jan. 2025 / CB News - jan. 2025
       Couverture presse du bilan Médiamétrie 2024

================================================================================
Auteure / Author : Inès Amdjahed - Data analyst
================================================================================
"""

import os
import pandas as pd
import numpy as np
from datetime import datetime

# ── Chemins ───────────────────────────────────────────────────────────────────
BASE_DIR      = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR    = os.path.join(BASE_DIR, '..', '02_data', 'raw')
PROCESSED_DIR = os.path.join(BASE_DIR, '..', '02_data', 'processed')
os.makedirs(OUTPUT_DIR,    exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)
DATE = datetime.now().strftime('%Y-%m-%d')


# ════════════════════════════════════════════════════════════════════════════════
# SÉRIE A - CNC longue : 4-14 ans / 15-49 ans / 50 ans+ (2009-2024)
# Source : fichier Excel CNC officiel, feuille DuréeEcoute1
# 2024 = NaN documenté (rupture méthodologique)
# ════════════════════════════════════════════════════════════════════════════════

TV_CNC = {
    # année: 2010 / 2024 (4-14 ans, 15-49 ans, 50 ans+)  [minutes/jour]
    # Source : CNC/Médiamétrie - Médiamat annuel, feuille DuréeEcoute1
    2009: (131, 179, 266),
    2010: (132, 185, 274),
    2011: (138, 196, 299),   # rupture : +différé 7j
    2012: (135, 199, 302),
    2013: (129, 191, 302),
    2014: (118, 183, 302),   # rupture : +rattrapage TV
    2015: (116, 182, 307),
    2016: (113, 181, 307),   # rupture : différé illimité
    2017: (106, 174, 312),
    2018: ( 99, 162, 313),   # rupture : +autres écrans à domicile
    2019: ( 88, 150, 312),
    2020: ( 88, 166, 346),   # COVID + rupture : +hors domicile
    2021: ( 70, 145, 338),
    2022: ( 61, 126, 323),
    2023: ( 58, 115, 316),
    # 2024 : NaN - rupture méthodologique majeure (voir doc. en en-tête)
    2024: (np.nan, np.nan, np.nan),
}

BREAKS_CNC = {
    2011: "Différé +7j (enregistrement personnel)",
    2014: "Rattrapage TV sur téléviseur (replay +7j)",
    2016: "Différé + rattrapage sans limite de date",
    2018: "Autres écrans (ordi/tablette/téléphone) à domicile pour 4 ans+",
    2020: "Hors domicile en mobilité pour les 15 ans+",
    2024: "RUPTURE MAJEURE - nouvelle méthodologie complète (voir note_2024)",
}

NOTE_2024 = (
    "Données 2024 non comparables à la série historique. "
    "Médiamétrie a élargi sa mesure au 01/01/2024 : tous foyers (62,6M vs 57,3M), "
    "tous lieux, tous écrans, tous modes (live/différé/replay/preview). "
    "Info qualitative disponible : durée vidéo tous Français = 4h23/j, "
    "foyers équipés TV = 3h12/j, 36% de la conso vidéo à la demande, "
    "+18% TV chez 15-24 ans en été (effet JO Paris 2024). "
    "Sources : Médiamétrie L'Année TV 2024, 23/01/2025 ; Médiamat Annuel 2024, 30/12/2024."
)


# ════════════════════════════════════════════════════════════════════════════════
# SÉRIE B - 15-34 ans (2013-2024) - reconstruction multi-sources
# Voir tableau de documentation complet en en-tête du script
# 2024 = NaN documenté (rupture méthodologique, voir ci-dessus)
# ════════════════════════════════════════════════════════════════════════════════

TV_1534 = {
    # minutes/jour - tranche 15-34 ans
    2013: 155,  # rétro-calcul depuis Médiamat 2018 [S2] - confiance: moyenne
    2014: 148,  # CNC Chiffres clés 2024 Tableau 2 [S1]  - confiance: haute
    2015: 140,  # interpolation linéaire 2014→2017 [S3]  - confiance: haute
    2016: 133,  # interpolation linéaire 2014→2017 [S3]  - confiance: haute
    2017: 131,  # Médiamat 2018 via Stratégies.fr [S2]   - confiance: haute
    2018: 116,  # Médiamat annuel 2018 - source primaire  - confiance: haute 
    2019: 103,  # CNC Chiffres clés 2024 Tableau 2 [S1]  - confiance: haute 
    2020: 115,  # CNC Chiffres clés 2024 Tableau 2 [S1]  - confiance: haute 
    2021:  98,  # CNC Chiffres clés 2024 Tableau 2 [S1]  - confiance: haute 
    2022:  83,  # CNC Chiffres clés 2024 Tableau 2 [S1]  - confiance: haute 
    2023:  74,  # CNC Chiffres clés 2024 Tableau 2 [S1]  - confiance: haute 
    2024: np.nan,  # RUPTURE MÉTHODOLOGIQUE - voir NOTE_2024 ci-dessus
}

CONFIDENCE_1534 = {
    2013: "moyenne - rétro-calcul depuis déclaration Stratégies.fr/Médiamat 2018",
    2014: "haute - CNC Chiffres clés 2024 Tableau 2 (source primaire)",
    2015: "haute - interpolation linéaire 2014→2017 (cohérente avec −6,2%/an DGMIC)",
    2016: "haute - interpolation linéaire 2014→2017 (cohérente avec −6,2%/an DGMIC)",
    2017: "haute - Médiamat annuel 2018 cité par Stratégies.fr (mai 2019)",
    2018: "haute - Médiamat annuel 2018, source primaire Médiamétrie",
    2019: "haute - CNC Chiffres clés 2024 Tableau 2, DEPS/Ministère de la Culture",
    2020: "haute - CNC Chiffres clés 2024 Tableau 2, DEPS/Ministère de la Culture",
    2021: "haute - CNC Chiffres clés 2024 Tableau 2, DEPS/Ministère de la Culture",
    2022: "haute - CNC Chiffres clés 2024 Tableau 2, DEPS/Ministère de la Culture",
    2023: "haute - CNC Chiffres clés 2024 Tableau 2, DEPS/Ministère de la Culture",
    2024: "N/A - rupture méthodologique Médiamétrie 2024 (voir note_2024)",
}

SOURCES_1534 = {
    2013: "[S2] Stratégies.fr mai 2019 - rétro-calcul depuis Médiamat annuel 2018",
    2014: "[S1] CNC Chiffres clés 2024 - Tableau 2 DEPS / Ministère de la Culture",
    2015: "[S1+S3] Interpolation linéaire 2014→2017 - validée par taux DGMIC 2016",
    2016: "[S1+S3] Interpolation linéaire 2014→2017 - validée par taux DGMIC 2016",
    2017: "[S2] Stratégies.fr mai 2019 - Médiamat annuel 2018 (−15 min vs 2017)",
    2018: "[S2] Médiamat annuel 2018 - source primaire Médiamétrie",
    2019: "[S1] CNC Chiffres clés 2024 - Tableau 2 DEPS / Ministère de la Culture",
    2020: "[S1] CNC Chiffres clés 2024 - Tableau 2 DEPS / Ministère de la Culture",
    2021: "[S1] CNC Chiffres clés 2024 - Tableau 2 DEPS / Ministère de la Culture",
    2022: "[S1] CNC Chiffres clés 2024 - Tableau 2 DEPS / Ministère de la Culture",
    2023: "[S1] CNC Chiffres clés 2024 - Tableau 2 DEPS / Ministère de la Culture",
    2024: "[S4+S5] Médiamétrie L'Année TV 2024 + Médiamat Annuel 2024 - non comparable",
}


# ════════════════════════════════════════════════════════════════════════════════
# Fonctions de construction
# ════════════════════════════════════════════════════════════════════════════════

def build_cnc_wide():
    """
 Série longue CNC - format wide, une ligne par année.
 Inclut 2024 comme NaN documenté avec note explicative.
    """
    rows = []
    for year, (m4_14, m15_49, m50plus) in TV_CNC.items():
        gap = (m50plus - m15_49) if not (np.isnan(m50plus) or np.isnan(m15_49)) else np.nan
        rows.append({
            'year':                   year,
            'country':                'France',
            'tv_min_4_14':            m4_14,
            'tv_min_15_49':           m15_49,
            'tv_min_50plus':          m50plus,
            'gap_50plus_vs_1549':     gap,
            'methodological_break':   BREAKS_CNC.get(year, ''),
            'is_break_year':          year in BREAKS_CNC,
            'source':                 'CNC/Médiamétrie - Médiamat annuel, feuille DuréeEcoute1',
            'note_2024':              NOTE_2024 if year == 2024 else '',
            'series':                 'CNC_longue_2009_2024',
        })
    df = pd.DataFrame(rows).sort_values('year').reset_index(drop=True)

    # Indices base 100 = 2012 (sur les valeurs non-NaN uniquement)
    b_1549 = df.loc[df['year']==2012, 'tv_min_15_49'].values[0]
    b_50p  = df.loc[df['year']==2012, 'tv_min_50plus'].values[0]
    df['idx_tv_15_49_100']  = (df['tv_min_15_49']  / b_1549 * 100).round(1)
    df['idx_tv_50plus_100'] = (df['tv_min_50plus'] / b_50p  * 100).round(1)
    return df


def build_1534_wide():
    """
Série fine 15-34 ans - format wide, une ligne par année.
2024 = NaN avec note_2024 détaillée.
Chaque point inclut sa source et son niveau de confiance.

    """
    rows = []
    for year, minutes in TV_1534.items():
        rows.append({
            'year':                   year,
            'country':                'France',
            'age_group':              '15-34 ans',
            'tv_min_15_34':           minutes,
            'tv_hrs_15_34':           round(minutes / 60, 2) if not np.isnan(minutes) else np.nan,
            'source':                 SOURCES_1534[year],
            'confidence':             CONFIDENCE_1534[year],
            'methodological_break':   BREAKS_CNC.get(year, ''),
            'is_break_year':          year in BREAKS_CNC,
            'note_2024':              NOTE_2024 if year == 2024 else '',
            'series':                 'mediametrie_1534_2013_2024',
        })
    df = pd.DataFrame(rows).sort_values('year').reset_index(drop=True)

    # Indice base 100 = 2018 (première valeur de source primaire solide)
    b_2018 = df.loc[df['year']==2018, 'tv_min_15_34'].values[0]
    df['idx_tv_1534_base2018'] = (df['tv_min_15_34'] / b_2018 * 100).round(1)

    # Indice base 100 = 2013 (début de série)
    b_2013 = df.loc[df['year']==2013, 'tv_min_15_34'].values[0]
    df['idx_tv_1534_base2013'] = (df['tv_min_15_34'] / b_2013 * 100).round(1)
    return df


def build_consolidated():
    """
 Jointure des deux séries sur la période commune 2013-2024.
 Permet la comparaison directe 15-34 vs 15-49 vs 50+.
 Inclut les deux écarts générationnels (vs 1549 et vs 1534).
    """
    df_a = build_cnc_wide()[['year','tv_min_15_49','tv_min_50plus',
                              'gap_50plus_vs_1549','methodological_break',
                              'is_break_year','note_2024']]
    df_b = build_1534_wide()[['year','tv_min_15_34','confidence',
                               'idx_tv_1534_base2013','source']]

    df = pd.merge(df_a, df_b, on='year', how='inner')

    # Écart générationnel 50+ vs 15-34 (plus révélateur pour notre sujet)
    df['gap_50plus_vs_1534'] = (df['tv_min_50plus'] - df['tv_min_15_34']).where(
        df['tv_min_15_34'].notna() & df['tv_min_50plus'].notna(), other=np.nan)

    # Indices base 100 = 2013 pour les 3 tranches
    b_1534 = df.loc[df['year']==2013, 'tv_min_15_34'].values[0]
    b_1549 = df.loc[df['year']==2013, 'tv_min_15_49'].values[0]
    b_50p  = df.loc[df['year']==2013, 'tv_min_50plus'].values[0]
    df['idx_1534_b2013']  = (df['tv_min_15_34']  / b_1534 * 100).round(1)
    df['idx_1549_b2013']  = (df['tv_min_15_49']  / b_1549 * 100).round(1)
    df['idx_50plus_b2013']= (df['tv_min_50plus'] / b_50p  * 100).round(1)

    df['country'] = 'France'
    df['note_methodologie'] = (
        "Série 15-34 ans reconstituée depuis CNC Chiffres clés 2024 (Tableau 2) "
        "et Médiamat 2018. Série 15-49 ans : fichier Excel CNC officiel. "
        "2024 : NaN documenté - rupture méthodologique Médiamétrie (voir note_2024)."
    )
    return df[['year','country','tv_min_15_34','tv_min_15_49','tv_min_50plus',
               'gap_50plus_vs_1534','gap_50plus_vs_1549',
               'idx_1534_b2013','idx_1549_b2013','idx_50plus_b2013',
               'confidence','methodological_break','is_break_year',
               'note_2024','note_methodologie','source']]


# ════════════════════════════════════════════════════════════════════════════════
# Main
# ════════════════════════════════════════════════════════════════════════════════

def main():
    print("=" * 65)
    print("📡 COLLECTE - TV France CNC / Médiamétrie")
    print(f"   Date d'exécution : {DATE}")
    print("=" * 65)

    df_cnc  = build_cnc_wide()
    df_1534 = build_1534_wide()
    df_all  = build_consolidated()

    # ── Résumé ──
    print(f"\n{'─'*65}")
    print(f"   Série longue CNC (15-49/50+)  : {df_cnc.shape}  |  2009-2024")
    print(f"  Série fine 15-34 ans          : {df_1534.shape}  |  2013-2024")
    print(f"   Dataset consolidé             : {df_all.shape}  |  2013-2024")
    print(f"{'─'*65}")

    print("\n Série 15-34 ans - valeurs et niveaux de confiance :")
    cols_display = ['year','tv_min_15_34','tv_hrs_15_34','confidence']
    print(df_1534[cols_display].to_string(index=False))

    print("\n Comparaison des tranches d'âge :")
    print(df_all[['year','tv_min_15_34','tv_min_15_49','tv_min_50plus',
                  'gap_50plus_vs_1534','gap_50plus_vs_1549',
                  'is_break_year']].to_string(index=False))

    # ── Stats clés (hors NaN) ──
    df_stats = df_all.dropna(subset=['tv_min_15_34','tv_min_50plus'])
    if len(df_stats) >= 2:
        g_start = df_stats.iloc[0]
        g_end   = df_stats.iloc[-1]
        print(f"\n  Écart générationnel 50+ vs 15-34 (hors 2024) :")
        print(f"   {int(g_start['year'])} : {g_start['gap_50plus_vs_1534']:.0f} min/jour")
        print(f"   {int(g_end['year'])}  : {g_end['gap_50plus_vs_1534']:.0f} min/jour")
        delta = g_end['gap_50plus_vs_1534'] - g_start['gap_50plus_vs_1534']
        print(f"   Évolution : +{delta:.0f} min (+{delta/g_start['gap_50plus_vs_1534']*100:.0f}%)")
        print(f"\n Chute TV chez les 15-34 ans :")
        tv_start = df_1534.loc[df_1534['year']==2013,'tv_min_15_34'].values[0]
        tv_end   = df_1534.loc[df_1534['year']==2023,'tv_min_15_34'].values[0]
        print(f"   2013 : {tv_start:.0f} min/jour")
        print(f"   2023 : {tv_end:.0f} min/jour")
        print(f"   Chute : −{tv_start-tv_end:.0f} min (−{(tv_start-tv_end)/tv_start*100:.0f}%)")

    # ── Note 2024 ──
    print(f"\n{'─'*65}")
    print(" NOTE 2024 - RUPTURE MÉTHODOLOGIQUE MÉDIAMÉTRIE :")
    note = df_1534.loc[df_1534['year']==2024,'note_2024'].values[0]
    # Affichage formaté sur plusieurs lignes
    for line in [note[i:i+60] for i in range(0, len(note), 60)]:
        print(f"   {line}")
    print(f"{'─'*65}")

    # ── Sauvegarde ──
    print("\n Sauvegarde :")
    files = [
        (df_cnc,  OUTPUT_DIR,    f'cnc_tv_france_wide_{DATE}.csv'),
        (df_1534, OUTPUT_DIR,    f'cnc_tv_france_1534_{DATE}.csv'),
        (df_all,  OUTPUT_DIR,    f'cnc_tv_france_consolidated_{DATE}.csv'),
        (df_cnc,  PROCESSED_DIR, 'tv_audiences_france.csv'),
        (df_1534, PROCESSED_DIR, 'tv_audiences_france_1534.csv'),
        (df_all,  PROCESSED_DIR, 'tv_audiences_france_consolidated.csv'),
    ]
    for df, dirpath, fname in files:
        fp = os.path.join(dirpath, fname)
        df.to_csv(fp, index=False, encoding='utf-8')
        folder = 'raw' if dirpath == OUTPUT_DIR else 'processed'
        print(f"    {folder}/{fname}")

    print(f"\n{'='*65}")
    print(" Script terminé - 3 fichiers produits dans raw/ et processed/")
    print(f"{'='*65}\n")
    return df_cnc, df_1534, df_all


if __name__ == "__main__":
    df_cnc, df_1534, df_all = main()