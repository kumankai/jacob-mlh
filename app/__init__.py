import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

work_experience = [
    {"company": "Tim Hortons", "position": "Crew Member"},
]

education = [
    {
        "institution": "Sheridan College",
        "degree": "Honors Bachelors of Computer Science",
        "date": "2022 - Present",
    },
]

hobbies = [
    {"hobby": "Basketball", "image": ""},
    {"hobby": "Guitar", "image": ""},
    {"hobby": "Eating", "image": ""},
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="MLH Fellow",
        url=os.getenv("URL"),
        work_experience=work_experience,
        education=education,
    )