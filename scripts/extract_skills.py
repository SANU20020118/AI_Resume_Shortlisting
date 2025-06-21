import os
import fitz  # PyMuPDF for PDF extraction
import re
import spacy

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using PyMuPDF."""
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text("text") + "\n"
    except Exception as e:
        print(f"⚠️ Error reading PDF: {e}")
    return text

def extract_skills_from_file(file_path):
    """Extracts skills from a given resume file (PDF or DOCX)."""
    file_ext = os.path.splitext(file_path)[1].lower()

    if file_ext == ".pdf":
        text = extract_text_from_pdf(file_path)
    else:
        raise ValueError(f"🚨 Unsupported file format: {file_ext}")

    print("\n🔍 **Extracted Raw Text:**\n", text[:500])  # Print first 500 characters for debugging

    # Process text with spaCy
    doc = nlp(text)

    # Extract potential skill keywords (only nouns & proper nouns)
    extracted_skills = set()
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:  # Extract meaningful words
            extracted_skills.add(token.text.lower())

    print("📝 **Extracted Tokens (Raw):**", extracted_skills)  # Debugging

    # Define common programming & technical skills to check against
    skill_list = {
    "python", "java", "sql", "c", "c++", "html", "javascript", "php", "css", 
    "flask", "django", "machine learning", "data science", "tensorflow", "nlp",
    "mysql", "mssql", "postgresql", "react", "angular", "nodejs", "express", 
    "git", "github", "data analysis", "deep learning", "pandas", "numpy"
}


    matched_skills = extracted_skills.intersection(skill_list)

    print("✅ **Final Matched Skills:**", matched_skills)  # Debugging

    return list(matched_skills)
