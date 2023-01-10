import streamlit as st

st.set_page_config(page_title="Snowflake Demo Catalog",page_icon="🏠",layout="wide")

st.title("Catalogue de démos de Snowflake❄️")

st.sidebar.info("Trouvez un asset en fonction de votre usage de la plateforme.")

annotated_text(
    "Les assets sont classés par persona et taggés en fonction de leur contenu :"
    ("Industrie",       "Industrie",        "#8ef","#000000"),
    ("Feature",         "Feature",          "#afa","#000000"),
    ("Snowsight",       "Front-end",        "#8ef","#000000")
)
"""
#### Chaque démo est présentée en vidéo, accompagnée de scripts SQL et/ou Python.
- 📄 __Analyste__ : Utilise Snowflake pour répondre à des questions. Intéressé par comment Snowflake résout des problèmes émanant des métiers.
- 🌍 __Data Engineer__ : Utilise Snowflake pour préparer des données afin qu'elles puissent être analysées. Intéressé par la facilité d'utilisation et l'optimisation de performance.
- ⚛️ __Data Scientist__ : Utilise Snowflake pour créer des modèles analytiques et prédictifs. Intéressé par l'accès centralisé à toutes les données nécessaires, la gouvernance des données et la création de modèles en plusieurs languages.


[contact](mailto:maxime.simon@snowflake.com)  
[source sur Github](https://github.com/sfc-gh-msimon/demo-catalog)
"""