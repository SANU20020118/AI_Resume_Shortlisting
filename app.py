from flask import Flask, render_template, request, send_from_directory
import os
from scripts.main import process_resume
from scripts.database import get_all_resumes

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_resume():
    if request.method == "POST":
        if "resume" not in request.files:
            return "No file part"

        uploaded_file = request.files["resume"]
        
        if uploaded_file.filename == "":
            return "No selected file"

        if uploaded_file:
            resume_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(resume_path)

            matched_skills, score = process_resume(resume_path)

            return render_template(
                "result.html", filename=uploaded_file.filename, skills=matched_skills, score=score
            )

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
