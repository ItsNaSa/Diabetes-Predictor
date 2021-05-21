from flask import Flask, render_template, request, flash, redirect
from flask.helpers import url_for
from flask_wtf import FlaskForm
from wtforms import Form, validators, IntegerField, DecimalField, SubmitField
import os

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="D4E5D124A6074C097A9A4DD39A6197AFD2F2736B",
    WTF_CSRF_SECRET_KEY="3062657BB8605C5BF791641664B38721F27CAC21"
))

class diabetesdataform(FlaskForm):
    pregnancies = IntegerField("Number of pregnancies", [validators.Required("Please enter your number of pregnancies")])
    glucose = IntegerField("Your glucose level", [validators.Required("Please enter your glucose level")])
    bp = IntegerField("Your blood pressure", [validators.Required("Please enter your Blood pressure")])
    st = IntegerField("Your Skin Thickness", [validators.Required("Enter the skin thickness")])
    insulin = IntegerField("Insulin", [validators.Required("Enter insulin level")])
    bmi = DecimalField("BMI", [validators.Required("Enter your BMI")])
    age = IntegerField("Age", [validators.Required("Enter your age")])
    submit = SubmitField("Predict")

@app.route('/')
def index():
    return redirect(url_for('home'))

# Home page
@app.route('/home')
def home():
    return render_template('index.html')

# Page to accept the values
@app.route('/predictor', methods=["POST"])
def predictor():
    form = diabetesdataform()
    # Logic to predict and redirect to the predicted value display
    return render_template('predictorPage.html', form=form)
