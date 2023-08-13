# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    context = {'title': 'Main'}
    return render_template('index.html', **context)


@app.route('/about/')
def info():
    context = {'title': 'About'}
    return render_template('about.html', **context)


@app.route('/contacts/')
def contacts():
    context = {'title': "Contacts"}
    return render_template('contacts.html', **context)


@app.route('/clothes/')
def clothes():
    context = {'title': 'Clothes'}
    return render_template('store_clothes.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'title': 'shoes'}
    return render_template('store_shoes.html', **context)


@app.route('/jacket/')
def jacket():
    context = {'title': 'Jacket'}
    return render_template('store_jacket.html', **context)


if __name__ == '__main__':
    app.run()
