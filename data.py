from flask import Flask, render_template, request, redirect, flash, url_for, session, logging

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("index.html")

if __name__ == " __main__":
    appplication.run(debug=True)