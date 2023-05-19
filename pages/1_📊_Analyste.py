import streamlit as st
from annotated_text import annotated_text

st.set_page_config(page_title="Analyste", page_icon="📊",layout="wide")

'''#### 🧾 Extraction des informations contenues dans des factures en PDF, analyse des ventes et prédiction des ventes
1. Stockage de factures au format PDF dans un stage interne de Snowflake
2. Extraction des informations contenues dans chaque facture (adresse, nom du client, montant de chaque ligne)
3. Aggrégation des ventes par jour et par adresse
4. Acquisition du dataset COVID-19 offert par StarSchema sur la marketplace de Snowflake
5. Création d'une carte qui joint les ventes par état avec le nombre de cas COVID-19 confirmés par état
6. Création d'un modèle qui prédit les ventes par jour dans les 90 prochains jours sur base des ventes passées.
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Any",             "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("Factures PDF",    "Données",          "#faa","#000"),"   \n",
    ("CRM Parquet",     "Données",          "#faa","#000"),"   \n",
    ("Marketplace",     "Feature",          "#fea","#000"),"   \n",
    ("Snowpark Python", "Feature",          "#fea","#000"),"   \n",
    ("Streamlit",       "Outil",            "#afa","#000")
   )
with col2:
   st.video('https://youtu.be/SZGiYnC20v0')
with col3:
   '[Github](https://github.com/sfc-gh-pneedleman/snowflake_lakehouse)'

'''### 📊 Snowsight
1. Découvrez la nouvelle interface Web de Snowflake : Snowsight
2. Accéder aux données sur Snowflake en SQL
3. Créer des graphes et des tableaux de bord sur base de requêtes SQL
4. Administrer la plateforme Snowflake et auditer les accès aux données
5. Monitorer l'utilisation de la plateforme 
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Any",             "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("Dashboards",      "Feature",          "#fea","#000"),"   \n",
    ("Administration",  "Feature",          "#fea","#000"),"   \n",
    ("Monitoring",      "Feature",          "#fea","#000"),"   \n",
    ("Snowsight",       "Outil",            "#afa","#000")
   )
with col2:
   st.video('https://youtu.be/rMXLpGICcyE')
with col3:
   '[Video 3 min](https://drive.google.com/drive/folders/1VJzhPg5rrDCpwirH2SQta_JzeZudvX4y)'


'''### 💵 Calcul du délai moyen de recouvrement, et des impayés sur base de données SAP
1. Extraire des données de systèmes SAP et les insérer sur Snowflake
2. Accéder aux données sur Snowflake en SQL
3. Modéliser les transformations nécessaires avec DBT : calculer le délai moyen de recouvrement 
4. Visualiser les résultats avec Tableau
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Any",                 "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("SAP ERP Finance",     "Données",          "#faa","#000"),"   \n",
    ("Modélisation en SQL", "Feature",          "#fea","#000"),"   \n",
    ("DBT",                 "Outil",            "#afa","#000"),"   \n",
    ("Tableau",             "Outil",            "#afa","#000")
   )
with col2:
   st.video('https://youtu.be/ycAjGAZDaM4')
with col3:
   '[Github](https://github.com/snowflakecorp/sfquickstarts-sap-dbt/blob/main/site/sfguides/src/kickstart_sap_to_snowflake/kickstart_sap_to_snowflake.md)  \n [Quickstart](https://snowflakecorp.github.io/sfquickstarts-sap-dbt/#0)'

'''### ⛅️ Analyser l'impact de facteurs externes(climat et COVID-19) sur les ventes et prédire quels clients vont se désabonner
1. Créer un tableau de bord dans l'interface Snowsight
2. Acquérir des données sur la marketplace de Snowflake : climat et COVID-19
3. Joindre des données internes de vente avec les données acquises sur la marketplace pour mesure l'impact des facteurs externes
4. Utiliser Dataiku pour créer un modèle de prédiction du désabonnement des clients, sur base de leurs interactions passées
5. Visualiser le résultat sur une carte dans Dataiku
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Retail",              "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("COVID-19",            "Données",          "#faa","#000"),"   \n",
    ("Climat",              "Données",          "#faa","#000"),"   \n",
    ("Marketplace",         "Feature",          "#fea","#000"),"   \n",
    ("Snowsight",           "Outil",            "#afa","#000"),"   \n",
    ("Dataiku",             "Outil",            "#afa","#000")
   )
with col2:
   st.video('https://youtu.be/AfGYn2tcDk0')
with col3:
   '[Quickstart](https://quickstarts.snowflake.com/guide/data_science_with_dataiku/)'


'''### 💊 Utiliser des données HL7 dans des analyses médicales
1. Importer et stocker des données au format HL7 FHIR dans Snowflake
2. Modéliser des données médicales au format HL7 FHIR en SQL
3. Utiliser ces les données directement dans des analyses et tableaux de bord
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Healthcare Life sciences",    "Industrie",    "#8ef","#000"),"   \n","   \n",
    ("HL7 FHIR",                    "Données",      "#faa","#000"),"   \n",
    ("Modélisation en SQL",         "Feature",      "#fea","#000"),"   \n",
    ("Snowsight",                   "Outil",        "#afa","#000"),"   \n",
    ("Tableau",                     "Outil",        "#afa","#000")
   )
with col2:
   st.video('https://youtu.be/s5VVT8X9dvE')
with col3:
   '[Quickstart](https://quickstarts.snowflake.com/guide/processing_hl7_fhir_messages_with_snowflake/)'


'''### 🌐 Partager des données sur Snowflake
1. Créer des vues et des fonctions sécurisées pour partager des données et du code
2. Créer un listing afin de partager un produit data à une autre organisation sur Snowflake sans copie
3. Accéder à des données depuis un autre compte
4. Limiter l'accès à une partie de la donnée en fonction du consommateur avec une row access policy
5. Accéder à des données depuis un compte reader
6. Accéder à des fonctions partagées depuis un autre compte
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Any",                    "Industrie",     "#8ef","#000"),"   \n","   \n",
    ("CRM",                    "Données",       "#faa","#000"),"   \n",
    ("Data sharing",           "Feature",       "#fea","#000"),"   \n",
    ("Code sharing",           "Feature",       "#fea","#000"),"   \n",
    ("Row access policy",      "Feature",       "#fea","#000"),"   \n",
    ("Reader account",         "Feature",       "#fea","#000"),"   \n",
    ("Snowsight",              "Outil",         "#afa","#000"),"   \n"
   )
with col2:
   st.video('https://youtu.be/X5-R_8U-C6U')
with col3:
   '[Quickstart](https://quickstarts.snowflake.com/guide/tasty_bytes_zero_to_snowflake_collaboration/)'

'''### 🧙 Requêter Snowflake avec Hex magic
1. Générer du code SQL automatiquement avec Hex magic
2. Visualiser des données directement dans un notebook Hex
3. Corriger et commenter automatiquement le code SQL
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Any",                         "Industrie",     "#8ef","#000"),"   \n","   \n",
    ("Génération de code",          "Feature",       "#fea","#000"),"   \n",
    ("Génération de commentaire",   "Feature",       "#fea","#000"),"   \n",
    ("Hex",                         "Outil",         "#afa","#000"),"   \n"
   )
with col2:
   st.video('https://youtu.be/JhuNaroFK1o')