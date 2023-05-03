"""A web applicate using Flask.
Charles Kresho, 04/25/23
"""
from datetime import datetime
import re
from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from passlib.hash import sha256_crypt


app = Flask(__name__)
app.config.update(
    SECRET_KEY='82cafce9733d18ce21d897bc83d613abcbad50801de1a3e06207af1bdef9f661')


# Perform the setup necessary for the webpage
# Load in the existing user login information; storing information as a text
# file is probably inefficient, but oh well, best I can do for now.
# Using a dictionary allows no duplicate users, allows for quick searching

cur_user = None
user_dict = {}

with open('user_login_data.txt', 'r+', encoding="UTF-8") as file:
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

    # If the user is not logged in and is not trying ot access either the login or registration
    # page, redirect them to the login page
    if cur_user is None:
        login_regex = re.compile(r'/login.*\.html')
        register_regex = re.compile(r'/register.*\.html')
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
    """
    If the user is not logged in, prompt for the user to log in.
    """
    if cur_user is not None:
        flash("You are already logged in.")
        return redirect(url_for("home"))
    return render_template("default_login_page.html")


@app.route("/login/process_login.html", methods=['GET', 'POST'])
def process_login():
    """
    Process the login form from /login.html
    """
    
    username = request.form['username']
    password = request.form['password']

    if username in user_dict:
        if sha256_crypt.verify(password, user_dict[username]):
            global cur_user
            cur_user = username
            return redirect(url_for("home"))

    flash("Username/password combo incorrect.")
    return redirect(url_for("login"))


@app.route("/register.html", methods=['GET', 'POST'])
def register():
    """
    If the user is not logged in, prompt for the user to log in.
    """
    if cur_user is not None:
        flash("You are already logged in.")
        return redirect(url_for("home"))
    return render_template("default_register_page.html")


@app.route("/register/process_register.html", methods=['GET', 'POST'])
def process_register():
    """
    Process the login form from /login.html
    """
    username = request.form['username']
    password = sha256_crypt.hash(request.form['password'])

    if username in user_dict:
        flash("Username already exists.")
        return redirect(url_for("register"))

    user_dict[username] = password
    with open('user_login_data.txt', 'a', encoding="UTF-8") as file:
        file.writelines(username + "," + password)
    return redirect(url_for("home"))


@app.route("/logout.html")
def logout_script():
    """
    Log out the current user.
    """
    global cur_user
    cur_user = None
    flash("Logged out successfully.")
    return redirect(url_for("login"))