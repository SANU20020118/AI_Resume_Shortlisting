# 🤖 AI-Powered Resume Shortlisting System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An intelligent web application that automates the process of shortlisting resumes by extracting skills and ranking candidates based on job-specific requirements using Natural Language Processing (NLP).

---

## 📑 Table of Contents

-   [About the Project](#about-the-project)
-   [Features](#features)
-   [Technology Stack](#technology-stack)
-   [File Structure](#file-structure)
-   [Getting Started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Installation](#installation)
    -   [Database Initialization](#database-initialization)
-   [Usage](#usage)
    -   [Uploading a Resume](#uploading-a-resume)
    -   [Viewing History](#viewing-history)
    -   [Candidate Ranking](#candidate-ranking)
-   [Future Enhancements](#future-enhancements)
-   [Contributing](#contributing)
-   [License](#license)
-   [Author](#author)

---

## 📌 About the Project

This project is an AI-powered web application designed to streamline the **resume shortlisting process**. It allows users to upload resumes (PDF currently, DOCX support planned), extract key skills using **spaCy NLP**, store resume data in a database, and analyze or rank candidates based on predefined job requirements.

The goal is to **automate** the initial screening of resumes, helping recruiters efficiently identify the most relevant candidates.

---

## 🚀 Features

-   📄 **Resume Upload** – Simple and intuitive upload interface for PDF (DOCX support planned)
-   🧠 **Skill Extraction** – Extracts both technical and soft skills using `spaCy`
-   💾 **Database Storage** – Stores resume filename, extracted skills, and upload timestamp using SQLite
-   📊 **Basic Resume Analysis** – Shows matched skills and a score on upload
-   📂 **Resume History** – View previously uploaded and analyzed resumes
-   📈 **Candidate Ranking** – Match resumes to job skills using basic intersection (TF-IDF similarity is in development)
-   🧩 **Modular Design** – Clean separation between extraction, storage, UI, and ranking logic

---

## 🛠️ Technology Stack

-   **Backend**: Python 3.x, Flask
-   **Database**: SQLite3
-   **NLP**: spaCy (`en_core_web_sm`)
-   **PDF Parsing**: PyMuPDF (`fitz`)
-   **Web Templates**: Jinja2 (HTML)
-   **Other Libraries**: `numpy`, `scikit-learn`, `gunicorn`

---

## 📁 File Structure
  
AI_Resume_Shortlisting/
├── app.py                     # Main Flask application entry point
├── requirements.txt           # Python dependencies
├── python_dev.txt             # Example job description for testing ranking
├── scripts/                   # Directory for core logic modules
│   ├── database.py            # Handles SQLite database operations (init, insert, get)
│   ├── extract_skills.py      # Extracts text from PDFs and identifies skills
│   ├── hashmap_scoring.py     # (Potential) Alternative scoring logic
│   ├── levenshtein.py         # (Potential) Levenshtein distance for fuzzy matching
│   ├── main.py                # Orchestrates resume processing and basic ranking
│   ├── matching.py            # (Potential) Advanced TF-IDF based matching
│   └── trie_structure.py      # (Potential) Trie data structure for optimized skill lookup
├── templates/                 # HTML templates for the web interface
│   ├── history.html           # Displays a list of all analyzed resumes
│   ├── rank.html              # Displays ranked candidates based on job skills
│   ├── result.html            # Shows analysis results for a single uploaded resume (includes ranking section)
│   └── upload.html            # Resume upload form
└── uploads/                   # Directory to store uploaded resume files

---

## ⚙️ Getting Started

### 📌 Prerequisites

-   Python 3.8+
-   `pip` (Python package installer)
-   Git (optional, for cloning the repository)

---

### 📥 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/AI_Resume_Shortlisting.git](https://github.com/your-username/AI_Resume_Shortlisting.git)
    cd AI_Resume_Shortlisting
    ```
    (Replace `your-username` with your actual GitHub username if you're forking the repo).

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download the spaCy English model:**
    ```bash
    python -m spacy download en_core_web_sm
    ```

---

## 🛢️ Database Initialization

The database table (`resumes`) is automatically initialized when the Flask application starts. Ensure you run the `app.py` file.

---

### 🧪 Usage

#### 📤 Uploading a Resume

1.  **Start the server:**
    ```bash
    python app.py
    ```
2.  Then open your browser and visit:
    ```
    http://localhost:5000
    ```
3.  Upload a resume (PDF) and view the extracted skills and score.

#### 📂 Viewing History

*(This feature requires an additional Flask route in `app.py` to be fully accessible from the UI. It will pull data via `get_all_resumes()` from `scripts/database.py` and render `templates/history.html`.)*

#### 📊 Candidate Ranking (Planned)

*(This feature will involve adding a method to input job-specific skills (e.g., from `python_dev.txt`). The system will then compare and rank resumes using the logic in `scripts/main.py` or `scripts/matching.py` and display results via `templates/rank.html`.)*

---

## 🔮 Future Enhancements

* ✅ Support for DOCX files in `scripts/extract_skills.py`.
* ✅ Admin login for HR panel.
* 🔄 Resume score normalization for more accurate comparisons.
* 📊 PDF preview of uploaded resumes.
* 📬 Email notifications with shortlisted resumes.
* 🌐 Deployment via platforms like Render, Railway, or GitHub Pages.
* Integrating and utilizing the advanced `matching.py` (TF-IDF), `hashmap_scoring.py`, `levenshtein.py`, and `trie_structure.py` modules.

---

## 🤝 Contributing

Contributions are welcome!
Please fork the repository and submit a pull request with improvements.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

Sanu Kumar Dwivedi
