import streamlit as st

st.title("My Streamlit App")

user_input = st.text_input("Enter text:")

st.write(f"You entered: {user_input}")

