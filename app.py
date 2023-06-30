from models.DB import DB
from flask import Flask, render_template, request, redirect, url_for
from helper.join import join
from helper.average import get_average

app = Flask(__name__)


@app.route("/")
def index():
    db = DB()
    return render_template("index.html", data=db.get_all_questions())

@app.route("/results")
def results():          
    db = DB()
    data = join(db.get_answers(), list(request.args.items()))
    average = get_average(data)
    print(average)
    return render_template("results.html", data=data, average=average)

if __name__ == "__main__":
    app.run(debug=True)
