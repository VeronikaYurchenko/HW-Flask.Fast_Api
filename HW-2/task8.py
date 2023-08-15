# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".
from html import escape

from flask import Flask, redirect, url_for, request, render_template, flash

app = Flask(__name__)

app.secret_key = '8b1d721a6643af2da67110bf2583582d5f3a399dbeca2d365b8ba175dffddc42'


@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'


@app.route('/flask/', methods=['GET', 'POST'])
def flask():
    if request.method == 'POST':
        name = escape(request.form.get('name'))
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('flask'))
    return render_template('flask.html')


if __name__ == '__main__':
    app.run(debug=True)
