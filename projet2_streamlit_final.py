# 31/08/2022
# reste à faire : -  corriger les errors d'affichage (fonction recherche() )
#                   - corriger la fin (bouton qui fait appel à la fonction recherche() à nouveau )

import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import unidecode
import re
import webbrowser

###
# DECLARATIONS : TABLEAUX / FONCTIONS / VAR GLOBALES
# ---------------------------------------
###

df_film = pd.read_csv("final_table_.csv", sep=",", index_col='Film_Id', low_memory=False, na_values=["\\N", "nan"])
df_film = df_film.drop(columns=['Nombre_acteurs_et_actrices'])


# fonction du nettoyage pour les str
def cleanup(name):
    name = unidecode.unidecode(name)  # remove accent
    name = re.sub(r'[^\w\s]', ' ', name)  # remove punctuation
    name = name.casefold().strip()  # lower and remove front and backspace
    name = re.sub(' +', ' ', name)  # remove duplicate spaces
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


def recherche(title):
    # récupérer le titre str saisi
    index_recherche = df_film[df_film['TitreCleanedUp'] == title].index.tolist()
    rows_count = len(index_recherche)

    # 1er cas - le titre exact trouvé → affichage de résultats
    if rows_count == 1:
        resultat_film_proche = rechecherFilmProche(index_recherche)
        st.write('Voici les films recommandés pour vous : ')
        for i in range(resultat_film_proche.shape[0]):
            if st.button(label=resultat_film_proche['Titre'].iloc[i] + "\n" + "(" + str(
                    resultat_film_proche['Année_de_sortie'].iloc[i])
                               + " dir. " + str(resultat_film_proche['Directeur'].iloc[i]) + ")"):
                # film_index = resultat_film_proche.index[i]
                url = 'https://www.streamlit.io/'
                webbrowser.open_new_tab(url)

    #   cas 2 Plusieurs résultats disponibles contenant le mot recherché
    elif rows_count < 1:
        resultat_possible = df_film[df_film['TitreCleanedUp'].str.contains(title)]
        rows_count_resultat = len(resultat_possible)
        if rows_count_resultat > 0:
            st.write('Plusieurs résultats disponibles contenant le mot "', title, '" :')
            for i in range(resultat_possible.shape[0]):
                if st.button(label=resultat_possible['Titre'].iloc[i] + "\n" + "(" + str(
                        resultat_possible['Année_de_sortie'].iloc[i])
                                   + " dir. " + str(resultat_possible['Directeur'].iloc[i]) + ")"):
                    recherche(cleanup(resultat_possible['Titre'].iloc[i]))
            # option pour choisir l'un des titres suggérés

        # cas 3 - pas de resultats
        else:
            result = 'Verifiez le titre de ton film!'
            return st.write(result)
    else:

        resultat_possible = df_film[df_film['TitreCleanedUp'].str.contains(title)]
        st.write("Plus d'un résultat trouvé avec ", title, ' :')
        for i in range(resultat_possible.shape[0]):
            if st.button(label=resultat_possible['Titre'].iloc[i] + "\n" + "(" + str(
                    resultat_possible['Année_de_sortie'].iloc[i])
                               + " dir. " + str(resultat_possible['Directeur'].iloc[i]) + ")"):
                recherche(cleanup(resultat_possible['Titre'].iloc[i]))
        return None


###
### AFFICHAGE SUR SITE
# ---------------------------------------
###

st.title('Partie II - Machine Learning')

st.write("Bienvenue dans notre système de recommendation ! ")

title = st.text_input('Veuillez saisir le titre du film: ')

if title:
    title = cleanup(title)  # nettoyer le titre
    df_recherche = recherche(title)  # faire sortir les résultats sous forme de la df
