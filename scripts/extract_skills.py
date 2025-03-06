import os
import re
import nltk
import spacy
from nltk.corpus import stopwords
import fitz
from docx import Document

# Download stopwords (only if not already available)
nltk.download('stopwords', quiet=True)

# Load spaCy model for NLP-based skill extraction
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    """Clean and tokenize text by removing punctuation and stopwords."""
    if not text.strip():  # Handle empty text case
        return []

    text = text.lower()
    text = re.sub(r'[^\w\s+]', '', text)  # Preserve `+` for "C++"
    words = text.split()

    # Define technical skills to keep
    technical_terms = {
        "python", "java", "sql", "c", "c++", "html", "javascript", "php",
        "data science", "machine learning", "django", "css", "flask", "nodejs"
    }

    stop_words = set(stopwords.words('english'))
    
    # Keep technical terms and remove general stopwords
    words = [word for word in words if word in technical_terms or word not in stop_words]

    return words  # ✅ No debug prints, just return final words

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using PyMuPDF."""
    doc = fitz.open(pdf_path)
    text = "\n".join(page.get_text() for page in doc)
    return text.lower().strip()
 

def extract_text_from_docx(docx_path):
    """Extract text from DOCX resumes."""
    if not os.path.exists(docx_path):
        raise FileNotFoundError(f"🚨 Error: File not found - {docx_path}")

    doc = Document(docx_path)
    text = '\n'.join([para.text for para in doc.paragraphs]).strip()

    if not text:  # Handle DOCX files with no text
        raise ValueError(f"🚨 Error: No readable text found in '{docx_path}'.")

    print(f"🔍 Extracted Text from {docx_path}:\n{text[:500]}")  # Debugging statement
    return text.lower()

def extract_skills_with_spacy(text):
    """Extract skills using NLP (spaCy)."""
    doc = nlp(text)
    skills = {ent.text.lower() for ent in doc.ents}
    return list(skills)

def extract_skills_from_file(file_path):
    """Extract and preprocess skills from a given file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"🚨 Error: File does not exist - {file_path}")

    filename, file_ext = os.path.splitext(file_path)
    file_ext = file_ext.lower().strip()  # Ensure lowercase and remove spaces

    if not file_ext:  # If no extension is found
        raise ValueError(f"🚨 Error: No file extension found in '{file_path}'. Please rename it with .pdf or .docx")

    if file_ext == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif file_ext == ".docx":
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError(f"🚨 Error: Unsupported file format ({file_ext}). Use PDF or DOCX.")

    # Extract skills using NLP
    nlp_skills = extract_skills_with_spacy(text)

    # Extract skills using preprocessing method
    processed_skills = preprocess_text(text)

    # Merge both sets of skills
    final_skills = set(nlp_skills + processed_skills)

    return list(final_skills)  
