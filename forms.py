from wtforms import validators, IntegerField, DecimalField, SubmitField
from flask_wtf import FlaskForm

class diabetesdataform(FlaskForm):
    pregnancies = IntegerField("Number of pregnancies", [validators.Required("Please enter your number of pregnancies")])
    glucose = IntegerField("Your glucose level", [validators.Required("Please enter your glucose level")])
    bp = IntegerField("Your blood pressure", [validators.Required("Please enter your Blood pressure")])
    st = IntegerField("Your Skin Thickness", [validators.Required("Enter the skin thickness")])
    insulin = IntegerField("Insulin", [validators.Required("Enter insulin level")])
    bmi = DecimalField("BMI", [validators.Required("Enter your BMI")])
    diabetesPedigree = DecimalField("Diabetes Pedigree function", [validators.Required("Enter the Diabetes pedigree function")])
    age = IntegerField("Age", [validators.Required("Enter your age")])
    