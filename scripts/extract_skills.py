import os
import re
import spacy
from docx import Document
import fitz  # PyMuPDF

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF."""
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text() for page in doc])
    return text.lower()

def extract_text_from_docx(docx_path):
    """Extract text from a DOCX file."""
    doc = Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs]).lower()

def extract_skills_from_file(file_path):
    """Extract and preprocess skills from a given file."""
    file_ext = os.path.splitext(file_path)[1].lower()

    if file_ext == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif file_ext == ".docx":
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError(f"🚨 Unsupported file format: {file_ext}. Use PDF or DOCX.")

    doc = nlp(text)
    skills = {token.text for token in doc if token.is_alpha}
    
    return list(skills)
