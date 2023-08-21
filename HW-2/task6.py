#Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.
from html import escape

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'


@app.route('/check_age/', methods=['GET', 'POST'])
def check_age():
    if request.method == 'POST':
        name = escape(request.form.get('name'))
        age = int(request.form.get('age'))
        if age >= 18:
            return "Можно"
        return "Нельзя"
    return render_template('check_age.html')


if __name__ == '__main__':
    app.run(debug=True)