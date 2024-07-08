import os
from flask import Flask, render_template, request, abort, jsonify
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306,
)

print(mydb)


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])


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


@app.route("/api/timeline_post", methods=["POST"])
def post_time_line_post():
    name = request.form["name"]
    email = request.form["email"]
    content = request.form["content"]
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)


@app.route("/api/timeline_post", methods=["GET"])
def get_time_line_post():
    return {
        "timeline_posts": [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


@app.route("/api/timeline_post/<int:id>", methods=["DELETE"])
def delete_time_line_post(id):
    try:
        post = TimelinePost.get_by_id(id)
        post.delete_instance()
        return jsonify({"message": "Post deleted successfully"})
    except DoesNotExist:
        abort(404, description=f"Timeline post with id {id} not found")
