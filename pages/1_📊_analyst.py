import streamlit as st
from annotated_text import annotated_text

annotated_text(
    "This ",
    ("is", "verb"),
    " some ",
    ("annotated", "adj"),
    ("text", "noun"),
    " for those of ",
    ("you", "pronoun"),
    " who ",
    ("like", "verb"),
    " this sort of ",
    ("thing", "noun"),
    "."
)
st.set_page_config(page_title="Analyste", page_icon="📊", layout="wide")
st.header("Analyste")
 

"""
# Toutes industries
#### 🧾 Exraction des informations contenues dans des factures en PDF, analyse des ventes et prédiction des ventes
1. Stockage de factures au format PDF dans un stage interne de Snowflake
2. Extraction des informations contenues dans chaque facture (adresse, nom du client, montant de chaque ligne)
3. Aggrégation des ventes par jour et par adresse
4. Acquisition du dataset COVID-19 offert par StarSchema sur la marketplace de Snowflake
5. Création d'une carte qui joint les ventes par état avec le nombre de cas COVID-19 confirmés par état
6. Création d'un modèle qui prédit les ventes par jour dans les 90 prochains jours sur base des ventes passées.
- [Video 16 min](https://drive.google.com/file/d/15o881bYeTa4Sgdk89QFRgBlVllcUKYqY/view?usp=share_link)
- [Github](https://github.com/sfc-gh-pneedleman/snowflake_lakehouse)
"""
"""
### 📊 Snowsight
1. Découvrez la nouvelle interface Web de Snowflake : Snowsight
2. Accéder aux données sur Snowflake en SQL
3. Créer des graphes et des tableaux de bord sur base de requêtes SQL
4. Administrer la plateforme Snowflake et auditer les accès aux données
5. Monitorer l'utilisation de la plateforme 
- [Video 20 min](https://drive.google.com/file/d/167jj-D5iGkB3C17d0AbARIHSfPQYbGVU/view?usp=share_link) [Video 3 min](https://drive.google.com/drive/folders/1VJzhPg5rrDCpwirH2SQta_JzeZudvX4y)
"""
"""
### 💵 Calcul du délai moyen de recouvrement, et des impayés sur base de données SAP
1. Extraire des données de systèmes SAP et les insérer sur Snowflake
2. Accéder aux données sur Snowflake en SQL
3. Modéliser les transformations nécessaires avec DBT : calculer le délai moyen de recouvrement 
4. Visualiser les résultats avec Tableau
- [Video 23 min](https://drive.google.com/file/d/16qtPbJqYT4Rq7m7dWyiH-L1bcXkrtk6t/view?usp=share_link)
- [Github](https://github.com/snowflakecorp/sfquickstarts-sap-dbt/blob/main/site/sfguides/src/kickstart_sap_to_snowflake/kickstart_sap_to_snowflake.md)
- [Quickstart SAP](https://snowflakecorp.github.io/sfquickstarts-sap-dbt/#0)
"""
"""
### ⛅️ Analyser l'impact de facteurs externes(climat et COVID-19) sur les ventes et prédire quels clients vont se désabonner.
1. Créer un tableau de bord dans l'interface Snowsight
2. Acquérir des données sur la marketplace de Snowflake : climat et COVID-19
3. Joindre des données internes de vente avec les données acquises sur la marketplace pour mesure l'impact des facteurs externes
4. Utiliser Dataiku pour créer un modèle de prédiction du désabonnement des clients, sur base de leurs interactions passées
5. Visualiser le résultat sur une carte dans Dataiku
- [Video 6min](https://drive.google.com/file/d/15mHw_r2EUxqMyZdvd60SR3KfyKehJy6N/view?usp=share_link)
- [Quickstart Accelerating Data Science with Snowflake and Dataiku](https://quickstarts.snowflake.com/guide/data_science_with_dataiku/)
"""
"""
# Healthcare et Life sciences
### 💊 HL7 
1. importez des données au format HL7 dans Snowflake
2. Utilisez toutes les données directement dans des analyses et tableaux de bord
- [Video 8min](https://drive.google.com/file/d/15lwfnn-fWdOQu4nadMtOqL5Vj385uUMG/view?usp=share_link)
"""