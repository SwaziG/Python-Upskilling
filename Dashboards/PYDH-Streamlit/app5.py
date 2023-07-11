import streamlit as st

def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs/2.2046

def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg*2.2046

st.title("kg pound converter")

col1, buf, col2 = st.columns([2,1,2])
with col1:
    pounds = st.number_input("Pounds:", key="lbs",
                             on_change = lbs_to_kg)

with col2:
    kilograms = st.number_input("Kilograms:", key="kg",
                                on_change = kg_to_lbs)