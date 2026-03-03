import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib
import requests
import json


# Create Embedding

def create_embedding(text_list):
    r = requests.post(
        "http://localhost:11434/api/embed",
        json={
            "model": "bge-m3",
            "input": text_list
        }
    )
    return r.json()["embeddings"]


# Streaming Inference

def inference_stream(prompt):
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": True
        },
        stream=True
    )

    for line in r.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            token = data.get("response", "")
            yield token   


df = joblib.load('embeddings.joblib')


# Main RAG Function
def ask_question(incoming_query):

    question_embedding = create_embedding([incoming_query])[0]

    similarities = cosine_similarity(
        np.vstack(df['embedding']),
        [question_embedding]
    ).flatten()

    top_results = 5
    max_indx = similarities.argsort()[::-1][0:top_results]
    new_df = df.loc[max_indx]

    prompt = f'''
I am teaching HTML in my Sigma web development course. Here are video subtitle chunks containing video title, video number, start time in seconds, end time in seconds, the text at that time:

{new_df[["title", "number", "start", "end", "text"]].to_json(orient="records")}
---------------------------------
"{incoming_query}"
User asked this question related to the video chunks, you have to answer in a human way (dont mention the above format, its just for you) where and how much content is taught in which video (in which video and at what timestamp) and guide the user to go to that particular video. If user asks unrelated question, tell him that you can only answer questions related to the course

'''

    return inference_stream(prompt)