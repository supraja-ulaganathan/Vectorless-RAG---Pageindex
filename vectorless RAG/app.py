import streamlit as st
from transformers import pipeline

# Load the model once
generator = pipeline("text2text-generation", model="google/flan-t5-large")

# Streamlit UI
st.title("Ask the PDF Model")

query = st.text_input("Enter your question:")

if query:
    result = generator(query, max_length=256)
    st.write("🧠 Answer:")
    st.write(result[0]["generated_text"])
