from flask import Flask, render_template, request, url_for, session
import requests
import data_manager

app = Flask(__name__)


@app.route("/checkuser", methods=["POST"])
def check_user():
    username = request.form["username"]
    return username


@app.route("/reguser", methods=["POST"])
def register_user():
    username = request.form["username"]
    password = request.form["password"]


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
    return render_template("index.html", planets=planets, prev_page=prev_page, next_page=next_page, planet_keys=planet_keys)


@app.route("/register/")
def register():
    return render_template("registration.html")


app.secret_key = "Egy ocska kalapocska benne csacska macska mocska."

if __name__ == '__main__':
    app.run(debug=True)