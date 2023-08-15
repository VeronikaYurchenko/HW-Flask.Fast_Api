#Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'


@app.route('/square/', methods=['GET', 'POST'])
def square():
    if request.method == 'POST':
        number = float(request.form.get('number'))
        data = {"number": number, "square": number ** 2}
        return render_template('square.html', data=data)
    return render_template('square.html')


if __name__ == '__main__':
    app.run(debug=True)