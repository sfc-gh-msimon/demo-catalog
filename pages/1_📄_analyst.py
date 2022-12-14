import streamlit as st

st.set_page_config(page_title="Analyste", page_icon="📄", layout="wide")
st.header("Analyste")
 
st.markdown(
"""
# Toutes industries
#### 📄 Exraction des informations contenues dans des factures en PDF, analyse des ventes et prédiction des ventes
1. Stockage de factures au format PDF dans un stage interne de Snowflake
2. Extraction des informations contenues dans chaque facture (adresse, nom du client, montant de chaque ligne)
3. Aggrégation des ventes par jour et par adresse
4. Acquisition du dataset COVID-19 offert par StarSchema sur la marketplace de Snowflake
5. Création d'une carte qui joint les ventes par état avec le nombre de cas COVID-19 confirmés par état
6. Création d'un modèle qui prédit les ventes par jour dans les 90 prochains jours sur base des ventes passées.
- [Video](https://drive.google.com/file/d/15o881bYeTa4Sgdk89QFRgBlVllcUKYqY/view?usp=share_link)
- [Github](https://github.com/sfc-gh-pneedleman/snowflake_lakehouse)
""")

st.markdown(
"""
#### 📈 Snowsight
1. Découvrez la nouvelle interface Web de Snowflake : Snowsight
2. Accéder aux données sur Snowflake en SQL
3. Créer des graphes et des tableaux de bord sur base de requêtes SQL
4. Administrer la plateforme Snowflake et auditer les accès aux données
5. Monitorer l'utilisation de la plateforme 
- [Video](https://drive.google.com/file/d/167jj-D5iGkB3C17d0AbARIHSfPQYbGVU/view?usp=share_link)
""")

st.markdown(
"""
#### 📈 Calcul du délai moyen de recouvrement, et des impayés sur base de données SAP
1. Extraire des données de systèmes SAP et les insérer sur Snowflake
2. Accéder aux données sur Snowflake en SQL
3. Modéliser les transformations nécessaires avec DBT : calculer le délai moyen de recouvrement 
4. Visualiser les résultats avec Tableau
- [Video](https://drive.google.com/file/d/16qtPbJqYT4Rq7m7dWyiH-L1bcXkrtk6t/view?usp=share_link)
- [Github](https://github.com/snowflakecorp/sfquickstarts-sap-dbt/blob/main/site/sfguides/src/kickstart_sap_to_snowflake/kickstart_sap_to_snowflake.md)
- [Quickstart](https://snowflakecorp.github.io/sfquickstarts-sap-dbt/#0)
""") 

st.markdown(
"""
# Healthcare et Life sciences
#### 💊 HL7 
1. importez des données au format HL7 dans Snowflake
2. Utilisez toutes les données directement dans des analyses et tableaux de bord
- [Video](https://drive.google.com/file/d/15lwfnn-fWdOQu4nadMtOqL5Vj385uUMG/view?usp=share_link)
""")