from config import CHUNK_SIZE, CHUNK_OVERLAP
from langchain.text_splitter import RecursiveCharacterTextSplitter



from crawling import extract_text


def chunking_text(text:str):

    splitter=RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    
    return splitter.split_text(text)


