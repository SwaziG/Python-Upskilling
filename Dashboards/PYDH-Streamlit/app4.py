import streamlit as st

st.title("Session State")
# "st.session_state object:", st.session_state

if 'a_counter' not in st.session_state:
    st.session_state['a_counter'] = 0

if "boolean" not in st.session_state:
    st.session_state.boolean = False

st.write(st.session_state)

st.write("Counter = ", st.session_state["a_counter"])
st.write("Boolean = ", st.session_state.boolean)

for the_key in st.session_state.keys():
    st.write(the_key)

for the_values in st.session_state.values():
    st.write(the_values)

for item in st.session_state.items():
    item

button1 = st.button("Update State")
"before pressing button", st.session_state
if button1:
    st.session_state['a_counter'] += 1
    st.session_state.boolean = not st.session_state.boolean
    "After pressing button", st.session_state

# for key in st.session_state.keys():
#     del st.session_state[key]

