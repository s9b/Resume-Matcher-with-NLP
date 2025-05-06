# RESUME MATCHER

RESUME MATCHER is an NLP-powered system designed to match resumes with job descriptions, providing users with a similarity score, skill analysis, and actionable suggestions for resume improvement.

This project consists of two main components:

-   **Frontend**: A React-based user interface for uploading resumes and job descriptions, and viewing the analysis results.
-   **Backend**: A Python FastAPI application that handles resume parsing, NLP processing, and matching logic.


## Getting Started

To run the full application, you need to start both the backend server and the frontend development server.

1.  **Backend Setup & Start:** Please refer to the [backend/README.md](./backend/README.md) for instructions on setting up and running the backend API.
2.  **Frontend Setup & Start:** Please refer to the [frontend/README.md](./frontend/README.md) for instructions on setting up and running the frontend application.

## Core Technologies

-   **Natural Language Processing (NLP):**
    -   spaCy for Named Entity Recognition (skill extraction)
    -   Sentence-Transformers for semantic text embeddings and similarity calculation
-   **Backend:** Python, FastAPI, Uvicorn
-   **Frontend:** React, JavaScript

## How it Works

1.  The user uploads their resume (PDF or DOCX) and provides a job description through the frontend.
2.  The frontend sends this data to the backend API.
3.  The backend parses the resume text.
4.  It then uses NLP models to:
    -   Generate semantic embeddings for both the resume and job description.
    -   Calculate a cosine similarity score between them.
    -   Extract key skills from both texts.
    -   Identify skills present in the job description but missing from the resume.
    -   Generate personalized suggestions to improve the resume based on its content and common best practices.
5.  The backend returns these results (score, skills, suggestions) to the frontend for display.
