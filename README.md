# 🚀 Sigma HTML AI Tutor

Sigma HTML AI Tutor is a **RAG (Retrieval-Augmented Generation) based AI teaching assistant** that helps users learn HTML by asking questions about course videos.

The system processes video lectures and converts them into searchable knowledge. When a user asks a question, the AI retrieves the most relevant parts of the course content and generates an answer using a locally running Large Language Model.

---

# ✨ Features

* Ask questions about HTML concepts
* Retrieves the most relevant video segments
* Uses semantic search to understand context
* Generates answers using a local LLM
* Shows the **video number and timestamp** where the concept is explained
* Simple interactive web interface built with Streamlit

---

# 🧠 How It Works

This project follows the **Retrieval-Augmented Generation (RAG)** architecture.

1. Video lectures are converted into audio files
2. Audio is transcribed into subtitle chunks
3. Each chunk is converted into vector embeddings
4. The embeddings are stored in a dataframe

When a user asks a question:

* The query is converted into an embedding
* Cosine similarity retrieves the most relevant chunks
* The retrieved chunks are used to build a prompt
* The prompt is sent to a locally running LLM using Ollama
* The generated response is displayed in the Streamlit web app

---

# 📂 Project Structure

```
sigma-html-ai-tutor
│
├── app.py
├── rag_engine.py
├── preprocess_json.py
├── mp3_to_json.py
├── videos_to_mp3.py
├── embeddings.joblib
│
├── videos/
├── mp3/
├── jsons/
│
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/sigma-html-ai-tutor.git
cd sigma-html-ai-tutor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install and run Ollama:

Download from
https://ollama.com

Run the model:

```bash
ollama run llama3
```

---

# 📊 Data Processing Pipeline

### Step 1 – Collect Video Data

Place your video files inside the **videos** folder.

---

### Step 2 – Convert Videos to MP3

Run:

```bash
python videos_to_mp3.py
```

This extracts audio from video files.

---

### Step 3 – Convert MP3 to JSON

Run:

```bash
python mp3_to_json.py
```

This generates JSON subtitle chunks from audio.

---

### Step 4 – Create Embeddings

Run:

```bash
python preprocess_json.py
```

This converts text chunks into vector embeddings and saves them as **embeddings.joblib**.

---

# 💻 Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

Then open the browser link provided by Streamlit.

Users can now interact with the **Sigma HTML AI Tutor** and ask questions about HTML concepts from the course videos.

---

# 🛠 Tech Stack

* Python
* Streamlit
* Ollama
* Sentence Embeddings
* Cosine Similarity
* Pandas
* Joblib
* Whisper
* NumPy
* RAG (Retrieval-Augmented Generation)

---

# 📚 Dataset

This project uses **11 HTML tutorial videos from the Sigma Web Development Course** as the knowledge source.

---

# 🎯 Purpose of the Project

The goal of this project is to demonstrate how **AI assistants can answer questions using custom knowledge sources** by combining semantic search with large language models.

It also serves as a learning project for building **RAG-based AI applications**.

---

# 🎥 Demo

A demo video of the system running locally can be found here:

https://www.linkedin.com/posts/abdullah-khan-935a66237_ai-machinelearning-rag-activity-7436110952128999424-Lr4N

---

# ⭐ Future Improvements

* Support for multiple courses
* Better UI design
* Faster embedding search
* Cloud deployment
* Support for more LLM models

