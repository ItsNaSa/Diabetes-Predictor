import re
from flask import Flask, Blueprint, render_template, request, flash, redirect
from flask.helpers import url_for
from flask_bootstrap import Bootstrap
from forms import diabetesdataform
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config.update(dict(
    SECRET_KEY="D4E5D124A6074C097A9A4DD39A6197AFD2F2736B",
    WTF_CSRF_SECRET_KEY="3062657BB8605C5BF791641664B38721F27CAC21"
))

@app.route('/', methods=["GET", "POST"])
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
    value = None
    string = ""
    if request.method == "POST" and form.validate():
        pregnancies = form.pregnancies.data
        glucose = form.glucose.data
        bp = form.bp.data
        st = form.st.data
        insulin = form.insulin.data
        bmi = form.bmi.data
        pedigreeFunc = form.diabetesPedigree.data
        age = form.bmi.data
        var = []
        if bmi <= 18.5:
            var = [0,0,0,0,1]
        elif bmi > 18.5 and bmi <= 24.9:
            var = [0,0,0,0,0]
        elif bmi > 24.9 and bmi <= 29.9:
            var = [0,0,0,1,0]
        elif bmi > 29.9 and bmi <= 34.9:
            var = [1,0,0,0,0]
        elif bmi > 34.9 and bmi <= 39.9:
            var = [0,1,0,0,0]
        elif bmi > 39.9:
            var = [0,0,1,0,0]
        scalerLoad = pickle.load(open("scaler.pkl", "rb"))
        modelLoad = pickle.load(open("randomForestModel.sav", "rb"))
        featureList = np.array([pregnancies, glucose, bp, st, insulin, pedigreeFunc, age]).reshape(1, -1)
        
        featureList = scalerLoad.transform(featureList)
        
        BMIVar = np.array(var).reshape(1, -1)
        finalFeatures = np.concatenate((featureList, BMIVar), axis = 1)
        
        value = modelLoad.predict(finalFeatures)
        print("Value = {}".format(value))
        # Logic to predict and redirect to the predicted value display
        if value == 0:
            string = "Congratulations!! You are NOT a diabetic!"
        elif value == 1:
            string = "You are a diabetic! Kindly consult a physician!"
    return render_template('predictorPage.html', form=form, result=string)
