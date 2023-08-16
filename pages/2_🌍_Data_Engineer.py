import streamlit as st
from annotated_text import annotated_text

st.set_page_config(page_title="Data engineer", page_icon="🌍",layout="wide")

'''#### 🔧 Join elimination
Dans certains cas, une jointure sur une colonne clé peut faire référence à des tables qui ne sont pas nécessaires pour cette jointure. 
Si vos tables ont des colonnes clés et que vous appliquez les contraintes UNIQUE, PRIMARY KEY et FOREIGN KEY, Snowflake peut améliorer les performances des requêtes en [éliminant les jointures](https://docs.snowflake.com/en/user-guide/join-elimination.html) inutiles sur les colonnes clés.
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Any",             "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("Join elimination","Feature",          "#fea","#000")
    )
with col2:
   st.video('https://youtu.be/QJ0zXosPDQQ')


'''#### 🏎 Optimiser la performance sur Snowflake
1. L'architecture de Snowflake
2. Le scaling sur Snowflake
3. Comment déterminer la taille optimale des virtual warehouses
4. Les micro-partitions sur Snowflake
5. Les services de Snowflake pour optimiser les performances : Automatic Clustering, Materialized views, Search Optimization Service
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Any",                         "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("Automatic clustering",        "Feature",          "#fea","#000"),"   \n",
    ("Materialized views",          "Feature",          "#fea","#000"),"   \n",
    ("Search optimization service", "Feature",          "#fea","#000")
    )
with col2:
   st.video('https://youtu.be/N-ifoTHtFbU')


'''### 🚲 Administration de base de données, DevOps et création de tableaux de bords chez Citibike
1. Administration de base de données
2. DevOps : clonage de base de données et masking de données pour les développeurs
3. Préparation de données et création de tableaux de bords sur Snowsight
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Any",                         "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("Administration",              "Feature",          "#fea","#000"),"   \n",
    ("Cloning",                     "Feature",          "#fea","#000"),"   \n",
    ("Time travel",                 "Feature",          "#fea","#000"),"   \n",
    ("Snowsight",                   "Outil",            "#afa","#000")
    )
with col2:
   st.video('https://youtu.be/4jPd8pZS0xw')
with col3:
   '[Github](https://github.com/snowflakecorp/citibike/wiki/V4_1-Welcome-to-Citibike)    \n [Quickstart](https://quickstarts.snowflake.com/guide/getting_started_with_snowflake/)'



'''### 🤝 Créer une data clean room sur Snowflake
1. Introduction aux data clean rooms
2. Les composants uniques de Snowflake pour créer des data clean rooms : Data sharing, row access policies, stored procedures, streams and tasks.
3. Créer une data clean room entre deux organisations
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Media",               "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("Row access policy",   "Feature",          "#fea","#000"),"   \n",
    ("Data sharing",        "Feature",          "#fea","#000"),"   \n",
    ("Stored procedures",   "Feature",          "#fea","#000"),"   \n",
    ("Streams&Tasks",       "Feature",          "#fea","#000")
    )
with col2:
   st.video('https://youtu.be/_0wE0p4vglo')
with col3:
    '[Quickstart](https://quickstarts.snowflake.com/guide/build_a_data_clean_room_in_snowflake_advanced/)'


'''### 🧬 Utiliser le clustering pour accélérer des requêtes sur des données genomics
1. Stocker de grandes quantités de données de gènes dans Snowflake
2. Joindre des allèles avec des études stockées dans deux tables différentes, afin d'identifier quelles allèles ont potentiellement un effet délétère
3. Accélérer des requêtes sur de grandes tables grace à l'architecture des micro-partitions de Snowflake (pruning) et au clustering
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Healthcare Life sciences",    "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("Genomics",                    "Données",          "#faa","#000"),"   \n",
    ("Automatic Clustering",        "Feature",          "#fea","#000")
    )
with col2:
   st.video('https://youtu.be/vi8eG9GY0go')

'''### 🏂 Data Engineering avec Snowpark
1. Apprenez à utiliser Snowpark pour faire du data engineering.
2. Dans ce quickstarts, nous utilisons des données Point of Sales représentant des ventes partout dans le monde, et nous mesurons l'impact du climat sur les ventes dans chaque ville.
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Retail",                  "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("Point of sales",          "Données",          "#faa","#000"),"   \n",
    ("Elastic compute",         "Feature",          "#fea","#000"),"   \n",
    ("Streams/Tasks",           "Feature",          "#fea","#000"),"   \n",
    ("Snowpark Python",         "Feature",          "#fea","#000"),"   \n",
    ("Github actions",          "Feature",          "#fea","#000")
    )
with col2:
   st.video('https://youtu.be/beMcZOur-fM')
with col3:
   '[Quickstart](https://quickstarts.snowflake.com/guide/data_engineering_pipelines_with_snowpark_python/)   \n [Webinar](https://resources.snowflake.com/webinars-thought-leadership/snowpark-101-technical-overview-3)'

'''### 🧑‍🏭 Snowflake connector for ServiceNow
1. Utiliser le Snowflake connector for ServiceNow pour synchroniser 3 tables depuis ServiceNow vers Snowflake.
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Toutes",                  "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("Incidents",               "Données",          "#faa","#000"),"   \n",
    ("ServiceNow Connector",    "Feature",          "#fea","#000"),"   \n",
    ("Native app",              "Feature",          "#fea","#000"),"   \n",
    ("Marketplace",             "Feature",          "#fea","#000")
    )
with col2:
   st.video('https://youtu.be/jMMCMPHNXDw')
with col3:
   '[Quickstart](https://quickstarts.snowflake.com/guide/servicenow_to_snowflake_connector/)'


'''### 📮 Requêter Snowflake via la SQL REST API avec Postman
1. Enregistrer une clé publique pour un utilisateur sur snowflake
2. Générer un JWT pour communiquer avec Snowflake de façon sécurisée
3. Requêter Snowflake via la SQL REST API
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Toutes",                  "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("Key/pair authentication", "Feature",          "#fea","#000"),"   \n",
    ("SQL REST API",            "Feature",          "#fea","#000"),"   \n"
    )
with col2:
   st.video('https://youtu.be/XO0SMvbGbDg')
with col3:
   '[Quickstart](https://quickstarts.snowflake.com/guide/a_postman_tutorial_for_snowflake_sql_api)'

'''### 🌊 Streaming & Dynamic Tables pour l'analyse d'ordres de bourse
Chaque utilisateur a des besoins différents en matière de fraicheur de données. 
Snowflake répond aux besoins d'insertion et de transformation de données en batch et en streaming.
Dans cette vidéo, je prends l'exemple d'une analyse d'ordres d'achat et de vente en bourse : il y a une grande quantité d'insertions et de suppressions rapides d'ordres, et il est nécessaire d'analyser les données avec une latence de moins de quelques minutes.
J'insère des données d'ordres au format JSON en streaming dans snowflake avec une latence de moins de 10 secondes. Ensuite, je transforme les données dans snowflake de façon incrémentale avec une latence de 1 minute.

1. Définir l'architecture : les sources, les transformations et les consommateurs de données
2. Emettre des données en continu depuis une application java vers snowflake
3. Insérer ces données dans une table de staging sur snowflake
4. Créer des dynamic tables qui définissent des transformations sur les données insérées en continu
5. Protéger les données en les divisant par schéma et en décryptant les données à risque seulement pour les utilisateurs autorisés

Quickstarts pour répliquer par vous-même : https://quickstarts.snowflake.com/guide/CDC_SnowpipeStreaming_DynamicTables
Best practices pour l'ingestion de données : https://www.snowflake.com/blog/data-ingestion-best-practices-part-three/
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Finance",                  "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("Snowpipe streaming",       "Feature",          "#fea","#000"),"   \n",
    ("Dynamic table",         "Feature",          "#fea","#000"),"   \n"
    )
with col2:
   st.video('https://youtu.be/hao5qPc5vVc')
with col3:
   '[Quickstarts](https://quickstarts.snowflake.com/guide/CDC_SnowpipeStreaming_DynamicTables)'


'''### 📮 Appeler une API REST depuis Snowflake avec une external function
1. Déployer une lambda sur AWS avec le module Node.js Serverless
2. Créer une external function dans snowflake qui appelle la lambda sur AWS avec serverless
3. Utiliser l'external function pour exécuter des appels REST en GET et en POST
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Toutes",                  "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("External Function",       "Feature",          "#fea","#000"),"   \n",
    ("API Integration",         "Feature",          "#fea","#000"),"   \n"
    )
with col2:
   st.video('https://youtu.be/A7ZWyYazlVU')
with col3:
   '[Blog](https://medium.com/starschema-blog/starsnow-http-client-for-snowflake-sql-e1b329293fc6)'
