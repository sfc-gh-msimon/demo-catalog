import streamlit as st
from annotated_text import annotated_text

st.set_page_config(page_title="Analyste", page_icon="📊")

'#### 🧾 Extraction des informations contenues dans des factures en PDF, analyse des ventes et prédiction des ventes'
annotated_text(
    ("Any",             "Industrie",        "#8ef","#000000"),
    ("PDF",             "Non-structuré",    "#faa","#000000"),
    ("Marketplace",     "Feature",          "#afa","#000000"),
    ("Snowpark Python", "Feature",          "#fea","#000000"),
    ("Streamlit",       "Front-end",        "#8ef","#000000")
)
'''
[Github](https://github.com/sfc-gh-pneedleman/snowflake_lakehouse)
1. Stockage de factures au format PDF dans un stage interne de Snowflake
2. Extraction des informations contenues dans chaque facture (adresse, nom du client, montant de chaque ligne)
3. Aggrégation des ventes par jour et par adresse
4. Acquisition du dataset COVID-19 offert par StarSchema sur la marketplace de Snowflake
5. Création d'une carte qui joint les ventes par état avec le nombre de cas COVID-19 confirmés par état
6. Création d'un modèle qui prédit les ventes par jour dans les 90 prochains jours sur base des ventes passées.
'''
st.video('https://youtu.be/SZGiYnC20v0')


'### 📊 Snowsight'
annotated_text(
    ("Any", "Industrie", "#8ef"),
    ("annotated", "adj 🧾", "#faa"),
    ("text", "noun", "#afa"),
    ("you", "pronoun", "#fea"),
    ("like", "verb", "#8ef"),
    ("thing", "noun", "#afa")
)
'''
1. Découvrez la nouvelle interface Web de Snowflake : Snowsight
2. Accéder aux données sur Snowflake en SQL
3. Créer des graphes et des tableaux de bord sur base de requêtes SQL
4. Administrer la plateforme Snowflake et auditer les accès aux données
5. Monitorer l'utilisation de la plateforme 
- [Video 20 min](https://drive.google.com/file/d/167jj-D5iGkB3C17d0AbARIHSfPQYbGVU/view?usp=share_link) [Video 3 min](https://drive.google.com/drive/folders/1VJzhPg5rrDCpwirH2SQta_JzeZudvX4y)
'''



'### 💵 Calcul du délai moyen de recouvrement, et des impayés sur base de données SAP'
annotated_text(
    ("Any", "Industrie", "#8ef"),
    ("annotated", "adj 🧾", "#faa"),
    ("text", "noun", "#afa"),
    ("you", "pronoun", "#fea"),
    ("like", "verb", "#8ef"),
    ("thing", "noun", "#afa")
)
'''
[Github](https://github.com/snowflakecorp/sfquickstarts-sap-dbt/blob/main/site/sfguides/src/kickstart_sap_to_snowflake/kickstart_sap_to_snowflake.md)
 [Quickstart SAP](https://snowflakecorp.github.io/sfquickstarts-sap-dbt/#0)
1. Extraire des données de systèmes SAP et les insérer sur Snowflake
2. Accéder aux données sur Snowflake en SQL
3. Modéliser les transformations nécessaires avec DBT : calculer le délai moyen de recouvrement 
4. Visualiser les résultats avec Tableau
'''
st.video('https://youtu.be/ycAjGAZDaM4')

'''### ⛅️ Analyser l'impact de facteurs externes(climat et COVID-19) sur les ventes et prédire quels clients vont se désabonner.''' 
annotated_text(
    ("Any", "Industrie", "#8ef"),
    ("annotated", "adj 🧾", "#faa"),
    ("text", "noun", "#afa"),
    ("you", "pronoun", "#fea"),
    ("like", "verb", "#8ef"),
    ("thing", "noun", "#afa")
)
'''
1. Créer un tableau de bord dans l'interface Snowsight
2. Acquérir des données sur la marketplace de Snowflake : climat et COVID-19
3. Joindre des données internes de vente avec les données acquises sur la marketplace pour mesure l'impact des facteurs externes
4. Utiliser Dataiku pour créer un modèle de prédiction du désabonnement des clients, sur base de leurs interactions passées
5. Visualiser le résultat sur une carte dans Dataiku
- [Video 6min](https://drive.google.com/file/d/15mHw_r2EUxqMyZdvd60SR3KfyKehJy6N/view?usp=share_link)
- [Quickstart Accelerating Data Science with Snowflake and Dataiku](https://quickstarts.snowflake.com/guide/data_science_with_dataiku/)
'''


'### 💊 HL7 '
annotated_text(
    ("Healthcare et Life sciences", "Industrie", "#8ef"),
    ("annotated", "adj 🧾", "#faa"),
    ("text", "noun", "#afa"),
    ("you", "pronoun", "#fea"),
    ("like", "verb", "#8ef"),
    ("thing", "noun", "#afa")
)
'''
1. importez des données au format HL7 dans Snowflake
2. Utilisez toutes les données directement dans des analyses et tableaux de bord
- [Video 8min](https://drive.google.com/file/d/15lwfnn-fWdOQu4nadMtOqL5Vj385uUMG/view?usp=share_link)
'''