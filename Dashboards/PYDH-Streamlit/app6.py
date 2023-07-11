import streamlit as st

st.title("Containers")

main_container = st.container()

if "a_counter" not in st.session_state:
    st.session_state.a_counter = 0

if st.button("up"):
    main_container.write(st.session_state.a_counter)
    st.session_state.a_counter +=1

if st.button("reset"):
    st.session_state.a_counter = 0
