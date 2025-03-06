import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scripts.database import get_all_resumes

def match_resumes(job_description_path):
    """Match resumes with job description using TF-IDF."""
    with open(job_description_path, "r") as f:
        job_desc = f.read()

    resumes = get_all_resumes()
    resume_texts = [r[2] for r in resumes]  # Extract skills from resumes

    # Vectorize job description and resumes
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([job_desc] + resume_texts)

    # Compute similarity scores
    scores = np.dot(tfidf_matrix[0], tfidf_matrix[1:].T).toarray().flatten()

    # Rank resumes
    ranked_resumes = sorted(zip(resumes, scores), key=lambda x: x[1], reverse=True)

    return ranked_resumes
