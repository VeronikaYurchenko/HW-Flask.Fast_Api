# Создать базовый шаблон для всего сайта, содержащий
# общие элементы дизайна (шапка, меню, подвал), и
# дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты",
# используя базовый шаблон.
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'Main'}
    return render_template('index.html', **context)


@app.route('/about/')
def about():
    context = {'title': 'About'}
    return render_template('about.html', **context)


@app.route('/contacts/')
def contacts():
    context = {'title': 'Contacts'}
    return render_template('contacts.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
