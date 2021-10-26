import streamlit as st

from predict_page import prediction_page
from titanic_insight import show_insight_page
from titanic_story import titanic_story_page


st.sidebar.header("1. Titanic Story and Insights")
st.sidebar.header("2. Predict Survival")

page = st.sidebar.selectbox("Choose", ('Titanic Story','Predict Survival'))

    
if page == "Titanic Story":
    titanic_story_page()
else:
    # page == 'Titanic Story':
    prediction_page()
