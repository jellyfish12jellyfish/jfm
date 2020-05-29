from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):

    name = StringField('Name: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    message = TextAreaField('Message: ', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')
    tz = StringField()
