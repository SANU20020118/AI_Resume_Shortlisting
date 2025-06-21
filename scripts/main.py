import os
from scripts.extract_skills import extract_skills_from_file
from scripts.database import insert_resume

def process_resume(file_path):
    """Extracts relevant skills and calculates the candidate score."""
    resume_skills = extract_skills_from_file(file_path)

    # Debugging: Print extracted skills
    print("🔍 Extracted Skills:", resume_skills)

    if not resume_skills:
        print("⚠️ Warning: No skills were extracted!")

    filename = os.path.basename(file_path)

    # Store extracted skills in database
    insert_resume(filename, resume_skills)

    # Score is the number of matched skills
    score = len(resume_skills)

    print(f"✅ Processed Resume: {filename} | Score: {score}")

    return resume_skills, score  # Return skills and score
