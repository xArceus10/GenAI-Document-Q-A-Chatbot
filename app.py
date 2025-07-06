import streamlit as st
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.docstore.document import Document
from PyPDF2 import PdfReader
import os

st.title("GenAI Document Q&A Chatbot")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
question = st.text_input("Ask a question about the document:")

if uploaded_file and question:
    pdf_reader = PdfReader(uploaded_file)
    raw_text = ""
    for page in pdf_reader.pages:
        raw_text += page.extract_text()

    # Split text
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = splitter.split_text(raw_text)
    docs = [Document(page_content=t) for t in texts]

    # Embedding & vector DB
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)

    # Run QA chain
    llm = ChatOpenAI()
    chain = load_qa_chain(llm, chain_type="stuff")
    docs = db.similarity_search(question)
    response = chain.run(input_documents=docs, question=question)

    st.markdown("**Answer:**")
    st.write(response)
