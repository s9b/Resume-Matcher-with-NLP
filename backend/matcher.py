from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import spacy

class ResumeMatcher:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.nlp = spacy.load('en_core_web_sm')
        
    def calculate_similarity(self, resume_text: str, job_description: str) -> float:
        """Calculate similarity score between resume and job description."""
        # Generate embeddings
        resume_embedding = self.model.encode([resume_text])
        jd_embedding = self.model.encode([job_description])
        
        # Calculate cosine similarity
        similarity = cosine_similarity(resume_embedding, jd_embedding)[0][0]
        
        # Convert to percentage
        return float(similarity * 100)

    def extract_skills(self, text: str) -> list[str]:
        """Extract skills from text using spaCy NER."""
        doc = self.nlp(text)
        skills = set()
        
        # Extract entities that might be skills
        for ent in doc.ents:
            if ent.label_ in ["PRODUCT", "ORG", "GPE"]:
                skills.add(ent.text)
                
        return list(skills)

    def find_missing_skills(self, resume_skills: list[str], jd_skills: list[str]) -> list[str]:
        """Find skills present in job description but missing from resume."""
        return list(set(jd_skills) - set(resume_skills))