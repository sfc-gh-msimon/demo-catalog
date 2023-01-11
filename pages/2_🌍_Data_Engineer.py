import streamlit as st
from annotated_text import annotated_text

st.set_page_config(page_title="Data engineer", page_icon="🌍",layout="wide")

'#### 🔧 Join elimination'
annotated_text(
    ("Any",             "Industrie",        "#8ef","#000"),
    ("Join elimination","Feature",          "#fea","#000")
)
'''
Dans certains cas, une jointure sur une colonne clé peut faire référence à des tables qui ne sont pas nécessaires pour cette jointure. 
Si vos tables ont des colonnes clés et que vous appliquez les contraintes UNIQUE, PRIMARY KEY et FOREIGN KEY, Snowflake peut améliorer les performances des requêtes en [éliminant les jointures](https://docs.snowflake.com/en/user-guide/join-elimination.html) inutiles sur les colonnes clés.
'''
col1, col2, col3 = st.columns(3)
with col2:
   st.video('https://youtu.be/QJ0zXosPDQQ')


'#### 🏎 Performance optimization'
annotated_text(
    ("Any",                         "Industrie",        "#8ef","#000"),
    ("Automatic clustering",        "Feature",          "#fea","#000"),
    ("Materialized views",          "Feature",          "#fea","#000"),
    ("Search optimization service", "Feature",          "#fea","#000")
)
'''
1. L'architecture de Snowflake
2. Le scaling sur Snowflake
3. Comment déterminer la taille optimale des virtual warehouses
4. Les micro-partitions sur Snowflake
5. Les services de Snowflake pour optimiser les performances : Automatic Clustering, Materialized views, Search Optimization Service
'''
col1, col2, col3 = st.columns(3)
with col2:
   st.video('https://youtu.be/N-ifoTHtFbU')



'### 🚲 Administration de base de données, DevOps et création de tableaux de bords chez Citibike'
annotated_text(
    ("Any",                         "Industrie",        "#8ef","#000"),
    ("Administration",              "Feature",          "#fea","#000"),
    ("Cloning",                     "Feature",          "#fea","#000"),
    ("Time travel",                 "Feature",          "#fea","#000"),
    ("Snowsight",                   "Outil",            "#afa","#000")
)
'''
[Github](https://github.com/snowflakecorp/citibike/wiki/V4_1-Welcome-to-Citibike) - 
[Quickstart](https://quickstarts.snowflake.com/guide/getting_started_with_snowflake/)
1. Administration de base de données
2. DevOps : clonage de base de données et masking de données pour les développeurs
3. Préparation de données et création de tableaux de bords sur Snowsight
'''
col1, col2, col3 = st.columns(3)
with col2:
   st.video('https://youtu.be/4jPd8pZS0xw')



'### 🤝 Créer une data clean room sur Snowflake'
annotated_text(
    ("Media",               "Industrie",        "#8ef","#000"),
    ("Row access policy",   "Feature",          "#fea","#000"),
    ("Data sharing",        "Feature",          "#fea","#000"),
    ("Stored procedures",   "Feature",          "#fea","#000"),
    ("Streams&Tasks",       "Feature",          "#fea","#000")
)
'''
[Quickstart](https://quickstarts.snowflake.com/guide/build_a_data_clean_room_in_snowflake_advanced/)
1. Introduction aux data clean rooms
2. Les composants uniques de Snowflake pour créer des data clean rooms : Data sharing, row access policies, stored procedures, streams and tasks.
3. Créer une data clean room entre deux organisations
'''
col1, col2, col3 = st.columns(3)
with col2:
   st.video('https://youtu.be/_0wE0p4vglo')



'### 🧬 Utiliser le clustering pour accélérer des requêtes sur des données genomics'
annotated_text(
    ("Healthcare Life sciences",    "Industrie",        "#8ef","#000"),
    ("Genomics",                    "Données",          "#faa","#000"),
    ("Automatic Clustering",        "Feature",          "#fea","#000")
)
'''
1. Stocker de grandes quantités de données de gènes dans Snowflake
2. Joindre des allèles avec des études stockées dans deux tables différentes, afin d'identifier quelles allèles ont potentiellement un effet délétère
3. Accélérer des requêtes sur de grandes tables grace à l'architecture des micro-partitions de Snowflake (pruning) et au clustering
'''
col1, col2, col3 = st.columns(3)
with col2:
   st.video('https://youtu.be/vi8eG9GY0go')
