from fastapi import FastAPI, UploadFile, File, HTTPException, Form, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, Dict
from resume_parser import ResumeParser
from matcher import ResumeMatcher
from suggestions import SuggestionGenerator
import os

app = FastAPI(title="Resume Matcher API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store uploaded resume text temporarily (in a real app, use a database)
resume_storage: Dict[str, str] = {}

class JobDescription(BaseModel):
    text: str
    resume_id: str  # Add resume_id to link with uploaded resume

class MatchingResponse(BaseModel):
    match_score: float
    resume_skills: list[str]
    jd_skills: list[str]
    missing_skills: list[str]
    suggestions: list[str]

@app.post("/upload-resume/", response_model=dict)
async def upload_resume(file: UploadFile = File(...)):
    try:
        parser = ResumeParser()
        content = await file.read()
        parsed_text = parser.parse(content, file.filename)
        
        # Generate a simple ID for the resume (in production, use proper ID generation)
        resume_id = f"resume_{len(resume_storage) + 1}"
        resume_storage[resume_id] = parsed_text
        
        return {"status": "success", "text": parsed_text, "resume_id": resume_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/match/", response_model=MatchingResponse)
async def match_resume_jd(job_description: JobDescription):
    try:
        # Get the resume text using the resume_id
        if job_description.resume_id not in resume_storage:
            raise HTTPException(status_code=404, detail="Resume not found. Please upload a resume first.")
            
        resume_text = resume_storage[job_description.resume_id]
        
        matcher = ResumeMatcher()
        suggestion_gen = SuggestionGenerator()
        
        # Get match results
        match_score = matcher.calculate_similarity(resume_text, job_description.text)
        resume_skills = matcher.extract_skills(resume_text)
        jd_skills = matcher.extract_skills(job_description.text)
        missing_skills = matcher.find_missing_skills(resume_skills, jd_skills)
        suggestions = suggestion_gen.generate_suggestions(resume_text, job_description.text)
        
        return MatchingResponse(
            match_score=match_score,
            resume_skills=resume_skills,
            jd_skills=jd_skills,
            missing_skills=missing_skills,
            suggestions=suggestions
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Add a simple health check endpoint
@app.get("/")
def read_root():
    return {"status": "Resume Matcher API is running"}

if __name__ == "__main__":
    import uvicorn
    # Get port from environment variable for deployment platforms
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)