from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from scripts.main import process_resume, match_resumes_to_job
from scripts.database import get_all_resumes

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
JOB_FOLDER = "job_descriptions"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(JOB_FOLDER, exist_ok=True)

@app.route("/download/<filename>")
def download_resume(filename):
    return send_from_directory("uploads", filename, as_attachment=True)

@app.route("/", methods=["GET", "POST"])
def upload_resume():
    if request.method == "POST":
        uploaded_file = request.files["resume"]
        job_file = request.files.get("job_description")

        if uploaded_file:
            resume_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(resume_path)

            matched_skills, score = process_resume(resume_path)

            # Handle Job Description
            if job_file:
                job_path = os.path.join(JOB_FOLDER, job_file.filename)
                job_file.save(job_path)
                rankings = match_resumes_to_job(job_path)
                return render_template("result.html", filename=uploaded_file.filename, skills=matched_skills, score=score, rankings=rankings)

            return render_template("result.html", filename=uploaded_file.filename, skills=matched_skills, score=score)

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
