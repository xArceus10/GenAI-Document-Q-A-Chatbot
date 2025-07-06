from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

def ask_question(db, question):
    llm = ChatOpenAI()
    chain = load_qa_chain(llm, chain_type="stuff")
    docs = db.similarity_search(question)
    return chain.run(input_documents=docs, question=question)
