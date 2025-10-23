# view.py
import streamlit as st

def mostrar():
    st.set_page_config(page_title="Hello Streamlit", layout="wide")
    st.title("Hello from my-project 👋")
    st.write("Agora a saída aparece no browser, não no terminal.")