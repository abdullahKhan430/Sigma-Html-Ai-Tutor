import streamlit as st
from rag_engine import ask_question
from videos import videos
import requests


st.markdown("""
<style>

/* Main background gradient */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Hide default header */
header {visibility: hidden;}

/* Centered hero section */
.hero {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 80vh;
    text-align: center;
}

/* Main title */
.hero h1 {
    font-size: 55px;
    font-weight: 800;
    margin-bottom: 10px;
}

/* Subtitle */
.hero h3 {
    font-size: 26px;
    font-weight: 400;
    margin-bottom: 20px;
    color: #cbd5e1;
}

/* Description */
.hero p {
    font-size: 20px;
    max-width: 700px;
    color: #e2e8f0;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background-color: white;
}

/* Chat message styling */
[data-testid="stChatMessage"] {
    background-color: white;
    padding: 12px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)


st.set_page_config(
    page_title="Sigma HTML AI Tutor",
    page_icon="💬",
    layout="wide"
)


page = st.sidebar.radio (
    "Navigate",
    ["Home", "Chat", "About"]

)
st.sidebar.title("📚 Course Videos")

for video in videos:
    st.sidebar.markdown(f"[{video['title']}]({video['link']})")

st.sidebar.markdown("---")



if page == "Home":

    st.markdown("""
    <div class="hero">
        <h1>🚀 Sigma HTML AI Tutor</h1>
        <h3>Your Personal AI Tutor for HTML</h3>
        <p>
        An AI-powered assistant trained on 10 HTML lectures from the Sigma Web Development Course.
        <br><br>
        Ask questions and receive intelligent, timestamp-based guidance instantly.
        <br><br>
        Built using Retrieval-Augmented Generation (RAG) for accurate and contextual answers.
        <br><br>
        Built by Abdullah khan | Powered by RAG + Ollama       
        </p>
    </div>
    """, unsafe_allow_html=True)



elif page == "Chat":

    st.title("💬 Ask About HTML")

    if "messages" not in st.session_state:
       st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    prompt = st.chat_input("Ask a question about HTML...")

    if prompt:
    
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

    
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            response = ""

            for token in ask_question(prompt):
                response += token
                response_placeholder.markdown(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}

    )

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()
      



elif page == "About":

    st.title("About Sigma HTML AI Tutor")

    st.subheader("What is RAG?")
    st.write("""
    Retrieval-Augmented Generation (RAG) combines document retrieval 
    with large language models. Instead of answering from memory, 
    the system retrieves relevant transcript chunks before generating 
    an answer.
    """)

    st.subheader("How It Works")
    st.write("""
    1. User asks a question  
    2. The system converts the question into embeddings  
    3. It finds the most similar transcript chunks  
    4. Retrieved context is sent to the LLM  
    5. The AI generates a contextual answer with video timestamps  
    """)

    st.subheader("Tech Stack Used")
    st.write("""
    - Python  
    - Streamlit  
    - Ollama (llama3.2)  
    - bge-m3 Embeddings  
    - scikit-learn (Cosine Similarity)  
    - Joblib
    - whisper
    - numpy
    - pandas           
    """) 