 🤖 AI-Powered Resume Shortlisting System

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
│ ├── history.html # History of resumes
│ └── result.html # Result view
│
├── static/ # CSS / JS files (optional)
│
├── model/
│ └── skill_extractor.py # spaCy-based skill extractor
│
├── database/
│ └── db_handler.py # SQLite3 DB connection & operations
│
├── matching/
│ └── ranker.py # TF-IDF-based candidate ranking (planned)
│
├── resumes/ # Folder to store uploaded resumes
│
├── requirements.txt # All dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Getting Started

### 📌 Prerequisites

- Python 3.x installed
- pip installed
- Git (optional)

### 📥 Installation

```bash
git clone https://github.com/your-username/AI-Resume-Shortlister.git
cd AI-Resume-Shortlister
pip install -r requirements.txt
python -m spacy download en_core_web_sm
🛢️ Database Initialization
bash
Copy
Edit
python
>>> from database.db_handler import initialize_db
>>> initialize_db()
>>> exit()
🧪 Usage
📤 Uploading a Resume
Run the server:

bash
Copy
Edit
python app.py
Go to http://localhost:5000

Upload a resume and view extracted skills.

📂 Viewing History
Click on the "History" page to see all analyzed resumes with details.

📊 Candidate Ranking
Provide a list of required job skills.

System will rank resumes (planned using TF-IDF match).

🔮 Future Enhancements
✅ Support for DOCX files

✅ Admin login for HR panel

🔄 Resume score normalization

📊 PDF preview of uploaded resume

📬 Email notifications with shortlisted resumes

🌐 Host using Render, Railway, or GitHub Pages (static)

🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

📄 License
This project is licensed under the MIT License.

👤 Author
Sanu Kumar Dwivedi
