# RESUME MATCHER - Backend

This is the backend API for RESUME MATCHER, an NLP-powered system to match resumes with job descriptions. It's built with Python and FastAPI.

## Features

- Parses resumes (PDF and DOCX).
- Calculates semantic similarity between resumes and job descriptions using Sentence Transformers.
- Extracts skills using spaCy NER.
- Identifies missing skills.
- Generates suggestions for resume improvement.

## Prerequisites

- Python 3.8+
- pip

## Setup and Running

1.  **Navigate to the backend directory:**
    ```bash
    cd /path/to/your/project/nlp/backend
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    This will also download necessary spaCy models and Sentence Transformer models upon first run if not cached.

4.  **Run the FastAPI application:**
    ```bash
    python app.py
    ```

The API will be available at `http://localhost:8000`.
API documentation (Swagger UI) can be accessed at `http://localhost:8000/docs`.

## API Endpoints

-   `POST /upload-resume/`: Upload a resume file. Returns a `resume_id`.
-   `POST /match/`: Takes `resume_id` and `job_description` text. Returns matching score, skills, and suggestions.
-   `GET /health/`: Health check endpoint.

## Key Technologies

- FastAPI: Web framework
- Uvicorn: ASGI server
- spaCy: For Named Entity Recognition (NER) and skill extraction.
- Sentence-Transformers: For generating text embeddings and semantic matching.
- pdfminer.six: For PDF parsing.
- python-docx: For DOCX parsing.