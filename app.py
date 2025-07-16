import streamlit as st
from document_handler import load_and_split_pdf
from vector_store import create_vector_store
from qa_chain import ask_question
from dotenv import load_dotenv
import os

load_dotenv()

# --- Page config ---
st.set_page_config(
    page_title="GenAI Doc Q&A Chatbot",
    page_icon="📄",
    layout="centered"
)

# --- Header ---
st.markdown("## 📄 GenAI Document Q&A Chatbot")
st.markdown("Ask questions from any uploaded PDF using AI!")

# --- Upload and Question ---
col1, col2 = st.columns([2, 3])

with col1:
    uploaded_file = st.file_uploader("Upload your PDF:", type=["pdf"])

with col2:
    question = st.text_input("Ask a question:")

# --- Process ---
if uploaded_file and question:
    with st.spinner("Reading and thinking.."):
        docs = load_and_split_pdf(uploaded_file)
        db = create_vector_store(docs)
        answer = ask_question(db, question)

    st.success("Answer Generated:")
    st.markdown(f"### 💬 {answer}")
elif uploaded_file and not question:
    st.info("✏️ Enter a question about the uploaded PDF.")
elif question and not uploaded_file:
    st.warning("📄 Please upload a PDF file first.")

# --- Footer ---
st.markdown("---")
