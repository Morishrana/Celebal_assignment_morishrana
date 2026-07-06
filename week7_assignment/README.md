# AI Question Answering Assistant

This project is a Streamlit-based question answering application powered by Cohere. It supports two usage modes:

- General question answering without uploading a PDF
- Document-based question answering using a PDF and Pinecone retrieval

When a PDF is uploaded, the app extracts text, creates embeddings, stores them in Pinecone, retrieves relevant chunks, and generates answers grounded in the document. When no PDF is uploaded, the app works like a general chatbot.

## Features

- Ask questions directly without uploading any document
- Upload a PDF for retrieval-augmented answers
- Cohere-powered response generation
- Pinecone-powered vector search for document mode
- Simple Streamlit interface

## Requirements

- Python 3.10+
- A Cohere API key
- A Pinecone API key for PDF mode only

## Project Structure

```text
week7_assignment/
|-- app.py
|-- chatbot.py
|-- vectorstore.py
|-- requirements.txt
|-- README.md
```

## Installation

From the project root:

```powershell
cd "C:\Users\itsrh\Downloads\week7_assignment_Morish _Rana"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r .\week7_assignment\requirements.txt
```

## Run the Application

From the project root:

```powershell
cd "C:\Users\itsrh\Downloads\week7_assignment_Morish _Rana"
.\.venv\Scripts\Activate.ps1
streamlit run .\week7_assignment\app.py
```

Or run it directly without activating the virtual environment:

```powershell
cd "C:\Users\itsrh\Downloads\week7_assignment_Morish _Rana"
.\.venv\Scripts\streamlit.exe run .\week7_assignment\app.py
```

After startup, open:

```text
http://localhost:8501
```

## How to Use

### General Chat Mode

1. Enter your Cohere API key in the sidebar.
2. Leave the PDF upload empty.
3. Type a question.
4. Click `Submit`.

### PDF Question Answering Mode

1. Enter your Cohere API key in the sidebar.
2. Enter your Pinecone API key in the sidebar.
3. Upload a PDF file.
4. Type a question about the uploaded document.
5. Click `Submit`.

## Notes

- Pinecone is only required when using PDF mode.
- The app stores the uploaded PDF locally as `uploaded_document.pdf` while processing.
- The application UI is written in English.

## License

This project is licensed under the Apache License. See [LICENSE](./LICENSE) for details.
