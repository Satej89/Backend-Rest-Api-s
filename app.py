from flask import Flask
app=Flask(__name__)

if __name__ == '__main__':
    app.debug = True
    app.run()
@app.route("/")
def welcome():
    return "heyyyyyyyyyyyyyy"
@app.route("/home")
def home():
    return "welcome toooo the home page"
from controller import * 