import os

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import get_users, hash_password

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index(message=''):    
    if 'username' in session:
        message = f"Logged in as {session['username']}"
    else:
        message = 'You are not logged in'
    return render_template("index.html", title="Index", message=message)


@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/newuser", methods=["GET", "POST"])
def newuser():
    error = request.args.get('error') == 'True'
    if request.method == 'POST':
        user = (request.form['username'])
        error = True
    return render_template("newuser.html", error=error)


@app.route("/cdci")
def cdci():
    return render_template("cdci.html", title="CDCI")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = request.args.get('error') == 'True'
    if request.method == 'POST':
        user = (request.form['username'], hash_password(request.form['password']))
        users = get_users()
        if user[0] in users.keys():
            hash = users.get(user[0])
            if hash == user[1]:
                session['username'] = request.form['username']
                print (session.values())
                return redirect(url_for('dashboard'))
        error = True
    return render_template('login.html', error=error)


@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html', username=session['username'])
    


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

