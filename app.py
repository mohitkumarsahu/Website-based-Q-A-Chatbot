import streamlit as st
from crawling import fetch_website, extract_text
from text_processing import chunking_text
from embeddings import create_embeddings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
from qa import retrieve_text, generate_answer




st.set_page_config(page_title="Website Chatbot")
st.title("Website-based Q&A Chatbot")


if "history" not in st.session_state:
     st.session_state.history=[]

url=st.text_input("Enter Website URL")

if st.button("Index Website"):
    try:
         html=fetch_website(url)
         title,text=extract_text(html)

         chunks=chunking_text(text)
         metadata=[
              
              {"text":c,"url":url,"title":title}
               for c in chunks
         ]

         create_embeddings(chunks,metadata)
         st.success("Website Indexed Successfully")

    except Exception as e:
         
        st.error(f"Error: {str(e)}")


        #st.error("Invalid or Unreachable URL")


question=st.chat_input("Ask a question")

if question:                                                                                                                                                                                                                                                                                    
    context_chunks=retrieve_text(question)

    if context_chunks is None:
        answer="The answer is not available in the given Website."

    else:
        context="\n".join(context_chunks)
        history="\n".join(
            f"Q: {q}\nA: {a}"
            for q,a in st.session_state.history[-3:]
        )

        answer=generate_answer(context, question, history)

    st.session_state.history.append((question,answer))

for q,a in st.session_state.history:
    st.chat_message("user").write(q)
    st.chat_message("assistant").write(a)

    
     



         
     