from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/total", methods=["GET", "POST"])
def total():
    bill = request.form.get("bill")
    tip = request.form.get("tip")
    bill = float(bill)
    tip = float(tip)
    total = bill * (tip * 0.01)

    return render_template("index.html", total=total)