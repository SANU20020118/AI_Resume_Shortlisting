import sqlite3

DB_PATH = "resume_data.db"

def init_db():
    """Initialize the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            skills TEXT NOT NULL
        )"""
    )

    conn.commit()
    conn.close()

def insert_resume(filename, skills):
    """Insert a new resume into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO resumes (filename, skills) VALUES (?, ?)", 
                   (filename, ", ".join(skills)))

    conn.commit()
    conn.close()

def get_all_resumes():
    """Retrieve all resumes from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id, filename, skills FROM resumes")
    resumes = [{"id": row[0], "filename": row[1], "skills": row[2].split(", ")} for row in cursor.fetchall()]

    conn.close()
    return resumes
