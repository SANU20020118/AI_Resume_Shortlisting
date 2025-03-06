import os
import re
import spacy
import pdftotext
from docx import Document

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    """Clean text and extract keywords using spaCy."""
    text = text.lower()
    text = re.sub(r'[^\w\s+]', '', text)  # Keep + for "C++"
    doc = nlp(text)
    
    # Extract nouns, proper nouns, and technical terms
    skills = {token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]}

    return skills

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF."""
    with open(pdf_path, "rb") as f:
        pdf = pdftotext.PDF(f)
    return "\n".join(pdf).strip().lower()

def extract_text_from_docx(docx_path):
    """Extract text from DOCX."""
    doc = Document(docx_path)
    return '\n'.join([para.text for para in doc.paragraphs]).strip().lower()

def extract_skills_from_file(file_path):
    """Extract skills from a given file."""
    file_ext = os.path.splitext(file_path)[1].lower()

    if file_ext == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif file_ext == ".docx":
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_ext}")

    return preprocess_text(text)
