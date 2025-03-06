import sqlite3

DATABASE_PATH = "resumes.db"

def init_db():
    """Initialize the database and create necessary tables."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Create resumes table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            matched_skills TEXT,
            score INTEGER,
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

def insert_resume(filename, matched_skills, score):
    """Insert analyzed resume details into the database."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO resumes (filename, matched_skills, score)
        VALUES (?, ?, ?)
    ''', (filename, ', '.join(matched_skills), score))

    conn.commit()
    conn.close()

def get_all_resumes():
    """Fetch all stored resumes."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM resumes ORDER BY uploaded_at DESC')
    resumes = cursor.fetchall()

    conn.close()
    return resumes
