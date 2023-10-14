import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.write("""
# World Records Of Covid 19 

Shown are the Continents and Countries of **Active Cases and Death Rates**


**This Data was been obtained from Kaggle**

""")






df = pd.read_csv("country_wise_latest.csv")

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)




st.sidebar.header(" *Input  Features BY Countries* ")



#OBTAINING DATA BY COUNTRIES

unique_countries = df["Country/Region"].unique()
default_select_con = unique_countries[0]
selected_countries = st.sidebar.multiselect("OBTAIN BY COUNTRIES", unique_countries, default_select_con)



df_selected_coutries = df[df["Country/Region"].isin(selected_countries)]





#OBTAINING DATA BY WHO REGION/CONTINENTS
st.sidebar.header(" *Input Features BY WHO Region*")


unique_region = df["WHO Region"].unique()
default_select =unique_region[0]
selected_continents = st.sidebar.multiselect("WHO Region", unique_region, default=default_select)



df_selected_region = df[df["WHO Region"].isin(selected_continents)]








st.header("Displayed Countries Of Continents By WHO")
st.write("There are ", str(len(df["Country/Region"].unique())), " Country on this data obtained from Kaggle and ", str(len(df["WHO Region"].unique())), " different Continents of WHO Region" )




st.write(df.head(100))



#SELECTED COUNTRIES
st.write("""
## DATA OBTAINED BY SELECTING OF COUNTRIES

""")
st.write("Data Dimension: ", str(df_selected_coutries.shape[0]) + " rows and " + str(df_selected_coutries.shape[1]) + " columns" )



st.write(df_selected_coutries)





#SELECTED WHO REGION/CONTINENTS
st.write("""
## DATA OBTAINED BY SELECTING OF WHO REGION/CONTINENTS

""")
st.write("Data Dimension: ", str(df_selected_region.shape[0]) + " rows and " + str(df_selected_region.shape[1]) + " columns" )

st.write(df_selected_region)





















st.header('Data Visualization')


st.set_option('deprecation.showPyplotGlobalUse', False)



st.title(f'Visualization of all  Deaths on all Region')
st.scatter_chart(df["Deaths"])


