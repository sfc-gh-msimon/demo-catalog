import streamlit as st

st.set_page_config(page_title="Analyste", page_icon="📄", layout="wide")
st.header("Analyste")
 
st.markdown(
"""#### 📄 Exraction des informations contenues dans des factures en PDF, analyse des ventes et prédiction des ventes
###### 1. Stockage de factures au format PDF dans un stage interne de Snowflake
###### 2. Extraction des informations contenues dans chaque facture (adresse, nom du client, montant de chaque ligne)
###### 3. Aggrégation des ventes par jour et par adresse
###### 4. Acquisition du dataset COVID-19 offert par StarSchema sur la marketplace de Snowflake
###### 5. Création d'une carte qui joint les ventes par état avec le nombre de cas COVID-19 confirmés par état
###### 6. Création d'un modèle qui prédit les ventes par jour dans les 90 prochains jours sur base des ventes passées.
""")
st.write("[Video](https://drive.google.com/file/d/15o881bYeTa4Sgdk89QFRgBlVllcUKYqY/view?usp=share_link)")  
st.write("[Github](https://github.com/sfc-gh-pneedleman/snowflake_lakehouse)")

st.markdown(
"""#### 📈 Snowsight
###### 1. Découvrez la nouvelle interface Web de Snowflake : Snowsight
###### 2. Accéder aux données sur Snowflake en SQL
###### 3. Créer des graphes et des tableaux de bord sur base de requêtes SQL
###### 4. Administrer la plateforme Snowflake et auditer les accès aux données
###### 5. Monitorer l'usage de la plateforme 
""")
st.write("[Video](https://drive.google.com/file/d/167jj-D5iGkB3C17d0AbARIHSfPQYbGVU/view?usp=share_link)")  
