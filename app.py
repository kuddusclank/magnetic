import streamlit as st
import pages.data as md
st.set_page_config(
    page_title="GeoGenix Digital Datasheet",
    page_icon="👋",
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
st.write("# Welcome To GeoGenix ! 👋")
st.write("  ### Magnetic Survey Digital Datasheet")
st.markdown(
    """
   Welcome to Geogenix, your go-to resource for geophysical exploration and insights. 
   Our mission is to bridge the gap between theory and practice, providing geoscientists, 
   researchers, and enthusiasts with valuable information and tools. 
    ### Want  more tools?
    - Check out [GeoGenix HomePage](https://geogenix.000webhostapp.com/)
  
"""
)
def switching():
    st.balloons()

st.subheader("Magnetic Survey↭")
SurveyName = st.text_input("Traverse Name")
Longitude = st.number_input(label= "Logitude ", placeholder="Degree Decimal",format ="%0.5f")
Lattitude=st.number_input("Lattitude", placeholder="Degree Decimal",format ="%0.5f")
Elevation=st.number_input("Elevation", placeholder="Metres",min_value=0.00)
Interval_Spacing=st.number_input("Spacing Interval",min_value=1)
if(st.button("Proceed",type='primary')):
    md.SurveyName=SurveyName
    md.Longitude=Longitude
    md.Lattitude=Lattitude
    md.Intervals=Interval_Spacing
    md.Elevation=Elevation
    md.dataset={"Datapoint":[],"Reading 1":[],"Reading 2":[],"Reading 3":[], "Reading_Average":[],"Time":[],"Longitude":[],"Lattitude":[],"Elevation":[]}
    md.Station=0
    md.profile=0
    st.switch_page("pages/base.py")

    





