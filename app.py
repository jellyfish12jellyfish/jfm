import secrets

from flask import Flask
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_mail import Mail, Message

import cfg

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


@app.route('/')
def index():
    return render_template('contact.html')


@app.route('/process', methods=['POST'])
def process():
    email = request.form['email']
    name = request.form['name']
    msg = request.form['msg']
    number = request.form['number']

    if name and email and msg:
        print(name)
        print(email)
        print(msg)
        print(number)
        message = Message(f'{name} send a message', sender=email, recipients=['grinvichforum10@mail.ru'])
        message.html = f'<b>EMAIL:</b>{email} <br> <b>BUDGET:</b> {number} <br> <b>MESSAGE:</b> {msg}'
        mail.send(message)
        return jsonify({'success': 'Success!'})
    return jsonify({'error': 'Missing data!'})


# debug
# export FLASK_ENV=development
# flask run
if __name__ == '__main__':
    app.run()
