from flask import render_template, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, EqualTo, Length
from YourLife import app, db
from YourLife.model import tables, queries
import os

class RegistrationForm(FlaskForm):
    name = StringField('Nome', validators=[InputRequired()])
    surname = StringField('Sobrenome', validators=[InputRequired()])
    username = StringField('Usuário', validators=[Length(min=3)])
    password = PasswordField('Senha', validators=[Length(min=8)])
    password_repeat = PasswordField('Repita sua senha', validators=[EqualTo('password')])
    email = StringField('Email', validators=[Email()])
    submit = SubmitField('Registrar')

@app.route("/register", methods=['GET', 'POST'])
def registerForm():
    form = RegistrationForm()
    message = ""

    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        username = form.username.data.lower()
        password = form.password.data
        email = form.email.data.lower()
        if not queries.email_available(email):
            form.name.data = ""
            form.surname.data = ""
            form.username.data = ""
            form.password.data = ""
            form.email.data = ""
            message = "Esse email já está cadastrado"
        elif not queries.username_available(username):
            form.username.data = ""
            message = "Já existe usuário com esse nome"
        else:
            form.name.data = ""
            form.surname.data = ""
            form.username.data = ""
            form.password.data = ""
            form.email.data = ""
            db.session.add(tables.User(username, password, name, surname, email))
            filepath = 'default.jpg'
            db.session.add(tables.Photo(filepath, username, 0))
            db.session.commit()
            return redirect('/registered')

    return render_template('registerPage.html', form=form, message=message)

@app.route("/registered")
def registered():
    return render_template('registeredPage.html')
