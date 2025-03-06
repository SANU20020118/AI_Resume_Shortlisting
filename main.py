import os
from scripts.extract_skills import extract_skills_from_file
from scripts.database import insert_resume
from scripts.matching import match_resumes

def process_resume(file_path):
    """Extract skills from resume, calculate score, and save to database."""
    resume_skills = extract_skills_from_file(file_path)
    filename = os.path.basename(file_path)

    # Store results in the database
    insert_resume(filename, resume_skills)

    return resume_skills

def match_resumes_to_job(job_description_path):
    """Match resumes against a job description and rank them."""
    return match_resumes(job_description_path)
