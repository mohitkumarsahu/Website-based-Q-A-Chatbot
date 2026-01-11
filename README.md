# Website-based Q&A Chatbot

## Project Overview
This project is a **Website-based Question & Answer (Q&A) Chatbot** that allows users to input a website URL, index its content, and ask natural language questions based strictly on the information available on that website.


The system crawls the webpage, extracts and cleans textual content, converts it into semantic embeddings, stores them in a vector database, and retrieves the most relevant content chunks to generate accurate, context-aware answers using a Large Language Model (LLM).

It demonstrates implementation of **Retrieval-Augmented Generation (RAG)** principles.

---

## Project Structure
Website-QA-Chatbot/
│
├── __pycache__/              # Python cache files (auto-generated)
│
├── data/                     # Data storage directory
│   ├── faiss.index          # FAISS vector database index
│   └── metadata.json        # Metadata for indexed chunks
│
├── app.py                    # Main Streamlit application
├── config.py                 # Configuration settings and constants
├── crawling.py               # Web scraping and text extraction
├── embeddings.py             # Embedding generation and FAISS indexing
├── load_index.py             # FAISS index and metadata loading
├── qa.py                     # Question answering and LLM integration
├── text_processing.py        # Text chunking functionality
│
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

---

## Architecture Explanation

1. **User Interface (Streamlit)**
   - Accepts website URLs
   - Provides a chat-based Q&A interface

2. **Web Crawling & Text Extraction**
   - Fetches HTML content
   - Removes non-relevant tags
   - Extracts clean text and page title

3. **Text Chunking**
   - Splits content into overlapping chunks

4. **Embedding Generation**
   - Converts text chunks into vectors

5. **Vector Storage**
   - Stores embeddings in a FAISS index
   - Saves metadata locally

6. **Retrieval**
   - Performs similarity search using cosine similarity

7. **Answer Generation**
   - Generates responses strictly from retrieved context

---

## Frameworks and Libraries Used

- **Streamlit** – UI framework
- **LangChain** – Text splitting utilities
- **FAISS** – Vector similarity search
- **Sentence-Transformers** – Embedding generation
- **Hugging Face Transformers** – LLM inference
- **BeautifulSoup** – HTML parsing
- **Requests** – HTTP requests

---

## Large Language Model (LLM)

**Model:** `google/flan-t5-small`

**Reason for Selection:**
- Lightweight and efficient
- Optimized for instruction-based tasks
- Suitable for local execution

---

## Vector Database

**Database:** FAISS 

**Why FAISS?**
- Fast similarity search
- Easy local setup
- No external dependencies

---

## Embedding Strategy

- **Model:** `all-MiniLM-L6-v2`
- Embeddings are normalized
- Uses cosine similarity
- Same model used for indexing and querying

---

## Setup and Run Instructions

### Prerequisites
- Python 3.9+
- pip

### Installation
```bash
pip install -r requirements.txt
```

### Run Application
```bash
streamlit run app.py
```

### Usage
1. Enter website URL
2. Click **Index Website**
3. Ask questions related to the site

---

## Assumptions

- Website content is publicly accessible
- Content is primarily text-based
- Single-page indexing only

---

## Limitations

- No multi-page crawling
- Local-only vector storage
- Basic prompt handling

---

## Future Improvements

- Multi-page crawling
- Persistent vector storage
- Improved UI and answer formatting
- Production-grade deployment

---

## Conclusion

This project demonstrates a practical and modular implementation of a **Retrieval-Augmented Generation (RAG)** system suitable for learning, demos, and early-stage production use.

---

## Made By :
MOHIT KUMAR SAHU