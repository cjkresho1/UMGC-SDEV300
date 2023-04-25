from flask import Flask
from flask import render_template
import re
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("welcome.html", date=datetime.now())


@app.route("/hello/")
@app.route("/hello_there")
@app.route("/hello_there.html")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )


@app.route("/coolest_games/")
@app.route("/game_site_list/")
@app.route("/game_site_list.html")
def ordered_games_list():
    return render_template("game_site_list.html")
