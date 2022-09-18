import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

#Image loader
image_icon = Image.open('icon.jpg')



plt.rcParams["figure.facecolor"] = (0.0, 0.0, 0.0, 0.0) # transparence du fond
plt.rcParams["axes.facecolor"] = (0.0, 0.0, 0.0, 0.0) # transparence des axes
plt.rcParams["legend.edgecolor"] = (0.0, 0.0, 0.0, 0.0) # transparence legende
plt.rcParams["axes.edgecolor"] = "dimgrey" # couleurs axe
plt.rcParams["axes.labelcolor"] = "silver" # couleurs labels axe
plt.rcParams["axes.labelsize"] = 20 # taille labels axes
plt.rcParams["xtick.labelcolor"] = "silver"
plt.rcParams["ytick.labelcolor"] = "silver"

st.set_page_config(layout="wide",page_title='Data Visualisation', page_icon=image_icon)

st.title('Data Vizualisation')

# définir NA values
na_values = [r'\N','NAN','Nan','""']
# predefinir la taille des graphiques
plt.rcParams["figure.figsize"] = (12,6)

#import du fichier ####changer l'url
df_main = pd.read_csv("https://raw.githubusercontent.com/SebastienTarres/Project/main/out.csv", header=0, sep=",", low_memory=False, na_values= na_values)

# rajouts de colonnes nécessaires pour les stats:
df_main['Année_de_sortie'] = pd.to_datetime(df_main['Année_de_sortie'], format='%Y')
df_main['Année'] = df_main['Année_de_sortie'].dt.year
df_main['Decade'] = df_main['Année_de_sortie'].apply(lambda x: (x.year//10)*10)
df_main['Note_moyenne_arrondie'] = df_main['Note_moyenne'].astype(int)

df_main['Liste_acteurs_et_actrices']=df_main['Liste_acteurs_et_actrices'].apply(lambda list1: str(list1).replace('[','').replace(']',''))
df_main[['Actor_1', 'Actor_2', 'Actor_3', 'Actor_4','Actor_5','Actor_6','Actor_7','Actor_8','Actor_9','Actor_10']] = df_main['Liste_acteurs_et_actrices'].str.split(',', expand=True)

st.write("Notre projet a commencé par le nettoyage et l'analyse de la base de données IMDB. A celle-ci, nous avons extrait une sélection de films adaptée à notre client : un cinéma creusois dans le déclin.")
st.write("A partir de cette nouvelle base de données de plus de 52 000 films disponibles sur le marché français (hors catégorie adulte), nous avons pu réaliser des data visualisations. Cette page vous montrera une sélection des graphiques.")

col1, col2 = st.columns(2)

with col1:
	##GRAPH 1: Top 10 directeur le plus productifs
	df_director = df_main['Directeur'].value_counts().to_frame()
	df_director.drop('Inconnu', axis=0, inplace=True)
	df_director = df_director.reset_index()
	df_director = df_director.rename(columns={'Directeur': 'nombre_de_films', 'index':'directeur'})
	df_director_head = df_director.head(10)

	st.header("Top 10 des directeurs les plus productifs")

	barplotDirector = sns.barplot(data=df_director_head, x='directeur', y='nombre_de_films', color='darkcyan')
	#plt.title('Top 10 des directeurs les plus productifs')
	plt.xlabel("Directeur")
	plt.ylabel("Nombre de films")
	plt.xticks(rotation=45)
	st.pyplot(barplotDirector.figure, clear_figure=True)

	st.write("Ce graphique représente les 10 réalisateurs les plus productifs de notre sélection de films. Michael Curtis (1886-1962), avec plus de 80 films dans notre base de données, est considéré comme le réalisateur le plus important de Warner Bros. Il devance John Ford et Jesús Franco.")


with col2:
	##GRAPH 2: repartitions films par genre
	columns_genres_list = ['Action',
	       'Aventure', 'Animation', 'Biographie', 'Comédie', 'Crime', 'Drame',
	       'Famille', 'Romance', 'Thriller', 'Guerre', 'Western', 'Histoire']
	len(columns_genres_list)

	columns_genreCount_list = []
	for i in columns_genres_list:
	    columns_genreCount_list.append(df_main[i].sum())
	df_genres_count = pd.DataFrame(columns_genreCount_list)
	df_genres_count['Genres'] = columns_genres_list
	df_genres_count.rename(columns = {0:'Nombre_de_films'},inplace=True)
	df_genres_count = df_genres_count.sort_values(by='Nombre_de_films', ascending=False)

	st.header("Nombre de films produits par genre")

	barplotFilmGenre = sns.barplot(data=df_genres_count, x='Genres', y='Nombre_de_films', color='darkcyan')
	plt.ylabel("Nombre de films")
	#plt.title('Nombre de films produits par genre')
	plt.xticks(rotation=45)
	st.pyplot(barplotFilmGenre.figure, clear_figure=True)

	st.write("Notre sélection cinématographique comporte majoritairement des films de type Drame ou Comédie. Le choix des films proposés est le fruit de recherche sur la zone du Client fictif du département de 'la Creuse', qui se compose d'une population plutôt familiale")

# GRAPH 4:les top 10 de tous les films le plus vus et le mieux notés
st.header("Le top 10 des films les mieux notés")
st.write("Ce tableau nous présente les 10 films les mieux notés de notre base de données ainsi que le nombre de votes. le premier film atteint la note de 9.3/10 avec plus de 2.5 millions de votes.")
top_10_tot = df_main.sort_values(by=['Nombre_de_votes'], ascending=False)
top_note = top_10_tot.head(10)
top_note["Note"] = top_note["Note_moyenne"].astype('float')
top_note["Nombre de votes"] = top_note["Nombre_de_votes"].astype('Int64')
#top_note["Note"] = top_note["Note_moyenne"].astype('float').round(1)
top = top_note[['Titre', 'Note', 'Nombre de votes']]
#top = top_note[['Titre', 'Nombre de votes', 'Note']]
#st.dataframe(top)
# Styled
st.dataframe(top.style.format({'Note': '{:.1f}'}))


col1, col2 = st.columns(2)

with col1:
	##GRAPH 3: Répartition par nombre de vote
	# comptage de tous les films en fonction de la moyenne arrondie de votes (la repartition par genre reflète la tendance gnéénrale)
	df_round_average = df_main["Note_moyenne_arrondie"].value_counts()
	df_round_average = df_round_average.to_frame()
	df_round_average.reset_index(inplace=True)
	df_round_average.rename(columns={'index' : 'Moyenne', 'Note_moyenne_arrondie':'Nombre_de_votes'}, inplace=True)

	st.header("Répartition par nombre de votes")

	barplotVote = sns.barplot(data=df_round_average, x="Moyenne", y='Nombre_de_votes', color='darkcyan')
	plt.ylabel('Nombre de films')
	#plt.title('Répartition par nombre de votes')
	st.pyplot(barplotVote.figure, clear_figure=True)

	st.write("Une grande partie des films est au-dessus de la moyenne, la base de films sélectionnées est bien notée")


with col2:
	# GRAPH 5: Evolution du nombre de films produits dans le temps'
	st.header("Nombre de films par année de sortie")
	fig=plt.figure(figsize=(10,5))
	ax1 = fig.add_subplot(111)
	#ax2 = ax1.twinx()
	sns.histplot(data=df_main, x='Année', stat="count", color='darkcyan', bins=35, ax=ax1)
	ax1.set_ylabel('Nombre de films')
	#plt.title('Evolution du nombre de films produits dans le temps')
	#plt.xticks(rotation=60)
	st.pyplot(fig)

	st.write("Nous assistons à une augmanetation marquée du nombre de films au cours de l'histoire. Nous avons à notre disposition une bibliothèque de films toujours plus riche.")


col1, col2 = st.columns(2)

with col1:
	# GRAPH 6: évolution de la durée des films dans le temps
	st.header("Evolution de la durée des films")
	df = df_main
	plt.figure(figsize = (15,8))
	sns.lineplot(x = 'Année_de_sortie', y = 'Durée_en_minutes',data = df, color='darkcyan', ci=None, linewidth=3)
	plt.xlabel('Année')
	plt.ylabel('Durée')
	#plt.title('Durée des films')
	st.set_option('deprecation.showPyplotGlobalUse', False)
	st.pyplot()

	st.write("Nous voyons que la durée des films s'est allongée depuis la première sortie cinéma, la durée est passée de 80 min en moyenne à 120 min aujourd'hui.")

with col2:
	# GRAPH 7: Evolution du nombre de film par genre
	# repartition des films par genre et par année
	df_year_genre = df_main.groupby(by='Année').sum()
	df_year_genre.drop(columns=['Nombre_acteurs_et_actrices','Durée_en_minutes','Note_moyenne','Nombre_de_votes'], inplace=True)

	st.header("Evolution de la production de films")
	plt.figure(figsize = (15,8))
	sns.lineplot(x = 'Année', y = 'Drame',data = df_year_genre, label = 'drame', linewidth=5)
	sns.lineplot(x = 'Année', y = 'Comédie', data = df_year_genre,label = 'comédie', linewidth=5)
	sns.lineplot(x = 'Année', y = 'Crime',data = df_year_genre, label = 'crime', linewidth=5)
	plt.xlabel('Année')
	plt.ylabel('Nombre de films')
	plt.legend()
	#plt.title('Evolution du nombre de film par genre')
	st.pyplot()

	st.write("On observe une nette augmentation de la production de films pour ces 3 genres, surtout ces dernières années. Les 3 genres suivent la même tendance.")


