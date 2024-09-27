import streamlit as st
import pandas as pd
from src.agents.messages import MessageHandler

handler = MessageHandler()
messages = handler.get_messages()
df = pd.DataFrame(data=messages)

st.header("Dialogen")
st.write("Here a table of all the user/assistant interactions (function calling included)")
st.table(df)