from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Python Developer',
        'location': 'Seattle, WA',
        'salary': 50000
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Seattle, WA',
        'salary': 60000
    },
    {
        'id': 3,
        'title': 'Machine Learning Engineer',
        'location': 'Seattle, WA',
        'salary': 70000
    },
    {
        "id": 4,
        "title": "Software Engineer",
        "location": "Seattle, WA",
        "salary": 80000
    },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
