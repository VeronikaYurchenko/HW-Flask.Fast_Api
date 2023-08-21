# №5. Создать форму регистрации для пользователя. Форма должна содержать поля: имя, электронная почта, пароль (с подтверждением), дата рождения, согласие на
# обработку персональных данных. Валидация должна проверять, что все поля заполнены корректно (например, дата рождения должна быть в
# формате дд.мм.гггг).  При успешной регистрации пользователь должен быть
# перенаправлен на страницу подтверждения регистрации.
# №8.Создать форму для регистрации пользователей на сайте.
#  Форма должна содержать поля "Имя", "Фамилия", "Email",
# "Пароль" и кнопку "Зарегистрироваться".
#  При отправке формы данные должны сохраняться в базе
#  данных, а пароль должен быть зашифрован.

from flask import Flask, render_template, request, flash, redirect, url_for
import os
from config import Config
from models import db, User, User2
from flask_wtf.csrf import CSRFProtect
from forms import Registration2Form, Registration3Form

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
csrf = CSRFProtect(app)

category = [
    {"title": 'Home page', "func_name": 'index'},
    {"title": 'Registration 2', "func_name": 'registration2'},
    {"title": 'Registration 3', "func_name": 'registration3'}
]


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', category=category)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/registration2/', methods=['GET', 'POST'])
def registration2():
    form = Registration2Form()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        username = form.username.data.lower()
        email = form.email.data
        date = form.date_of_birth.data
        user = User(username=username, email=email, date_of_birth=date)
        if User.query.filter(User.username == username).first() or User.query.filter(User.email == email).first():
            flash(f'Пользователь с username {username} или e-mail {email} уже существует')
            return redirect(url_for('registration2'))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Вы успешно зарегистрировались!')
        return redirect(url_for('registration2'))
    return render_template('registration2.html', form=form)


@app.route('/registration3/', methods=['GET', 'POST'])
def registration3():
    form = Registration3Form()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        name = form.name.data.lower()
        surname = form.surname.data.lower()
        email = form.email.data
        user = User2(name=name, surname=surname, email=email)
        if User2.query.filter(User2.email == email).first():
            flash(f'Пользователь с e-mail {email} уже существует')
            return redirect(url_for('registration'))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Вы успешно зарегистрировались!')
        return redirect(url_for('registration3'))
    return render_template('registration3.html', form=form)


if __name__ == '__main__':
    app.run()