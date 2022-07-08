from flask import render_template, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, EqualTo, Length

from YourLife import app, db
from YourLife.model import tables, queries

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[Length(min=3)])
    password = PasswordField('Senha', validators=[Length(min=8)])
    submit = SubmitField('Entrar')

@app.route("/login", methods=['GET', 'POST'])
def loginForm():
    form = LoginForm()
    message = ""

    if form.validate_on_submit():
        username = form.username.data.lower()
        password = form.password.data
        if queries.login(username, password):
            form.username.data = ""
            form.password.data = ""
            session['username'] = username
            return redirect('/profile/' + username)
        else:
            form.username.data = ""
            form.password.data = ""
            message = 'Usuário ou senha incorretos.'
    return render_template('loginPage.html', form=form, message=message)