import streamlit as st
from annotated_text import annotated_text

st.set_page_config(page_title="Data scientist", page_icon="⚛️",layout="wide")


'''### 🎥 Snowpark 101 - Analyse sur les films
1. Utiliser un Jupyter Notebook pour accéder à Snowflake avec Snowpark python.
2. Créer des fonctions en local et les exécuter sur Snowflake
3. Créer une régression linéaire pour préduire le nombre de films produits annuellement
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Any",                 "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("Snowpark python",     "Feature",          "#fea","#000"),"   \n",
    ("Jupyter notebook",    "Outil",            "#afa","#000")
    )
with col2:
   st.video('https://youtu.be/_peXDwdEpXA')
with col3:
   '[Github](https://github.com/Snowflake-Labs/snowpark-python-examples/tree/main/Snowpark101)'




'''### 🏡 Prédire la rentabilité des investissements immobiliers
1. Sur base d'une liste d'annonces immobilières de ventes et locations en France, prédire un prix de location pour chaque annonce de vente
2. Calculer la rentabilité de chaque annonce de vente (prix de location estimé / prix d'achat du bien)
3. Visualiser les résultats dans une application Streamlit
4. Explorer les résultats par région pour trouver les annonces les plus rentables !
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Any",                  "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("Annonces immobilières","Données",          "#faa","#000"),"   \n",
    ("Snowpark python",      "Feature",          "#fea","#000"),"   \n",
    ("Streamlit",            "Outil",            "#afa","#000"),"   \n",
    ("Jupyter notebook",     "Outil",            "#afa","#000")
    )
with col2:
   st.video('https://youtu.be/AXeOTxJo_78')
with col3:
   '[Github](https://github.com/snowflakecorp/snowpark-python-xgboost-realestate)'


'''### 👩‍👩‍👧‍👦 Déduplication de master data avec TF-IDF
1. De nombreuses organisations ont des master data (clients, produits) dupliquées dans plusieurs systèmes.
2. Utiliser Hex pour se connecter à Snowflake en Python et SQL, pour accéder à une table de clients qui contient des trous et une table de clients complète.
3. Implémenter un algorithme de déduplication entre le jeu de données complet et celui qui contient des trous. Déduplication avec TF-IDF en Python exécuté sur Snowpark
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Any",             "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("Snowpark python", "Feature",          "#fea","#000"),"   \n",
    ("Hex",             "Outil",            "#afa","#000")
    )
with col2:
   st.video('https://youtu.be/4tvesDD5gQg')
with col3:
   '[Hex notebook](https://app.hex.tech/snowflake/hex/d264214a-09cc-40e4-b980-a294ff3114bc/draft/logic)  \n [Blog](https://medium.com/snowflake/entity-matching-using-tf-idf-in-snowpark-python-3d1942d4ef19)'



'''### 🥷🏻 Détection de fraudes sur des transactions e-commerce
1. Ingérer des données de transaction E-commerce dans Snowflake
2. Enrichir les transactions avec des données mises à disposition sur la Snowflake Marketplace par IPInfo
3. Visualiser les transactions passées : quels sont les facteurs suspects des transactions frauduleuses
4. Sur base de résultats passés et d'informations sur les adresses IP fournies par IPInfo, créer un modèle de prédiction de fraudes
5. Exécuter l'inférence en masse sur Snowflake
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Any",                     "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("Transactions e-commerce", "Données",          "#faa","#000"),"   \n",
    ("Snowpark python",         "Feature",          "#fea","#000"),"   \n",
    ("Marketplace",             "Feature",          "#fea","#000"),"   \n",
    ("Jupyter notebook",        "Outil",            "#afa","#000")
    )
with col2:
   st.video('https://youtu.be/T83FBoTsu4Y')
with col3:
   '[Github](https://github.com/Snowflake-Labs/snowpark-python-examples/tree/main/Fraud-Detection-Demo)  \n [English video](https://www.youtube.com/watch?v=zuBnBpFtUjA&ab_channel=SnowflakeInc.)'


'''### 🏎️ Marketing analytics : Transformez vos clients en fans
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
with col1:
   annotated_text(
    ("Evenements",              "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("Marketing",               "Données",          "#faa","#000"),"   \n",
    ("Neustar",                 "Données",          "#faa","#000"),"   \n",
    ("Snowpark python",         "Feature",          "#fea","#000"),"   \n",
    ("Marketplace",             "Feature",          "#fea","#000"),"   \n",
    ("Jupyter notebook",        "Outil",            "#afa","#000"),"   \n",
    ("Snowsight",               "Outil",            "#afa","#000"),"   \n",
    ("Tableau",                 "Outil",            "#afa","#000")
    )
with col2:
   st.video('https://youtu.be/JtPwHQJ25TA')
with col3:
   '[Github](https://github.com/snowflakecorp/frostbytes/tree/main/Department%20-%20Marketing%20Analytics)'


'''### 💸 Prédire le retour sur investissement marketing
1. Data engineering avec Snowpark Python : préparer des données qui représentent 10 ans d'investissements sur différents canaux de marketing afin de prédire quel canal offre le meilleur retour sur investissement. 
2. Data pipeline : Créer des tasks qui permettent d'automatiser les transformation de données
3. Data science avec Snowpark Python : créer un modèle pour identifier l'impact des canaux marketing sur le revenu (régression linéaire)
4. Accéder au modèle au travers d'une interface streamlit qui permet aux utilisateurs d'exécuter des analyses "what-if ?" : Quel serait l'impact d'un changement de dépenses en marketing sur les revenus pour les prochains mois ?
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Any",                     "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("Marketing",               "Données",          "#faa","#000"),"   \n",
    ("Snowpark python",         "Feature",          "#fea","#000"),"   \n",
    ("Streamlit",               "Outil",            "#afa","#000"),"   \n",
    ("Jupyter notebook",        "Outil",            "#afa","#000"),"   \n",
    ("Snowsight",               "Outil",            "#afa","#000"),"   \n"
    )
with col2:
   st.video('https://youtu.be/wleF5GZpiKo')
with col3:
   '[Quickstarts](https://quickstarts.snowflake.com/guide/getting_started_with_dataengineering_ml_using_snowpark_python/)'

'''### 📜 Analyser de larges corpus de texte avec le Natural Language Processing
1. Utiliser les stages pour stocker des données PDF dans snowflake de façon sécurisée
2. Créer des fonctions de Natural Language Processing en python pour extraire des informations de larges quantités de texte
3. Accéder aux PDF stockés sur les stages au travers d'URL sécurisées afin d'extraire les informations
4. Analyser et visualiser les informations dans snowsight
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Any",                     "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("PDF",                     "Données",          "#faa","#000"),"   \n",
    ("Snowpark python",         "Feature",          "#fea","#000"),"   \n",
    ("Snowsight",               "Outil",            "#afa","#000"),"   \n"
    )
with col2:
   st.video('https://youtu.be/8tr1q88NA7Y')
with col3:
   '[Blog : Simplify data ingestion with Snowpark Python file access](https://medium.com/snowflake/simplify-data-ingestion-with-snowpark-python-file-access-f2bc0e4cd887)'


'''### 📜 Analyse de sentiments de tweets en scala
1. Créer un dataframe en scala qui récupère des données depuis un fichier sur un stage
2. Créer une UDF en scala pour analyser le sentiment de tweets
3. Créer une procédure pour automatiser l'analyse de sentiments grace à notre UDF
'''
col1, col2, col3 = st.columns(([1,2,1]))
with col1:
   annotated_text(
    ("Any",                     "Industrie",        "#8ef","#000"),"   \n","   \n",
    ("Tweets",                  "Données",          "#faa","#000"),"   \n",
    ("Snowpark scala",          "Feature",          "#fea","#000"),"   \n",
    ("VS Code",                 "Outil",            "#afa","#000"),"   \n",
    ("Snowsight",               "Outil",            "#afa","#000"),"   \n"
    )
with col2:
   st.video('https://youtu.be/2vBiD3bH0Ts')
with col3:
   '[Quickstarts](https://quickstarts.snowflake.com/guide/getting_started_with_snowpark_scala/)'


