import streamlit as st
from groq import Groq

st.title("Free AI Chatbot")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

question = st.text_input("Enter your question")

if st.button("Ask AI"):
    if question:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": question}],
        )
        st.write(response.choices[0].message.content)