import secrets

from flask import Flask
from flask import render_template, flash, redirect, url_for
from flask_mail import Mail, Message

import cfg
from forms import ContactForm

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
app.config.update(dict(
    MAIL_SERVER=cfg.mail_srv,
    MAIL_PORT=cfg.mail_port,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=cfg.mail_user,
    MAIL_PASSWORD=cfg.mail_pass, ))

app.config["RECAPTCHA_PUBLIC_KEY"] = cfg.pub
app.config["RECAPTCHA_PRIVATE_KEY"] = cfg.pk

mail = Mail(app)


@app.route('/', methods=['get', 'post'])
def index():
    return render_template('index.html')


@app.route('/contact/', methods=['get', 'post'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        tz = form.tz.data
        name = form.name.data
        email = form.email.data
        message = form.message.data
        msg = Message(f'{name} leave you message', sender=email,
                      recipients=['grinvichforum10@mail.ru'])
        msg.html = f'{email}: <h3>{message}</h3> <br> {tz}'
        mail.send(msg)
        flash('Success!', category='success')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)


# debug
# export FLASK_ENV=development
# flask run
if __name__ == '__main__':
    app.run()
