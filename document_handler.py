from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document

def load_and_split_pdf(file):
    reader = PdfReader(file)
    raw_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            raw_text += text

    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = splitter.split_text(raw_text)
    return [Document(page_content=t) for t in texts]
