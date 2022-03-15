import os
from flask import Flask, render_template, redirect, url_for, request
from forms.forms import Form 
#import random
#import string
#from func.plots import analysis_param
#from flaskext.markdown import Markdown
import pandas as pd
import joblib

app = Flask(__name__)
app.config.from_object(__name__)
SECRET_KEY=os.urandom(32)
app.config['SECRET_KEY']=SECRET_KEY
#plots_folder=os.path.join('static')

#Markdown(app)

@app.route('/', methods=["GET", "POST"])
def home():
    form=Form()
    form.person_home_ownership.choices=["RENT", "OWN", "MORTGAGE", "OTHER"]
    form.loan_intent.choices=["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOME IMPROVEMENT", "DEBT CONSOLIDATION"]
    form.loan_grade.choices=["A", "B", "C", "D", "E", "F", "G"]
    form.past_default.choices=["YES", "NO"]

    if form.validate_on_submit():
        age=form.age.data
        income=form.income.data
        person_home_ownership=form.person_home_ownership.data
        person_emp_length=form.person_emp_length.data
        loan_intent=form.loan_intent.data
        loan_grade=form.loan_grade.data
        loan_amnt=form.loan_amnt.data
        loan_int_rate=form.int_rate.data
        person_default_on_file=form.past_default.data
        person_cred_hist_length=form.credit_hist_length.data

        dictionary={'person_age':[age], 'person_income':[income], 'person_home_ownership':[person_home_ownership],\
            'person_emp_length':[person_emp_length], 'loan_intent': [loan_intent.replace(' ', '')], 'loan_grade':[loan_grade],\
            'loan_amnt':[loan_amnt], 'loan_int_rate':[loan_int_rate], 'cb_person_default_on_file': [person_default_on_file[0]],\
            'cb_person_cred_hist_length':[person_cred_hist_length]}
        test=pd.DataFrame(dictionary)
        model=joblib.load('final_model.sav')
        pred_default_proba=model.predict_proba(test)[0][1]
        if pred_default_proba>0.234:
            status='DENIED'
        else: status='ACCEPTED'
                
        return redirect(url_for('result', age=age, income=income, home_own=person_home_ownership, emp_len=person_emp_length,\
                intent=loan_intent, grade=loan_grade, amnt=loan_amnt, int_rate=loan_int_rate, past_defa=person_default_on_file,\
                cred_len=person_cred_hist_length, status=status))
    return render_template('home.html', form_single=form)

@app.route('/result', methods=['GET', 'POST'])
def result():
    age=request.args['age']
    income=request.args['income']
    home_own=request.args['home_own']
    emp_len=request.args['emp_len']
    intent=request.args['intent']
    grade=request.args['grade']
    amnt=request.args['amnt']
    int_rate=request.args['int_rate']
    past_defa=request.args['past_defa']
    cred_len=request.args['cred_len']

    status=request.args['status']

    return render_template('result.html', age=age, income=income, home_own=home_own, emp_len=emp_len, intent=intent,\
            grade=grade, amnt=amnt, int_rate=int_rate, past_defa=past_defa, cred_len=cred_len, status=status)


if __name__=="__main__":
    app.run(host='0.0.0.0')
