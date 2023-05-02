"""A web applicate using Flask.
Charles Kresho, 04/25/23
"""
from datetime import datetime
from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from passlib.hash import sha256_crypt
import re


app = Flask(__name__)
app.config.update(SECRET_KEY='82cafce9733d18ce21d897bc83d613abcbad50801de1a3e06207af1bdef9f661')

# Perform the setup necessary for the webpage
# Load in the existing user login information; storing information as a text
# file is probably inefficient, but oh well, best I can do for now.
# Using a dictionary allows no duplicate users, allows for quick searching
cur_user = None
user_dict = {}


with open('user_login_data.txt', 'w+', encoding="UTF-8") as file:
    while True:
        # For each line, extract the username and hashed password
        line = file.readline()
        line = line.strip()
        if len(line) == 0:  # Exit reading file when end of file reached
            break
        split_line = line.split(',')
        user_dict[split_line[0]] = split_line[1]




# This function is called before each request to the page. 
@app.before_request
def check_for_login_session():
    """
    Checks to ensure that either the user is logged in, or they are trying to access a login page.
    """

    # If the user is not logged in and is not trying ot access either the login or registration page, redirect them to the login page
    if cur_user is None:
        login_regex = re.compile(r'/login\w*.html')
        register_regex = re.compile(r'/register\w*.html')
        if not (login_regex.search(request.path)
                or register_regex.search(request.path)):
            flash("You must be logged in to access other pages on this site.", "error")
            return redirect(url_for("login"))


# The default welcome page for the site.
@app.route("/")
def home():
    """
    Renders a the welcome homepage. Datetime is passed for displaying the system time.
    """
    return render_template("welcome.html", date=datetime.now())


# Displays an image in the browser. It's a prank hehe
@app.route("/rick_roll.html")
def rickroll():
    """
    Renders the prank image webpage.
    """
    return render_template("rick_roll.html")


# A list of my favorite games, with links to their homepages.
@app.route("/game_site_list.html")
def ordered_games_list():
    """
    Renders the "Top games" webpage.
    """
    return render_template("game_site_list.html")


# Login page, redirect if user not logged in
@app.route("/login.html", methods=['GET', 'POST'])
def login():
    return render_template("default_login_page.html")
