from collections import defaultdict

def score_candidates(job_skills, resume_skills):
    """Score candidates based on skill match using HashMap."""
    skill_weight = {skill: 5 for skill in job_skills}  # Assign a weight to each skill
    candidate_score = defaultdict(int)

    for skill in resume_skills:
        if skill in skill_weight:
            candidate_score["Candidate"] += skill_weight[skill]

    return candidate_score
