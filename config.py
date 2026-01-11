from langchain.llms import Ollama
CHUNK_SIZE=500
CHUNK_OVERLAP=100
DATA_DIR="data"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
INDEX_PATH = f"{DATA_DIR}/faiss.index"
META_PATH = f"{DATA_DIR}/metadata.json"
LLM_MODEL = "google/flan-t5-small"
TOP_K = 3
SIMILARITY_SCORE=0.6