import streamlit as st

# Title of the app
st.title("Welcome to your ai chatbot")

import re

chatbot_response(user_inport):
patterns = [
    (r"hi|hello|hey","Hello! how can i help you today?"),
    (r"my name is (\w+)","nice to meet you ,{}!)
]

for pattern,response in pattern:
    match = re.search(pattern,user_inport,re.IGNORRECASE)
    if match:
        if callable(response):
            return response(match)
