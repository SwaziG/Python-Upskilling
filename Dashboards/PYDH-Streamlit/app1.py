import streamlit as st

st.title("Streamlit Tutorial App")
st.write("This is my new app")
button1 = st.button("Click Me")

if button1:
    st.write("Button Clicked, well done!")

like = st.checkbox("Is this cool?")

button2 = st.button("Submit")

if button2:
    if like:
        st.write("Thanks, I appreciate that")
    else:
        st.write("You Suck!")

st.header("Start of Radio Button Section")

animal = st.radio("What animal do you like most?",
                   ("Lions", "Tigers", "Bears"))

button3 = st.button("Submit Animal")
if button3:
    if animal == "Lions":
        st.write("RWR!")
    elif animal == "Tigers":
        st.write("GRRR!")
    elif animal == "Bears":
        st.write("Roar!")
    

st.header("Start of Radio SelectBox Section")

animal2 = st.selectbox("What animal do you like most?",
                   ("Lions", "Tigers", "Bears"))

button4 = st.button("Submit Animal 2")
if button4:
    if animal2 == "Lions":
        st.write("RWR!")
    elif animal2 == "Tigers":
        st.write("GRRR!")
    elif animal2 == "Bears":
        st.write("Roar!")

st.header("Start of Multiselect Section")

options = st.multiselect("What animals do you like?",["Lion","Tiger","Bear"])

button5 = st.button("Print Animals")

if button5:
    st.write(options)

st.header("Start of the Slider Section")

epochs_num = st.slider("How many epochs?", 1,100, 10)
if st.button("Slider Button"):
    st.write(epochs_num)

st.header("Start of Text Input Section")
user_text = st.text_input("What is your favorite Book?", "Pooping for Dummies")
if st.button("Text Button"):
    st.write(user_text)

user_num = st.number_input("What is your favorite number?")
if st.button("Number Button"):
    st.write(user_num)

st.header("Start of the Text Area:")

def run_sentiment_analysis(txt):
    st.write(f"Character Count = {len(txt)}")

txt = st.text_area('Please input your story:','''This is an example that can be manipulated''')
st.write('Sentiment:', run_sentiment_analysis(txt))