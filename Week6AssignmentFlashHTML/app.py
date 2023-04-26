"""A web applicate using Flask.
Charles Kresho, 04/25/23
"""
from datetime import datetime
from flask import Flask
from flask import render_template

app = Flask(__name__)


# The default welcome page for the site.
@app.route("/")
def home():
    """
    Renders a the welcome homepage. Datetime is passed for displaying the system time.
    """
    return render_template("welcome.html", date=datetime.now())


# Displays an image in the browser. It's a prank hehe
@app.route("/rick_roll/")
@app.route("/rick_roll.html")
@app.route("/rickroll/")
@app.route("/display_image/")
@app.route("/display_image.html")
def rickroll():
    """
    Renders the prank image webpage.
    """
    return render_template("display_image.html")


# A list of my favorite games, with links to their homepages.
@app.route("/coolest_games/")
@app.route("/game_site_list/")
@app.route("/game_site_list.html")
def ordered_games_list():
    """
    Renders the "Top games" webpage.
    """
    return render_template("game_site_list.html")
