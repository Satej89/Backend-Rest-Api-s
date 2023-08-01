from flask import Flask
app=Flask(__name__)

@app.route("/")
def welcome():
    return "heyyyyyyyyyyyyyy"
@app.route("/home")
def home():
    return "welcome toooo the home page"
from controller import * 