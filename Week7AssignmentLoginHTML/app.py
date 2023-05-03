"""A web applicate using Flask.
Charles Kresho, 05/02/23
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

CUR_USER = None
user_dict = {}

# Creates a new file if one doesn't exist.
try:
    with open('user_login_data.txt', 'r', encoding="UTF-8") as file:
        while True:
            # For each line, extract the username and hashed password
            line = file.readline()
            line = line.strip()
            if len(line) == 0:  # Exit reading file when end of file reached
                break
            split_line = line.split(',')
            user_dict[split_line[0]] = split_line[1]
except FileNotFoundError:
    create_file = open('user_login_data.txt', 'w', encoding="UTF-8")
    create_file.close()


# This function is called before each request to the page.
@app.before_request
def check_for_login_session():
    """
    Checks to ensure that either the user is logged in, or they are trying to access a login page.
    """

    # If the user is not logged in and is not trying ot access either the login or registration
    # page, redirect them to the login page
    if CUR_USER is None:
        # The regex here matches any subpage of login or register
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
    if CUR_USER is not None:
        flash("You are already logged in.")
        return redirect(url_for("home"))
    return render_template("default_login_page.html")


# Should probably be in the scripts folder...
@app.route("/login/process_login.html", methods=['GET', 'POST'])
def process_login():
    """
    Process the login form from /login.html
    """

    username = request.form['username']
    password = request.form['password']

    # If the user exists and the password matches, log in and redirect to home
    if username in user_dict:
        if sha256_crypt.verify(password, user_dict[username]):
            global CUR_USER
            CUR_USER = username
            return redirect(url_for("home"))

    # Otherwise, error and return to login
    flash("Username/password combo incorrect.")
    return redirect(url_for("login"))


# Registration page
@app.route("/register.html", methods=['GET', 'POST'])
def register():
    """
    If the user is not logged in, prompt for the user to log in.
    """
    if CUR_USER is not None:
        flash("You are already logged in.")
        return redirect(url_for("home"))
    return render_template("default_register_page.html")


# Process registration (should probably be put in scrits folder...)
@app.route("/register/process_register.html", methods=['GET', 'POST'])
def process_register():
    """
    Process the login form from /login.html
    """
    username = request.form['username']
    password = request.form['password']

    # If username already exists, display error.
    if username in user_dict:
        flash("Username already exists.")
        return redirect(url_for("register"))

    # Check for and display errors relating to any password requirements.
    valid_password = True
    if len(password) < 12:
        valid_password = False
        flash("Password must be 12 characters in length.")
    if not re.compile(r'\W+', re.ASCII).search(password):
        valid_password = False
        flash("Password contain at least one special character.")
    if not re.compile(r'[a-z]+', re.ASCII).search(password):
        valid_password = False
        flash("Password must contain at least one lower case letter.")
    if not re.compile(r'[A-Z]+', re.ASCII).search(password):
        valid_password = False
        flash("Password must contain at least one upper case letter.")

    # If the password is valid, add it to the file and dictionary
    if valid_password:
        user_dict[username] = sha256_crypt.hash(password)
        with open('user_login_data.txt', 'a', encoding="UTF-8") as file:
            file.writelines(username + "," + user_dict[username])
        flash("Account created successfully.")
        return redirect(url_for("home"))

    # On an invalid password, return to the register page (with the errors)
    return redirect(url_for("register"))


# Logout script (should probably be in the script folder...)
@app.route("/logout.html")
def logout_script():
    """
    Log out the current user.
    """
    global CUR_USER
    CUR_USER = None
    flash("Logged out successfully.")
    return redirect(url_for("login"))
