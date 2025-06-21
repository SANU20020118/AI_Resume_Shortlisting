# 🤖 AI-Powered Resume Shortlisting System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An intelligent web application that automates the process of shortlisting resumes by extracting skills and ranking candidates based on job-specific requirements using Natural Language Processing (NLP).

---

## 📑 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [File Structure](#file-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Database Initialization](#database-initialization)
- [Usage](#usage)
  - [Uploading a Resume](#uploading-a-resume)
  - [Viewing History](#viewing-history)
  - [Candidate Ranking](#candidate-ranking)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## 📌 About the Project

This project is an AI-powered web application designed to streamline the **resume shortlisting process**. It allows users to upload resumes (PDF/DOCX), extract key skills using **spaCy NLP**, store resume data in a database, and analyze or rank candidates based on predefined job requirements.

The goal is to **automate** the initial screening of resumes, helping recruiters efficiently identify the most relevant candidates.

---

## 🚀 Features

- 📄 **Resume Upload** – Simple and intuitive upload interface for PDF (DOCX support planned)
- 🧠 **Skill Extraction** – Extracts both technical and soft skills using `spaCy`
- 💾 **Database Storage** – Stores resume name, extracted skills, and timestamp using SQLite
- 📊 **Basic Resume Analysis** – Shows matched skills and a score on upload
- 📂 **Resume History** – View previously uploaded and analyzed resumes
- 📈 **Candidate Ranking** – Match resumes to job skills using TF-IDF similarity (in development)
- 🧩 **Modular Design** – Clean separation between extraction, storage, UI, and ranking logic

---

## 🛠️ Technology Stack

- **Backend**: Python 3.x, Flask
- **Database**: SQLite3
- **NLP**: spaCy (`en_core_web_sm`)
- **PDF Parsing**: PyMuPDF (`fitz`)
- **Web Templates**: Jinja2 (HTML)
- **Other Libraries**: `numpy`, `scikit-learn`, `gunicorn`

---

## 📁 File Structure

AI-Resume-Shortlister/
│
├── app.py # Flask main application
├── templates/
│ ├── upload.html # Resume upload page
│ ├── history.html # Resume history page
│ └── result.html # Result view page
│
├── static/ # CSS / JS files (optional)
├── model/
│ └── skill_extractor.py # spaCy-based skill extractor
├── database/
│ └── db_handler.py # SQLite3 DB operations
├── matching/
│ └── ranker.py # TF-IDF-based candidate ranking (planned)
├── resumes/ # Folder to store uploaded resumes
├── requirements.txt # All dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Getting Started

### 📌 Prerequisites

- Python 3.x
- pip
- Git (optional)

---

### 📥 Installation

```bash
git clone https://github.com/your-username/AI-Resume-Shortlister.git
cd AI-Resume-Shortlister
pip install -r requirements.txt
python -m spacy download en_core_web_sm
🛢️ Database Initialization
python
Copy
Edit
# Run in Python shell or inside a script
from database.db_handler import initialize_db
initialize_db()
🧪 Usage
📤 Uploading a Resume
Start the server:

bash
Copy
Edit
python app.py
Open your browser and go to: http://localhost:5000

Upload a resume to view extracted skills.

📂 Viewing History
Click on the History page to see all previously uploaded resumes and their extracted data.

📊 Candidate Ranking (Planned)
Add a list of required job-specific skills.

The system will compare and rank resumes using TF-IDF similarity.

🔮 Future Enhancements
✅ Support for DOCX files

✅ Admin login for HR panel

🔄 Resume score normalization

📊 PDF preview of uploaded resume

📬 Email notifications with shortlisted resumes

🌐 Deployment via Render/Railway

🤝 Contributing
Contributions are welcome!
Please fork the repository and submit a pull request with improvements.

📄 License
This project is licensed under the MIT License.

👤 Author
Sanu Kumar Dwivedi
