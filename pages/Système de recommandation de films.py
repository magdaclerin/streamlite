# 31/08/2022
# reste à faire : -  corriger les errors d'affichage (fonction recherche() )
#                   - corriger la fin (bouton qui fait appel à la fonction recherche() à nouveau )

import streamlit as st
import pandas as pd

from sklearn.neighbors import NearestNeighbors

from sklearn.preprocessing import StandardScaler
import unidecode

import re
from PIL import Image

#Image loader
image_icon = Image.open('icon.jpg')
st.set_page_config(page_title='Système de recommendation', page_icon=image_icon)


###
# DECLARATIONS : TABLEAUX / FONCTIONS / FONCTIONS GLOBALES
# ---------------------------------------
###

df_film = pd.read_csv("https://raw.githubusercontent.com/SebastienTarres/Project/main/out.csv", sep = ",",index_col='Film_Id',low_memory=False,  na_values=["\\N","nan"])

# variables globales:
title = ""

# fonction du nettoyage pour les str
def cleanup(name):
    name = unidecode.unidecode(name)  # remove accent
    name = re.sub(r'[^\w\s]', ' ', name)  # remove punctuation
    name = name.casefold().strip()  # lower and remove front and back space
    name = re.sub(' +', ' ', name)  # remove dupliacte spaces
    return name


# ajout d'une colonne avec titre "nettoyés"
df_film['TitreCleanedUp'] = df_film.Titre.apply(cleanup)

# MODELE ML

X = df_film.select_dtypes("number")  # selection de tous les numériques
scaler = StandardScaler()
scaler.fit(X)  # standardisation des données
X_scaled = pd.DataFrame(scaler.transform(X), index=X.index, columns=X.columns)
model = NearestNeighbors()  # déclaration du modèle
model.fit(X_scaled)


def rechecherFilmProche(movie):  # fonction recherche des films

    film_concerne = X_scaled.loc[movie]  # recherche du film dans X et affichage
    neigh_dist, neigh_mov = model.kneighbors(film_concerne, n_neighbors=6)  # recherche des X plus proches /
    # selection du nombre de neighbors
    film_proche = neigh_mov[0][1:]
    resultat_film_proche = df_film.iloc[film_proche]
    return resultat_film_proche

def recherche():
    # etape 2: recherche de l'index (tconst/movieID) de ce film via lower case
    nom_recherche = title
    index_recherche = df_film[df_film['TitreCleanedUp'] == nom_recherche].index.tolist()
    rows_count = len(index_recherche)

    # 1er cas - le titre exacte trouvé -> affichage de resultats
    if rows_count == 1 :
        resultat_film_proche = rechecherFilmProche(index_recherche)
        result = resultat_film_proche[['Titre', 'Année_de_sortie']]
        st.write('Voici les films recommandés pour vous : ')
        return result

    elif rows_count < 1 :
        print('Desolé pas de resultat pour votre recherche!')
        resultat_possible = df_film[df_film['TitreCleanedUp'].str.contains(nom_recherche)]
        rows_count_resultat = len(resultat_possible)
        if rows_count_resultat > 0 :
            st.write('Desolé pas de résultat pour votre recherche!')
            st.write('Voici les titres disponibles contenant le mot "', nom_recherche, '" :')
            result = resultat_possible[['Titre', 'Année_de_sortie']]
            return result
            # option pour choisir l'un des titres suggérés
        else :
            st.write('Verifiez le titre de ton film!')
            return None
    else :
        st.write("Plus d'un resultat trouvé avec ", nom_recherche, ' :')
        resultat_possible = df_film[df_film['TitreCleanedUp'].str.contains(nom_recherche)]
        result = resultat_possible
        return result

###
### AFFICHAGE SUR SITE
# ---------------------------------------
###

st.title('Partie II - Machine Learning')

st.write("Bienvenue dans notre système de recommendation ! ")

title = st.text_input('Veuillez saisir le titre du film: ')

if title:
    title = cleanup(title)
    df_recherche = recherche()
    df_recherche = df_recherche.reset_index() # les résultats de la fonction spnt stockés sous forme de la df
    try:
        for i in range(df_recherche.shape[0]): # pour chaque ligne de la df_recherche ... 1. créer un bouton avec le résultat / 2. appeler la fonction "recherche" à nouveau, avec comme parametre la ligne de la df [i]:
            st.button(label=df_recherche['Titre'].iloc[i]+"\n"+"("+str(df_recherche['Année_de_sortie'].iloc[i])+")")
            condition = df_film['TitreCleanedUp'] == df_recherche['TitreCleanedUp'].iloc[i]
            condition2 = df_film['Année_de_sortie'] == df_recherche['Année_de_sortie'].iloc[i]
            st.write(df_film[condition & condition2]) # à cet étape le bouton retourne la ligne de la df concernée - mettre à la place l'appel de la fonction (recherche)
    except AttributeError:
        pass


#%%
