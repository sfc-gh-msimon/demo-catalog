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
col1, col2, col3 = st.columns(([1,2,1]))
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
[Github](https://github.com/snowflakecorp/snowpark-python-xgboost-realestate)
1. Sur base d'une liste d'annonces immobilières de ventes et locations en France, prédire un prix de location pour chaque annonce de vente
2. Calculer la rentabilité de chaque annonce de vente (prix de location estimé / prix d'achat du bien)
3. Visualiser les résultats dans une application Streamlit
4. Explorer les résultats par région pour trouver les annonces les plus rentables !
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col2:
   st.video('https://youtu.be/AXeOTxJo_78')



'### 👩‍👩‍👧‍👦 Déduplication de master data avec TF-IDF'
annotated_text(
    ("Any",             "Industrie",        "#8ef","#000"),
    ("Snowpark python", "Feature",          "#fea","#000"),
    ("Hex",             "Outil",            "#afa","#000")
)
'''
[Hex notebook](https://app.hex.tech/snowflake/hex/d264214a-09cc-40e4-b980-a294ff3114bc/draft/logic) - 
[Blog](https://medium.com/snowflake/entity-matching-using-tf-idf-in-snowpark-python-3d1942d4ef19)
1. De nombreuses organisations ont des master data (clients, produits) dupliquées dans plusieurs systèmes.
2. Utiliser Hex pour se connecter à Snowflake en Python et SQL, pour accéder à une table de clients qui contient des trous et une table de clients complète.
3. Implémenter un algorithme de déduplication entre le jeu de données complet et celui qui contient des trous. Déduplication avec TF-IDF en Python exécuté sur Snowpark
'''
col1, col2, col3 = st.columns(([1,2,1]))
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
[Github](https://github.com/Snowflake-Labs/snowpark-python-examples/tree/main/Fraud-Detection-Demo) - 
[English video](https://www.youtube.com/watch?v=zuBnBpFtUjA&ab_channel=SnowflakeInc.)
1. Ingérer des données de transaction E-commerce dans Snowflake
2. Enrichir les transactions avec des données mises à disposition sur la Snowflake Marketplace par IPInfo
3. Visualiser les transactions passées : quels sont les facteurs suspects des transactions frauduleuses
4. Sur base de résultats passés et d'informations sur les adresses IP fournies par IPInfo, créer un modèle de prédiction de fraudes
5. Exécuter l'inférence en masse sur Snowflake
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col2:
   st.video('https://youtu.be/T83FBoTsu4Y')


'### 🏎️ Marketing analytics : Transformez vos clients en fans'
annotated_text(
    ("Evenements",              "Industrie",        "#8ef","#000"),
    ("Marketing",               "Données",          "#faa","#000"),
    ("Neustar",                 "Données",          "#faa","#000"),
    ("Snowpark python",         "Feature",          "#fea","#000"),
    ("Marketplace",             "Feature",          "#fea","#000"),
    ("Jupyter notebook",        "Outil",            "#afa","#000"),
    ("Snowsight",               "Outil",            "#afa","#000"),
    ("Tableau",                 "Outil",            "#afa","#000")
)
'''
[Github](https://github.com/snowflakecorp/frostbytes/tree/main/Department%20-%20Marketing%20Analytics) 
1. Comprendre nos clients
- Explorer les données internes sur les clients
- Joindre les données internes aux données fournies sur la Marketplace par Neustar
- Créer des fonctions en SQL pour permettre aux analystes de requêter les données plus facilement

2. Data Science
- Déterminer le lead score de chaque client pour chaque évènement : entrainer un modèle xgboost, déployer le modèle, expliquer le modèle
- Déterminer la meilleure action à prendre pour chaque client (téléphone, mail, pas de contact) en fonction de son historique : entrainer un modèle, déployer le modèle, expliquer le modèle, automatiser l'historisation des performances du modèle et le ré-entrainement en cas de drift.

3. Analytics et prise d'action
- Dashboard corporate dans snowsight pour avoir une vue d'ensemble des ventes et de la performance des évènements, ainsi qu'un drill-down sur les clients
- Dashboard opérationnel dans Tableau pour donner aux équipes de contact clients les informations nécessaires afin d'offrir le meilleur service (lead score, meilleure action à prendre) et aux équipes marketing pour confectionner des campagnes marketing pour les prochains évènements
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col2:
   st.video('https://youtu.be/JtPwHQJ25TA')
