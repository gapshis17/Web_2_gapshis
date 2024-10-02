from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)


@lab1.route("/lab1")
def lab():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Гапшис Аьбинас Альбинович, Лабораторная 1</title>
</head>
<body>
    <header>
        НГТУ, ФБ, лабораторная работа 1
    </header>

    <h1>web-сервер на flask</h1>
    <div>
        Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов веб-приложений, сознательно предоставляющих лишь самые ба-
        зовые возможности.
    </div>
    <li> <a href="/menu"> Меню </a></li>
    <h2>Реализованные роуты</h2>
    <li> <a href="/lab1/oak"> Дуб </a></li>
    <li> <a href="/lab1/student"> Student </a></li>
    <li> <a href="/lab1/python"> Python </a></li>
    <li> <a href="/lab1/about"> About </a></li>
    

    <footer>
        &copy; Альбинас Гапшис, ФБИ-23, 3 курс, 2024
    </footer>
</body>
</html>
"""


@lab1.route("/lab1/oak")
def oak():
    return f'''
<!DOCTYPE html>
<html>
<head>
     <link rel="stylesheet" href="{url_for('static', filename='lab1/lab1.css')}">
</head>
<body>
    <h1>Дуб</h1>
    <img src="{url_for('static', filename='lab1/oak.jfif')}">
</body>
</html>
'''

@lab1.route('/lab1/student')
def student():
    return f'''
<!DOCTYPE html>
<html>
<head>
     <link rel="stylesheet" href="{url_for('static', filename='lab1/lab1.css')}">
</head>
<body>
    <h1>Гапшис Альбинас Альбинович</h1>
    <img src="{url_for('static', filename='lab1/logo.jpeg')}">
</body>
</html>
'''


@lab1.route('/lab1/python')
def python():
    return f'''
<!DOCTYPE html>
<html>
<head>
     <link rel="stylesheet" href="{url_for('static', filename='lab1/lab1.css')}">
</head>
<body>
    <h1>Python</h1>

    <p>Python - это высокоуровневый язык программирования общего назначения, который известен 
    своей простотой и читаемостью. Он используется в различных областях, включая веб-разработку, 
    научные вычисления, машинное обучение и автоматизацию.</p>

    <p>Одним из ключевых преимуществ Python является его большой и активный сообщество разработчиков, 
    которое предоставляет обширный набор библиотек и инструментов. Это делает его идеальным языком 
    для начинающих, а также для опытных программистов.</p>

    <p>Python также известен своей гибкостью и кроссплатформенностью. Он работает на различных 
    операционных системах, таких как Windows, macOS, Linux и Unix.</p>

    <img src="{url_for('static', filename='lab1/python.jpeg')}">
</body>
</html>
'''


@lab1.route('/lab1/about')
def about():
    return f'''
<!DOCTYPE html>
<html>
<head>
     <link rel="stylesheet" href="{url_for('static', filename='lab1/lab1.css')}">
</head>
<body>
    <h1>О работе</h1>

    <h2>Цель лабораторной работы</h2>
    <p>Научиться создавать простейшие страницы на Flask.>
    <h2>Задания</h2>
    <p>В этой лабораторной работе мы узнаем, как создать простейшие страницы с
    помощью фреймворка Flask.</p>

    <p>В ходе выполнения лабораторной работы необходимо выполнить:</p>
    <li>установить Flask и необходимые пакеты,</li>
    <li>создать репозиторий на github,</li>
    <li>создать простейшие страницы.</li>
    
    <img src="{url_for('static', filename='lab1/about.jpeg')}">
</body>
</html>
'''