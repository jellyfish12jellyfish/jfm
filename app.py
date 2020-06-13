import secrets

from flask import Flask
from flask import render_template, request, jsonify
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

# app.config["RECAPTCHA_PUBLIC_KEY"] = cfg.pub
# app.config["RECAPTCHA_PRIVATE_KEY"] = cfg.pk

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projects')
def get_projects():
    return render_template('projects.html')


@app.route('/team')
def get_team():
    return render_template('team.html')


@app.route('/contact')
def get_contact():
    return render_template('contact_us.html')


@app.route('/first-job')
def get_job():
    return render_template('job.html')


@app.route('/process', methods=['POST'])
def process():
    email = request.form['email']
    msg = request.form['msg']
    number = request.form['number']
    date = request.form['date']

    if email and msg:
        message = Message(f'{email} send a message', sender=email, recipients=['grinvichforum10@mail.ru'])
        message.html = f'<b>EMAIL:</b>{email} <br> <b>BUDGET:</b> {number} <br> <b>MESSAGE:</b> {msg}, <br> DATE: {date}'
        mail.send(message)
        return jsonify({'success': 'Ваша форма успешно отправлена!'})
    return jsonify(
        {'error': 'Что-то пошло не так! Скорее всего, вы заполнили не все поля или ввели некорректные данные'})


if __name__ == '__main__':
    app.run()
