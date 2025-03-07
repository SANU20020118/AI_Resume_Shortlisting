import os
from scripts.extract_skills import extract_skills_from_file
from scripts.database import insert_resume, get_all_resumes

def process_resume(file_path):
    """Extract skills from a resume, calculate a score, and store it in the database."""
    resume_skills = extract_skills_from_file(file_path)
    filename = os.path.basename(file_path)

    # Store in database
    insert_resume(filename, resume_skills)

    return resume_skills, len(resume_skills)  # Return skills & score

def match_resumes_to_job(job_skills):
    """Match resumes against job skills and rank them."""
    all_resumes = get_all_resumes()  # Fetch all stored resumes
    ranked_resumes = []

    for resume in all_resumes:
        matched_skills = set(job_skills).intersection(set(resume["skills"]))
        score = len(matched_skills)

        ranked_resumes.append({
            "filename": resume["filename"],
            "score": score,
            "matched_skills": list(matched_skills)
        })

    ranked_resumes.sort(key=lambda x: x["score"], reverse=True)  # Sort by highest score
    return ranked_resumes
