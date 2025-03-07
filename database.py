import sqlite3

DB_PATH = "database.db"

def init_db():
    """Initialize the database and create tables if they don't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL,
        skills TEXT NOT NULL,
        uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()
    conn.close()

def insert_resume(filename, skills):
    """Insert resume data into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    skills_str = ", ".join(skills)
    cursor.execute("INSERT INTO resumes (filename, skills) VALUES (?, ?)", (filename, skills_str))

    conn.commit()
    conn.close()

def get_all_resumes():
    """Retrieve all resumes from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT filename, skills FROM resumes")
    rows = cursor.fetchall()

    resumes = []
    for row in rows:
        resumes.append({"filename": row[0], "skills": row[1].split(", ")})

    conn.close()
    return resumes
