import streamlit as st

file_path = './assets/help.md'
with open(file_path, 'r') as file:
    content = file.read().strip()  # Read and strip any extra whitespace
    st.markdown(content)
