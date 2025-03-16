import re
from datetime import datetime
from flask import Flask, render_template, request
import linearRegression601N

app = Flask(__name__)

@app.route("/")
def home():
    return "Ingenieria de sistemas, Flask, ¡bienvenidos!"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    match_object = re.match("[a-zA-Z]+", name)
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"
    content = "Hello there, " + clean_name + "! Hour: " + str(now)
    return content

@app.route("/examplehtml")
def examplehtml():
    return render_template("example.html")

@app.route("/linearRegression", methods=["GET", "POST"])
def calculateGrade():
    predictResult = None
    if request.method == "POST":
        hours = float(request.form["hours"])
        predictResult = linearRegression601N.calculateGrade(hours)[0] # Extrae el valor numérico
    return render_template("linearRegressionGrades.html", result=predictResult)
