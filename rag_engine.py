import os
import numpy as np
import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from groq import Groq



# Load Embedding Model

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


# Load Stored Data

df = joblib.load("embeddings.joblib")


# Initialize Groq Client
def get_groq_client():
    api_key = os.environ.get("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found. Add it in Streamlit Secrets.")

    return Groq(api_key=api_key)



# Create Embeddings
def create_embedding(text_list):
    return embedding_model.encode(text_list).tolist()



# Streaming Inference
def inference_stream(prompt):

    client = get_groq_client()

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )

    for chunk in completion:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content



# Main RAG Function
def ask_question(incoming_query):

    question_embedding = create_embedding([incoming_query])[0]

    similarities = cosine_similarity(
        np.vstack(df["embedding"]),
        [question_embedding]
    ).flatten()

    top_results = 5
    max_indx = similarities.argsort()[::-1][:top_results]
    new_df = df.loc[max_indx]

    context = new_df[
        ["title", "number", "start", "end", "text"]
    ].to_json(orient="records")

    prompt = f'''
I am teaching HTML in my Sigma web development course. Here are video subtitle chunks containing video title, video number, start time in seconds, end time in seconds, the text at that time:

{new_df[["title", "number", "start", "end", "text"]].to_json(orient="records")}
---------------------------------
"{incoming_query}"
User asked this question related to the video chunks, you have to answer in a human way (dont mention the above format, its just for you) where and how much content is taught in which video (in which video and at what timestamp) and guide the user to go to that particular video. If user asks unrelated question, tell him that you can only answer questions related to the course

'''

    return inference_stream(prompt)