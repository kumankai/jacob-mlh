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
    {
        "institution": "University of Saskatchewan",
        "degree": "Bachelors in Science",
        "date": "2021-2022",
    },
]

hobbiesList = [
    {"hobby": "Basketball", "image": "basketball.jpg"},
    {"hobby": "Guitar", "image": "guitar.JPG"},
    {"hobby": "Eating", "image": "food.JPG"},
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="Jacob Angga",
        url=os.getenv("URL"),
        work_experience=work_experience,
        education=education,
    )


@app.route("/hobbies")
def hobbies():
    return render_template(
        "hobby-page.html",
        title="Jacob Angga",
        url=os.getenv("URL"),
        hobbiesList=hobbiesList,
    )
