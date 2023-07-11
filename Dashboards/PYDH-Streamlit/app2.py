import streamlit as st

def clean_text(text):
    text = text.replace("`", "").replace("-\n", "").replace("\n"," ").strip()
    return(text)

st.title("Lesson 01.02: Intro to Layouts and Images")

#st.sidebar.image("Location of image")

st.sidebar.header("Options")

text = st.sidebar.text_area("Paste Text Here")

button1 = st.sidebar.button("Clean Text")
if button1:
    col1, col2 = st.columns(2)
    col1_expander = col1.expander("Expand Original Text")
    with col1_expander:
        col1_expander.header("Original Text")
        col1_expander.write(text)

    clean = clean_text(text)

    col2_expander = col2.expander("Expand Cleaned Text")
    with col2_expander:
        col2_expander.header("Cleaned Text")
        col2_expander.write(text)

st.header("Lets continue with the page")