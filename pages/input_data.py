import streamlit as st
from pages.data import *
import pandas as pd

st.set_page_config(
    page_title="GeoGenix",
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

st.write("### Datapoint ",profile)
longitude = st.number_input("Longitude",key='longitude')
lattitude = st.number_input("Lattitude",key='lattitude')
elevation = st.number_input("Elevation",key='elevation')
z1 = st.number_input("Reading 1",key='z1')
z2 = st.number_input("Reading 2",key='z2')
z3 = st.number_input("Reading 3",key='z3')

def clear_all_text_inputs():

    add_data(z1,z2,z3,longitude,lattitude,elevation)
    st.session_state['z1'] = None  # Clear inphase text input
    st.session_state['z2'] = None  # Clear outphase number input
    st.session_state['z3'] = None  # Clear outphase number input
    st.session_state['longitude'] = None  # Clear longitude number input
    st.session_state['lattitude'] = None  # Clear latitude number input
    st.session_state['elevation'] = None  # Clear elevation number input

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

col1, col2, col3 = st.columns(3)
with col1:
    insert_button = st.button("Add Dataset", type='primary', key='insert_button', on_click=clear_all_text_inputs)
with col2:
    if (st.button("Datasheet View")):
        st.switch_page("pages/export_data.py")
with col3:
    if (st.button("Close Reading")):
        CloseDp()
        st.switch_page("pages/close_base.py")


