import streamlit as st
import pandas as pd
import seaborn as sns

import matplotlib
import matplotlib.pyplot as plt


st.set_page_config(layout="wide")

st.title('Hello Wilders, welcome to my first application!')

st.write("I enjoy to discover stremalit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
cond = df_cars['continent'] == ' Europe.'
df_Europe = df_cars[cond]
cond = df_cars['continent'] == ' Japan.'
df_Japan = df_cars[cond]
cond = df_cars['continent'] == ' US.'
df_US = df_cars[cond]
columns_list = df_cars.columns
df_cars['year'] = df_cars['year'].astype(str)

year_continent = pd.crosstab(df_cars['continent'], df_cars['year']).T
year_continent = year_continent.rename({'continent': 'index'})


###


with st.container():

    option = st.selectbox(
        'Please select the geographic area :',
        ('- show all - ', 'Europe', 'Japan', 'US'))

    col1, col2 = st.columns(2, gap="small")

    with col1:
        #st.header(option)
        if option == '- show all - ':
            st.write(df_cars)
        elif option == 'Europe':
            st.write(df_Europe)
        elif option == 'Japan':
            st.write(df_Japan)
        elif option == 'US':
            st.write(df_US)

    with col2:
        #st.header("show all", option)
        if option == '- show all - ':
            # with plt.style.context('dark_background'):
            plt.rcParams["figure.figsize"] = (10, 7)
            plt.rcParams["figure.facecolor"] = (0.0, 0.0, 0.0, 0.0)
            #plt.rcParams["figure.edgecolor"] = "#0E1117" - marche pas ( changer le fond de mon bar)
            plt.rcParams["axes.facecolor"] = (0.0, 0.0, 0.0, 0.0)
            plt.rcParams["axes.edgecolor"] = "dimgrey"
            plt.rcParams["axes.labelcolor"] = "silver"
            plt.rcParams["axes.labelsize"] = 20
            plt.rcParams["xtick.labelcolor"] = "silver"
            plt.rcParams["ytick.labelcolor"] = "silver"

            tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
                ['mpg', 'cylinders', 'cubicinches', 'hp', 'weightlbs', 'time-to-60'])

            with tab1:
                fig = plt.figure()

                sns.histplot(x='mpg', data=df_cars,  color="lightcoral")
                plt.xlabel("miles per gallon")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab2:
                fig = plt.figure()

                sns.histplot(x='cylinders', data=df_cars, color="lightcoral")
                plt.xlabel("number of cylinders")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab3:
                fig = plt.figure()

                sns.histplot(x='cubicinches', data=df_cars, color="lightcoral")
                plt.xlabel("cubicinches")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab4:
                fig = plt.figure()

                sns.histplot(x="hp", data=df_cars, color="lightcoral")
                plt.xlabel("hp")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab5:
                fig = plt.figure()

                sns.histplot(x='weightlbs', data=df_cars,  color="lightcoral")
                plt.xlabel("weightlbs")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab6:
                fig = plt.figure()

                sns.histplot(x='time-to-60', data=df_cars,  color="lightcoral")
                plt.xlabel("time-to-60")
                plt.ylabel("count")
                st.pyplot(fig)



        elif option == 'Europe':
            # with plt.style.context('dark_background'):
            plt.rcParams["figure.figsize"] = (10, 7)
            plt.rcParams["figure.facecolor"] = (0.0, 0.0, 0.0, 0.0)
            #plt.rcParams["figure.edgecolor"] = "#0E1117" - marche pas ( changer le fond de mon bar)
            plt.rcParams["axes.facecolor"] = (0.0, 0.0, 0.0, 0.0)
            plt.rcParams["axes.edgecolor"] = "dimgrey"
            plt.rcParams["axes.labelcolor"] = "silver"
            plt.rcParams["axes.labelsize"] = 20
            plt.rcParams["xtick.labelcolor"] = "silver"
            plt.rcParams["ytick.labelcolor"] = "silver"

            tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
                ['mpg', 'cylinders', 'cubicinches', 'hp', 'weightlbs', 'time-to-60'])

            with tab1:
                fig = plt.figure()

                sns.histplot(x='mpg', data=df_Europe,  color="lightcoral")
                plt.xlabel("miles per gallon")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab2:
                fig = plt.figure()

                sns.histplot(x='cylinders', data=df_Europe, color="lightcoral")
                plt.xlabel("number of cylinders")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab3:
                fig = plt.figure()

                sns.histplot(x='cubicinches', data=df_Europe, color="lightcoral")
                plt.xlabel("cubicinches")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab4:
                fig = plt.figure()

                sns.histplot(x="hp", data=df_Europe, color="lightcoral")
                plt.xlabel("hp")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab5:
                fig = plt.figure()

                sns.histplot(x='weightlbs', data=df_Europe,  color="lightcoral")
                plt.xlabel("weightlbs")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab6:
                fig = plt.figure()

                sns.histplot(x='time-to-60', data=df_Europe,  color="lightcoral")
                plt.xlabel("time-to-60")
                plt.ylabel("count")
                st.pyplot(fig)

        elif option == 'Japan':
            # with plt.style.context('dark_background'):
            plt.rcParams["figure.figsize"] = (10, 7)
            plt.rcParams["figure.facecolor"] = (0.0, 0.0, 0.0, 0.0)
            #plt.rcParams["figure.edgecolor"] = "#0E1117" - marche pas ( changer le fond de mon bar)
            plt.rcParams["axes.facecolor"] = (0.0, 0.0, 0.0, 0.0)
            plt.rcParams["axes.edgecolor"] = "dimgrey"
            plt.rcParams["axes.labelcolor"] = "silver"
            plt.rcParams["axes.labelsize"] = 20
            plt.rcParams["xtick.labelcolor"] = "silver"
            plt.rcParams["ytick.labelcolor"] = "silver"

            tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
                ['mpg', 'cylinders', 'cubicinches', 'hp', 'weightlbs', 'time-to-60'])

            with tab1:
                fig = plt.figure()

                sns.histplot(x='mpg', data=df_Japan,  color="lightcoral")
                plt.xlabel("miles per gallon")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab2:
                fig = plt.figure()

                sns.histplot(x='cylinders', data=df_Japan, color="lightcoral")
                plt.xlabel("number of cylinders")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab3:
                fig = plt.figure()

                sns.histplot(x='cubicinches', data=df_Japan, color="lightcoral")
                plt.xlabel("cubicinches")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab4:
                fig = plt.figure()

                sns.histplot(x="hp", data=df_Japan, color="lightcoral")
                plt.xlabel("hp")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab5:
                fig = plt.figure()

                sns.histplot(x='weightlbs', data=df_Japan,  color="lightcoral")
                plt.xlabel("weightlbs")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab6:
                fig = plt.figure()

                sns.histplot(x='time-to-60', data=df_Japan,  color="lightcoral")
                plt.xlabel("time-to-60")
                plt.ylabel("count")
                st.pyplot(fig)

        elif option == 'US':
            # with plt.style.context('dark_background'):
            plt.rcParams["figure.figsize"] = (10, 7)
            plt.rcParams["figure.facecolor"] = (0.0, 0.0, 0.0, 0.0)
            #plt.rcParams["figure.edgecolor"] = "#0E1117" - marche pas ( changer le fond de mon bar)
            plt.rcParams["axes.facecolor"] = (0.0, 0.0, 0.0, 0.0)
            plt.rcParams["axes.edgecolor"] = "dimgrey"
            plt.rcParams["axes.labelcolor"] = "silver"
            plt.rcParams["axes.labelsize"] = 20
            plt.rcParams["xtick.labelcolor"] = "silver"
            plt.rcParams["ytick.labelcolor"] = "silver"

            tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
                ['mpg', 'cylinders', 'cubicinches', 'hp', 'weightlbs', 'time-to-60'])

            with tab1:
                fig = plt.figure()

                sns.histplot(x='mpg', data=df_US,  color="lightcoral")
                plt.xlabel("miles per gallon")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab2:
                fig = plt.figure()

                sns.histplot(x='cylinders', data=df_US, color="lightcoral")
                plt.xlabel("number of cylinders")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab3:
                fig = plt.figure()

                sns.histplot(x='cubicinches', data=df_US, color="lightcoral")
                plt.xlabel("cubicinches")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab4:
                fig = plt.figure()

                sns.histplot(x="hp", data=df_US, color="lightcoral")
                plt.xlabel("hp")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab5:
                fig = plt.figure()

                sns.histplot(x='weightlbs', data=df_US,  color="lightcoral")
                plt.xlabel("weightlbs")
                plt.ylabel("count")
                st.pyplot(fig)

            with tab6:
                fig = plt.figure()

                sns.histplot(x='time-to-60', data=df_US,  color="lightcoral")
                plt.xlabel("time-to-60")
                plt.ylabel("count")
                st.pyplot(fig)

with st.container():
    st.write("models by year")
    chart_data = pd.DataFrame(
        year_continent,
        columns=[' Europe.', ' Japan.', ' US.'])

    st.line_chart(chart_data)

