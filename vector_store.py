from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

def create_vector_store(docs):
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    return db
