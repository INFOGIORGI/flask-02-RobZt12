from flask import Flask,render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    nomi = ["Roberto","Alberto","Samuele","Francesco"]
    i = (random.random()) % 4
    return render_template("index.html",titolo = "Homepage",nome = random.choice(nomi))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

app.run(debug=True)
