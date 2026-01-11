from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL,LLM_MODEL, TOP_K,SIMILARITY_SCORE
from transformers import pipeline
from load_index import load_index



embedder=SentenceTransformer(EMBEDDING_MODEL)
llm=pipeline('text2text-generation',LLM_MODEL)

def retrieve_text(question : str):

    index,metadata=load_index()
    ques_vector=embedder.encode([question],normalize_embeddings=True)

    scores,ids=index.search(ques_vector, TOP_K) #scores is 2D list of similarity values

    result=[]
    for score,idx in zip(scores[0],ids[0]):
        if score >= SIMILARITY_SCORE:   
            result.append(metadata[idx]['text'])
            
    if not result:
        return None


    return result


def generate_answer(context, question, history):

    prompt=f""" 
    You are a helpful assistant. Answer the user's question **using only the context
    Do NOT make up information. If the answer is not in the context, respond exactly:
    "the answer is not available on the provided Website."
    
    Context:{context}
    Conversation History:{history}
    Question:{question}

    Answer:"""

    response=llm(prompt, max_new_tokens=150)
    result=response[0]["generated_text"].strip()

    return result


