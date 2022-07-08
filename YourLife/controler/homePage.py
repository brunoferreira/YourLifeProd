from flask import render_template
from YourLife import app
from YourLife.model import queries

@app.route("/")
def index():
    return render_template('homePage.html')