from django.shortcuts import render
from flask import Flask, render_template
import sqlalchemy 
from flask_sqlalchemy import  SQLAlchemy


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True,port=9090)