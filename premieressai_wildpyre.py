from turtle import color
import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
import plotly.express as px
import colorcet as cc
from bokeh.io import output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, LogColorMapper
from PIL import Image 
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html

import hydralit_components as hc
import hydralit as hy
from hydralit import HydraApp

import datetime



#make it look nice from the start
st.set_page_config(layout='wide',initial_sidebar_state='collapsed')

header = st.container()

with header :

    st.image("img/project_wildfire.png")
    st.subheader('Etude des causes de feux de forêt aux USA de 1992 à 2015')

# specify the primary menu definition

over_theme = {'txc_inactive': '#FFFFFF'}

menu_data = [
    {'icon': "fa fa-tree", 'label':"Introduction",'ttip':"Présentation du projet et des données"},
    {'icon': "fa fa-clipboard-list",'label':"Constats",'ttip':"Data analysis"},
    {'icon': "fa fa-fire",'label':"Explication des causes de feux de forêts", 'submenu':[{'id':'sous_menu_1','icon': "bi bi-flower3", 'label':"sous_menu_1"},{'id':'sous_menu_2','icon': "fa fa-bolt", 'label':"sous_menu_2"},{'id':'sous_menu_3','icon': "fa fa-user", 'label':"sous_menu_3"}],'ttip':"The truth is out there"},
    {'icon': "bi bi-signpost-split-fill",'label':"Préconisations",'ttip':"For a better life !"},
]

menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=False, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)


logo = Image.open('img/wildfire_pin.jpg')

profile = Image.open('img/wildfire_tree2.jpg')




# Ecrire dans le menu Introduction :
if menu_id == "Home" :

    st.markdown('')


# Ecrire dans le menu Introduction :
if menu_id == "Introduction":

    col1, col2 = st.columns( [0.8, 0.2])


    with col1:               # To display the header text using css style

        st.markdown(""" <style> .font {
        font-size:40px ; font-family: sans-serif;} 
        </style> """, unsafe_allow_html=True)

        st.markdown('<p class="font">Introduction</p>', unsafe_allow_html=True)    


    with col2:               # To display brand log
        st.image(logo, width=130 )
    
    st.write("Blablabla")    

    st.image(profile, width=700 )



#Affiche une barre d'info avec le nom de l'onglet après le clic sur l'onglet :
#st.info(f"{menu_id}")


sidebar = st.container()
container = st.container()
dataset = st.container()



with st.sidebar:

    st.markdown("<h1 style='text-align: center; color: black;'>Projet WildPYre</h1>", unsafe_allow_html=True)
 

    st.sidebar.markdown("--------")
    st.sidebar.markdown("Réalisé par :")
    st.sidebar.markdown("Océane Perrin | Paulo Machado Mendes | Lionel Laroche")
    st.sidebar.markdown("Formation Continue Data Analyst - Promotion Décembre 2021")


