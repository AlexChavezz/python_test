from models.DB import DB
from flask import Flask, render_template, request, redirect, url_for
from helper.join import join
from helper.average import get_average
import random

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")

@app.route("/python")
def index():
   
    db = DB()
    data = db.get_all_questions()
    random.shuffle(data)
    for item in data:
        if 'answers' in item:
            random.shuffle(item['answers'])
    return render_template("index.html", data=data)

@app.route("/results")
def results():        
    db = DB()
    data = join(db.get_answers(), list(request.args.items()))
    average = get_average(data)
    if average != 0:
        db.save_attempt(average, request.remote_addr)
    return render_template("results.html", data=data, average=average)

@app.route("/java")
def main_java():
    db = DB()
    data = db.get_java_questions()
    random.shuffle(data)
    for item in data:
        if 'answers' in item:
            random.shuffle(item['answers'])
    return render_template("java.html", data=data)

@app.route("/java_results")
def java_results():
    db = DB()
    data = join(db.get_java_questions(), list(request.args.items()))
    average = get_average(data)
    if average != 0:
        db.save_java_attempt(average, request.remote_addr)
    return render_template("results.html", data=data, average=average)



if __name__ == "__main__":
    app.run(debug=True)
