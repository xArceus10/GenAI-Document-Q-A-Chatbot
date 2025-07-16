# GenAI-Powered Document Q&A Chatbot

An interactive Streamlit app that lets you upload documents (PDF) and ask natural language questions. It uses LangChain, OpenAI, and FAISS for intelligent retrieval and answer generation.

##  Features
- LLM-based answers to uploaded documents
- LangChain + FAISS for semantic retrieval
- Streamlit front-end for easy interaction

## Tech Stack
- Python, Streamlit
- OpenAI GPT-3.5
- LangChain, FAISS
- PyPDF for PDF parsing

## How to Run

```bash
git clone https://github.com/your-username/genai-doc-chatbot.git
cd genai-doc-chatbot
pip install -r requirements.txt

# Add your OpenAI key
cp .env.example .env
# Edit .env and insert your key

streamlit run app.py
