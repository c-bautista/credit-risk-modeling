from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, IntegerField, SelectField, SelectMultipleField

class Form(FlaskForm):
    age = IntegerField(label='Age (in years)')
    income = FloatField(label='Annual Income (in dollars)')
    person_emp_length = IntegerField(label='Years of employment')
    loan_amnt = FloatField(label='Loan amount (in dollars)')
    int_rate = FloatField(label='Interest rate (in percentage)')
    credit_hist_length = IntegerField(label='Length of credit history (in years)')
    person_home_ownership = SelectField(label='Home ownership')
    loan_intent = SelectField(label='Loan intention')
    loan_grade = SelectField(label='Loan grade')
    past_default = SelectField(label='Have you ever defaulted on a loan?')
    submit = SubmitField(label='Compute')

    person_home_ownership.choices=["RENT", "OWN", "MORTGAGE", "OTHER"]
    loan_intent.choices=["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOME IMPROVEMENT", "DEBT CONSOLIDATION"]
    loan_grade.choices=["A", "B", "C", "D", "E", "F", "G"]
    past_default.choices=["YES", "NO"]
