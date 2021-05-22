import re
from flask import Flask, Blueprint, render_template, request, flash, redirect
from flask.helpers import url_for
from flask_bootstrap import Bootstrap
from forms import diabetesdataform
import pickle

import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config.update(dict(
    SECRET_KEY="D4E5D124A6074C097A9A4DD39A6197AFD2F2736B",
    WTF_CSRF_SECRET_KEY="3062657BB8605C5BF791641664B38721F27CAC21"
))

@app.route('/')
def index():
    return redirect(url_for('home'))

# Home page
@app.route('/home')
def home():
    return render_template('index.html')

# Page to accept the values
@app.route('/predictor', methods=["GET", "POST"])
def predictor():
    form = diabetesdataform(request.form)
    if request.method == "POST" and form.validate():
        print("hello")
    # Logic to predict and redirect to the predicted value display
    return render_template('predictorPage.html', form=form)
