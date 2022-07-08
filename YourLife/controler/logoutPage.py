from flask import render_template, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, EqualTo, Length

from YourLife import app, db
from YourLife.model import tables, queries

@app.route("/logout")
def logout():
    try:
        session.pop('username')
    except:
        pass
    return render_template('logoutPage.html')
