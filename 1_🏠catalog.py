import streamlit as st

st.set_page_config(page_title="Snowflake Demo Catalog",page_icon="🏠",layout="wide")

st.title("Snowflake Demo Catalog ❄️")

st.sidebar.info("Choisissez la démo en fonction de la personne à qui vous allez présenter.")

st.markdown(
"""
#### Les démos sont classées par persona et par industrie.
#### Chaque démo est présentée en vidéo, accompagnée de scripts SQL et/ou Python quand c'est possible.
- 📄 Analyste : Utilise Snowflake pour répondre à des questions. Intéressé par comment Snowflake résout des problèmes émanant des métiers.
- 🌍 Data Engineer : Utilise Snowflake pour préparer des données afin qu'elles puissent être analysées. Intéressé par la facilité d'utilisation et l'optimisation de performance.
- ⚛️ Data Scientist : Utilise Snowflake pour créer des modèles analytiques et prédictifs. Intéressé par l'accès centralisé à toutes les données nécessaires, la gouvernance des données et la création de modèles en plusieurs languages.

contact : maxime.simon@snowflake.com
[source sur Github](https://github.com/sfc-gh-msimon/demo-catalog)
""")