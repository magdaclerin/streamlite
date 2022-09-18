import streamlit as st
import pandas as pd
import seaborn as sns
import time
import importlib
from PIL import Image

#Image loader
image = Image.open('movie.jpg')
image_icon = Image.open('icon.jpg')

#Page config
st.set_page_config(layout="wide", page_title='Projet cinéma- Wild Code School', page_icon=image_icon)

#Imports
url_imdb = "https://www.imdb.com/"
url_datasets = "https://datasets.imdbws.com/"
url_doc = "https://www.imdb.com/interfaces/"
df_films = pd.read_csv("https://raw.githubusercontent.com/SebastienTarres/Project/main/out.csv", sep = ",",index_col='Film_Id',low_memory=False,  na_values=["\\N","nan"])

#Sidebar
st.sidebar.success("Sélectionnez une page au dessus.")
st.sidebar.image(image)

#Content
st.title('Plateforme de recommandations de films basée sur le site IMDB 🎥')
#st.write("Projet d'étude réalisé par une équipe de 4 personnes durant le cursus de la formation Data Analyst à la Wild Code School.")
("👈 Cliquez sur le lien **'Système de recommendations de films'** dans le menu de gauche afin d'accéder à l'application de suggestions de films ou sur le lien **'Visualisation de données'** afin d'accéder aux graphiques de visualisations de données développés par notre équipe.")

st.subheader("Objectifs du projet :bulb:")
st.write(":arrow_right: Dans un premier temps, travailler sur les bases de données de la plateforme IMDB afin de faire ressortir des informations pertinentes via l'utilisation de graphiques adaptés.")
st.write(":arrow_right: Dans un second temps, utiliser le machine learning afin de développer un système de recommandations de films basée sur le choix de l'utilisateur.")

st.subheader("Vous désirez en savoir d'avantage sur la base IMDB ?")
st.write('''
    -   Visitez le [site officiel](https://www.imdb.com/) d'IMBD et immergez vous dans le monde cinématographique.
    -	Accédez aux [bases de données](https://datasets.imdbws.com/) utilisées dans la création de ce projet (au format CSV). 
    -	Ainsi qu'à [leurs documentations](https://www.imdb.com/interfaces/) respectives.
  '''
    )

#DataFrame
with st.expander("Vous pouvez cliquer ici afin d'accéder au dataset brut ⬇️"):
	st.write(df_films)


