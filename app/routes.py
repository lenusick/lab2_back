from app import app

from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Alex"}
    return render_template("index.html", user=user)

@app.route('/500')
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("error500.html"), 500