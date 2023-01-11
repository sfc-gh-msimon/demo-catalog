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



'### 🏡 Prédire la rentabilité des investissements immobiliers'
annotated_text(
    ("Any",                  "Industrie",        "#8ef","#000"),
    ("Annonces immobilières","Données",          "#faa","#000"),
    ("Snowpark python",      "Feature",          "#fea","#000"),
    ("Streamlit",            "Outil",            "#afa","#000"),
    ("Jupyter notebook",     "Outil",            "#afa","#000")
)
'''
1. Sur base d'une liste d'annonces immobilières de ventes et locations en France, prédire un prix de location pour chaque annonce de vente
2. Calculer la rentabilité de chaque annonce de vente (prix de location estimé / prix d'achat du bien)
3. Visualiser les résultats dans une application Streamlit
4. Explorer les résultats par région pour trouver les annonces les plus rentables !
'''
col1, col2, col3 = st.columns(3)
with col2:
   st.video('https://youtu.be/AXeOTxJo_78')



'### 👩‍👩‍👧‍👦 Déduplication de master data avec TF-IDF'
annotated_text(
    ("Any",             "Industrie",        "#8ef","#000"),
    ("Snowpark python", "Feature",          "#fea","#000"),
    ("Hex",             "Outil",            "#afa","#000")
)
'''
1. Le problèmes des clients qui ont des master data dupliquées dans plusieurs systèmes
2. Les algorithmes de déduplication, y compris TF-IDF
3. Implémenter TF-IDF en Python sur Snowpark avec Hex
'''
col1, col2, col3 = st.columns(3)
with col2:
   st.video('https://youtu.be/4tvesDD5gQg')



'### 🥷🏻 Détection de fraudes sur des transactions e-commerce'
annotated_text(
    ("Any",                     "Industrie",        "#8ef","#000"),
    ("Transactions e-commerce", "Données",          "#faa","#000"),
    ("Snowpark python",         "Feature",          "#fea","#000"),
    ("Marketplace",             "Feature",          "#fea","#000"),
    ("Jupyter notebook",        "Outil",            "#afa","#000")
)
'''
1. Ingérer des données de transaction E-commerce dans Snowflake
2. Enrichir les transactions avec des données mises à disposition sur la Snowflake Marketplace par IPInfo
3. Visualiser les transactions passées : quels sont les facteurs suspects des transactions frauduleuses
4. Sur base de résultats passés et d'informations sur les adresses IP fournies par IPInfo, créer un modèle de prédiction de fraudes
5. Exécuter l'inférence en masse sur Snowflake
'''
col1, col2, col3 = st.columns(3)
with col2:
   st.video('https://youtu.be/T83FBoTsu4Y')