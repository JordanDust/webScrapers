
from flask import Flask, redirect, url_for, render_template, request
from webScraper import *

app = Flask(__name__)
product = ""
webType = ""
sOrE = ""


    # Defining the home page of our site
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
	product = request.form["stockOrProduct"]
        return redirect(url_for("result"))
    else:
	    return render_template("website.html")
    
    
    

@app.route("/result")
def result():
    if sOrE == "stock":
        runStock(product)
    else:
        runPrices("all", product)
    return f"<p>Info {getVars(webType, gui)}</p>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
	return redirect(url_for("home"))


def getProduct():
    return product



if __name__ == "__main__":
    app.run()
