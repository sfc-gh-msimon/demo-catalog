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

'''### 🏂 Snowflake connector for ServiceNow
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