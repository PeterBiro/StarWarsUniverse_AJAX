from flask import Flask, render_template, request, url_for, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash

import requests
import data_manager

app = Flask(__name__)

@app.route("/sessionuser", methods=["POST"])
def session_user():
    if "username" in session:
        return session["username"]
    else:
        return ""

@app.route("/checkuser", methods=["POST"])
def check_user():
    username = request.form["username"]
    return data_manager.check_user(username)


@app.route("/reguser", methods=["POST"])
def register_user():
    username = request.form["username"]
    password = request.form["password"]
    data_manager.new_user(username, generate_password_hash(password))
    return "Done"


@app.route("/loguser", methods=["POST"])
def login_user():
    username = request.form["username"]
    password = request.form["password"]
    result = data_manager.login_user(username)
    if (result is not None) and (check_password_hash(result, password)):
        session["username"] = username
        return "OK"
    else:
        return ":("


@app.route("/")
def index():
    page = request.args.get("page")
    if page is None:
        page = "1"
    response = requests.get("http://swapi.co/api/planets/?page={}".format(page))
    planets = response.json()["results"]
    prev_page = response.json()["previous"]
    next_page = response.json()["next"]
    if prev_page is not None:
        prev_page = prev_page[34:]
    if next_page is not None:
        next_page = next_page[34:]
    planet_keys = [
        ("Name", "name"),
        ("Diameter", "diameter"),
        ("Climate", "climate"),
        ("Terrain", "terrain"),
        ("Surface Water Percentage", "surface_water"),
        ("Population", "population"),
        ("Residents", "residents")
    ]
    if "username" in session:
        user = session["username"]
    else:
        user = "guest"
    return render_template("index.html", planets=planets, prev_page=prev_page, next_page=next_page, planet_keys=planet_keys, user=user)

@app.route("/logout/")
def logout():
    session.pop("username")
    return redirect("/", code=302)

@app.route("/register/")
def register():
    if "username" in session:
        user = session["username"]
    else:
        user = "guest"
    return render_template("registration.html", user=user)

@app.route("/login/")
def login():
    if "username" in session:
        user = session["username"]
    else:
        user = "guest"
    return render_template("login.html", user=user)


app.secret_key = "T9T9R76M7NAEI3574HNBPY46C219E7GEXL2O7BWGOX5QFJVWISB33ZUBR8R6XE8Y0EIBSZAOI1IW9LR2"


if __name__ == '__main__':
    app.run(debug=True)
