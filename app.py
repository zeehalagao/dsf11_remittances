import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st


def load_data():
    # Load the data
    data = pd.read_csv(
        "micro_world.csv",
        encoding='ISO-8859-1'
    )
    return data


def introduction():

    # Load photo
    st.image("1.png")
    st.image("2.png")
    st.image("4.png")
    

def fi_state_ph():
    st.image("5.png")
    st.image("6.png")
    st.image("7.png")
    st.image("8.png")
    st.image("9.png")
    st.image("10.png")
    st.image("11.png")
    st.image("13.png")
    st.image("12.png")
    
                    

def fi_state_worldwide():
    st.image("14.png")
    st.image("15.png")
    st.image("16.png")
    st.image("17.png")

def recommendations():
    st.image("18.png")
  


def the_team():
     st.image("19.png")


list_of_pages = [
    "Introduction",
    "Methodology",
    "What to do?",
    "Future Updates",
    "The Team"
]

st.sidebar.title(':scroll: Main Pages')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Introduction":
    introduction()

elif selection == "Methodology":
    fi_state_ph()

elif selection == "What to do?":
    fi_state_worldwide()

elif selection == "Future Updates":
    recommendations()

elif selection == "The Team":
    the_team()
