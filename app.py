from flask import Flask, request
from flask import render_template, redirect, url_for
from forms import ContactForm
import secrets
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
app.config.update(dict(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME='',
    MAIL_PASSWORD='', ))

mail = Mail(app)


@app.route('/', methods=['get', 'post'])
def index():
    return render_template('index.html')


@app.route('/contact/', methods=['get', 'post'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        msg = Message(f'{name} ({email}) leave you message: {message}', sender=email,
                      recipients=[''])
        mail.send(msg)
        return 'Success!'
    return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
