import os
from scripts.extract_skills import extract_skills_from_file
from scripts.trie_structure import Trie
from scripts.hashmap_scoring import score_candidates
from scripts.levenshtein import levenshtein_distance
from scripts.database import insert_resume

# Load job skills
job_skills = {
    "python", "machine learning", "data science", "django",
    "c", "c++", "java", "sql", "html", "javascript", "php", "css", "soft skills"
}

# Common variations of SQL
sql_variants = {"mysql", "mssql", "postgresql", "sqlite"}

# Initialize Trie and insert job skills
trie = Trie()
for skill in job_skills:
    trie.insert(skill.lower())  # Store only lowercase for standardization

def process_resume(file_path):
    """Extract skills from a resume, calculate score, and save to database."""
    resume_skills = extract_skills_from_file(file_path)

    # Find exact matches using Trie
    matching_skills = set()
    for skill in resume_skills:
        if skill.lower() in job_skills:
            matching_skills.add(skill)
        elif skill.lower() in sql_variants:  # Convert SQL variations to "sql"
            matching_skills.add("sql")

    # Score candidates based on exact matches
    candidate_score = score_candidates(job_skills, list(matching_skills))

    # Check for close matches using Levenshtein Distance
    for resume_skill in resume_skills:
        if resume_skill not in matching_skills:
            for job_skill in job_skills:
                if len(resume_skill) >= 4 and levenshtein_distance(resume_skill.lower(), job_skill) <= 2:
                    matching_skills.add(job_skill)  # Store correct job skill
                    candidate_score["Candidate"] += 3  

    # Ensure "data science" is captured correctly
    if "data" in resume_skills and "science" in resume_skills:
        matching_skills.add("data science")

    # Convert set to sorted list
    matching_skills = sorted(matching_skills)

    # Store results in the database
    filename = os.path.basename(file_path)
    insert_resume(filename, matching_skills, candidate_score["Candidate"])

    return matching_skills, candidate_score["Candidate"]
