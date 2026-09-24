# Vectorless-RAG---Pageindex
# Overview
This project demonstrates a Vectorless RAG pipeline built using Hugging Face models, without requiring OpenAI API keys. Instead of storing embeddings in a vector database, the system organizes documents into a tree structure and queries them directly using an instruction‑tuned model (google/flan-t5-large).
The goal is to make RAG lightweight, transparent, and easy to run locally — ideal for students, researchers, and engineers who want to experiment with document QA without external API dependencies.

# Features
- No API keys required — runs fully on Hugging Face models.
- Tree-based document indexing — avoids vector databases.
- Instruction-tuned reasoning — uses flan-t5-large for structured answers.
- PDF support — parse and query documents like research papers or reports.
- Streamlit app — simple web interface to ask queries interactively.

# Tech Stack
- Python
- Hugging Face Transformers (flan-t5-large)
- Streamlit (UI)
- PyPDF2 / custom parsing (document tree creation)

# Contributing
Pull requests are welcome! If you’d like to extend this project (e.g., add support for other models or indexing strategies), feel free to fork and submit improvements.
