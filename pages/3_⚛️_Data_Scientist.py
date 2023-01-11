import streamlit as st
from annotated_text import annotated_text

st.set_page_config(page_title="Data scientist", page_icon="⚛️",layout="wide")


'### 🎥 Snowpark 101 - Analyse sur les films'
annotated_text(
    ("Any",                 "Industrie",        "#8ef","#000"),
    ("Snowpark python",     "Feature",          "#fea","#000"),
    ("Jupyter notebook",    "Outil",            "#afa","#000")
)
'''
[Github](https://github.com/Snowflake-Labs/snowpark-python-examples/tree/main/Snowpark101)
1. Utiliser un Jupyter Notebook pour accéder à Snowflake avec Snowpark python.
2. Créer des fonctions en local et les exécuter sur Snowflake
3. Créer une régression linéaire pour préduire le nombre de films produits annuellement
'''
col1, col2, col3 = st.columns(3)
with col2:
   st.video('https://youtu.be/_peXDwdEpXA')



'### 🏡 Immobilier'
annotated_text(
    ("Any",                  "Industrie",        "#8ef","#000"),
    ("Snowpark python",      "Feature",          "#fea","#000"),
    ("Jupyter notebook",     "Outil",            "#afa","#000")
)
'''

'''
col1, col2, col3 = st.columns(3)
with col2:
   st.video('https://youtu.be/rMXLpGICcyE')



'### 👩‍👩‍👧‍👦 Master data management : entity matching avec TF-IDF'
annotated_text(
    ("Any",             "Industrie",        "#8ef","#000"),
    ("Snowpark python",      "Feature",          "#fea","#000"),
    ("Jupyter notebook",       "Outil",            "#afa","#000")
)
'''

'''
col1, col2, col3 = st.columns(3)
with col2:
   st.video('https://youtu.be/rMXLpGICcyE')



'### 🥷🏻 Détection de fraudes '
annotated_text(
    ("Any",             "Industrie",        "#8ef","#000"),
    ("Snowpark python",      "Feature",          "#fea","#000"),
    ("Jupyter notebook",       "Outil",            "#afa","#000")
)
'''

'''
col1, col2, col3 = st.columns(3)
with col2:
   st.video('https://youtu.be/rMXLpGICcyE')