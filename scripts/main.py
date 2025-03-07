import os
from scripts.extract_skills import extract_skills_from_file
from scripts.database import insert_resume

def process_resume(file_path):
    """Extract skills from a resume, calculate a score, and store it in the database."""
    resume_skills = extract_skills_from_file(file_path)
    filename = os.path.basename(file_path)

    # Store in database
    insert_resume(filename, resume_skills)

    return resume_skills, len(resume_skills)  # Return skills & score
