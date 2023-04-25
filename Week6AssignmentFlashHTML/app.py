from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("welcome.html", date=datetime.now())


@app.route("/rick_roll/")
@app.route("/rick_roll.html")
@app.route("/rickroll/")
@app.route("/display_image/")
@app.route("/display_image.html")
def rickroll():
    return render_template("display_image.html")


@app.route("/coolest_games/")
@app.route("/game_site_list/")
@app.route("/game_site_list.html")
def ordered_games_list():
    return render_template("game_site_list.html")
