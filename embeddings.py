
import os
import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from config import DATA_DIR, EMBEDDING_MODEL, INDEX_PATH,META_PATH

def create_embeddings(chunks, metadata):
    if not chunks:
        raise ValueError("No chunks provided for embeddings")
    
    os.makedirs(DATA_DIR, exist_ok=True)

    model=SentenceTransformer(EMBEDDING_MODEL)
    embeddings=model.encode(chunks,normalize_embeddings=True) 
    dim=embeddings.shape[1]     # it will tell you how many numbers are there in one embedding vector - means no. of column in embedding vector bcz when we 
                                # when we create vector database we have to pass the dimension of the embedding.
 
    index=faiss.IndexFlatIP(dim) 
    
    index.add(np.array(embeddings,dtype='float32')) # Adding the embeddings into vector index in array format.

    faiss.write_index(index, INDEX_PATH)    # writing the indexes into faiss vector database.

    with open(META_PATH, "w") as f: #Writing index with embeddings stored in it in local computer.
        json.dump(metadata,f)

