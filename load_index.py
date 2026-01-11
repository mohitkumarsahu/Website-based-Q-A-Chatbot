import json
import faiss
from config import INDEX_PATH,META_PATH

def load_index():
    index=faiss.read_index(INDEX_PATH)  # Loading vector index

    with open(META_PATH) as f:
        metadata=json.load(f)  # Loading metadata from local computer.

    return index, metadata