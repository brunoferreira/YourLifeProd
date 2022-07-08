from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app=Flask(__name__)
app.config.from_object('config')
db=SQLAlchemy(app)
Bootstrap(app)

from YourLife.controler import homePage, registerPage, loginPage, profilePage, logoutPage, editPage, albumPage