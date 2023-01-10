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



"""
### 
- [Video 18 min](https://drive.google.com/file/d/16vgQ-5IkT2bPaxvnqzEOs9kbc_tw-eQt/view?usp=share_link)
"""

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




"""
### 🚲 Administration de base de données, DevOps et création de tableaux de bords chez Citibike
1. Administration de base de données
2. DevOps : clonage de base de données et masking de données pour les développeurs
3. création de tableaux de bords sur Snowsight
- [Video 24 min](https://drive.google.com/file/d/15nViolkbysKCVbDSV1JcmebOKb7XswLB/view?usp=share_link)
- [Github](https://github.com/snowflakecorp/citibike/wiki/V4_1-Welcome-to-Citibike)
- [Quickstart Zero to Snowflake](https://quickstarts.snowflake.com/guide/getting_started_with_snowflake/)
"""



"""
### 🤝 Créez votre data clean room sur Snowflake 
1. Introduction aux data clean rooms
2. Les composants uniques de Snowflake pour créer des data clean rooms : Data sharing, row access policies, stored procedures, streams and tasks.
3. Créer une data clean room entre deux organisations
"""
st.video('https://youtu.be/_0wE0p4vglo')


"""
# Healthcare et Life sciences
### 🧬 Genomics 
1. Stocker de grandes quantités de données de gènes dans Snowflake
2. Joindre des allèles avec des études stockées dans deux tables différentes, afin d'identifier quelles allèles ont potentiellement un effet délétère
3. Accélérer des requêtes sur de grandes tables grace à l'architecture des micro-partitions de Snowflake (pruning) et au clustering
- [Video 14 min](https://drive.google.com/file/d/154GzuSZBXUjtSPs_e6LFAWwA9Hg3NoVr/view?usp=share_link)
"""