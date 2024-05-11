import streamlit as st
from pages.data import *
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Base Reading",
    page_icon="🌍",
    initial_sidebar_state="collapsed"
)



st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
st.write("# 🌍 GeoGenix")
st.write("## Survey Metadata")
st.write("Name: ",SurveyName)
st.write("Longitude: ",Longitude,"    Lattitude: ",Lattitude,"Elevation :",Elevation)


st.divider()

st.write("### Base (Opening Record)")
longitude = st.number_input("Longitude",key='longitude')
lattitude = st.number_input("Lattitude",key='lattitude')
elevation = st.number_input("Elevation",key='elevation')
z1 = st.number_input("Reading 1",key='z1')
z2 = st.number_input("Reading 2",key='z2')
z3 = st.number_input("Reading 3",key='z3')
z4 = st.number_input("Reading 4",key='z4')

st.markdown("""
            <style>
                div[data-testid="column"] {
                    width: fit-content !important;
                    flex: unset;
                }
                div[data-testid="column"] * {
                    width: fit-content !important;
                }
            </style>
            """, unsafe_allow_html=True)


if (st.button("Proceed")):
    basemap("Base Opening",z1,z2,z3,z4,Longitude,Lattitude,Elevation)
    StartDP()
    st.switch_page("pages/input_data.py")



