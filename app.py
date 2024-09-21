from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>НГТУ, ФБ, Лабораторные работы</title>
</head>
<body>
    <header>
        НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
    </header>

    <h1>web-сервер на flask</h1>
    <li> <a href="/lab1"> Лабораторная работа 1 </a></li>
    <li> <a href="/lab2"> Лабораторная работа 2 </a></li>
    <footer>
        &copy; Альбинас Гапшис, ФБИ-23, 3 курс, 2024
    </footer>
</body>
</html>
"""

@app.route("/lab1")
def lab1():
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

@app.route("/lab1/oak")
def oak():
    return f'''
<!DOCTYPE html>
<html>
<head>
     <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
</head>
<body>
    <h1>Дуб</h1>
    <img src="{url_for('static', filename='oak.jfif')}">
</body>
</html>
'''

@app.route('/lab1/student')
def student():
    return f'''
<!DOCTYPE html>
<html>
<head>
     <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
</head>
<body>
    <h1>Гапшис Альбинас Альбинович</h1>
    <img src="{url_for('static', filename='logo.jpeg')}">
</body>
</html>
'''

@app.route('/lab1/python')
def python():
    return f'''
<!DOCTYPE html>
<html>
<head>
     <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
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

    <img src="{url_for('static', filename='python.jpeg')}">
</body>
</html>
'''

@app.route('/lab1/about')
def about():
    return f'''
<!DOCTYPE html>
<html>
<head>
     <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
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
    
    <img src="{url_for('static', filename='about.jpeg')}">
</body>
</html>
'''

@app.route('/lab2/example')
def example():
    name = 'Альбинас Гапшис'
    number = '2'
    group = 'ФБИ-23'
    kurs = '3 курс'
    calculation_1 = 5 + 2
    calculation_2 = 11 * 28
    calculation_3 = 8452 / 793
    calculation_4 = 45 ** 8
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    books = [
    {'author': 'Джордж Оруэлл', 'title': '1984', 'genre': 'Антиутопия', 'pages': 328},
    {'author': 'Федор Достоевский', 'title': 'Преступление и наказание', 'genre': 'Классическая литература', 'pages': 671},
    {'author': 'Харпер Ли', 'title': 'Убить пересмешника', 'genre': 'Социальный роман', 'pages': 281},
    {'author': 'Джон Р.Р. Толкин', 'title': 'Властелин Колец', 'genre': 'Фэнтези', 'pages': 1178},
    {'author': 'Маргарет Митчелл', 'title': 'Унесенные ветром', 'genre': 'Исторический роман', 'pages': 1037},
    {'author': 'Агата Кристи', 'title': 'Десять негритят', 'genre': 'Детектив', 'pages': 271},
    {'author': 'Рэй Брэдбери', 'title': 'Fahrenheit 451', 'genre': 'Научная фантастика', 'pages': 249},
    {'author': 'Стивен Кинг', 'title': 'Сияние', 'genre': 'Ужасы', 'pages': 447},
    {'author': 'Ф. Скотт Фицджеральд', 'title': 'Великий Гэтсби', 'genre': 'Классическая литература', 'pages': 180},
    {'author': 'Джейн Остин', 'title': 'Гордость и предубеждение', 'genre': 'Классическая литература', 'pages': 432}
    ]

    return render_template ('example.html', name = name, number = number, 
                            group = group, kurs = kurs, calculation_1 = calculation_1, 
                            calculation_2 = calculation_2, calculation_3 = calculation_3, 
                            calculation_4 = calculation_4, fruits = fruits, books = books)

@app.route ('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/popular-russian-rappers')
def popular_russian_rappers():
    images = [
        {'filename': 'lab2_1.jpg', 'alt': 'Scally Milano', 'caption': 'Scally Milano'},
        {'filename': 'lab2_2.jpeg', 'alt': 'Friendly Thug 52 ngg', 'caption': 'Friendly Thug 52 ngg'},
        {'filename': 'lab2_3.jpeg', 'alt': 'Kai Angel', 'caption': 'Kai Angel'},
        {'filename': 'lab2_4.jpeg', 'alt': 'Shaman', 'caption': 'Shaman'},
        {'filename': 'lab2_5.jpeg', 'alt': 'Maybe Baby', 'caption': 'Maybe Baby'}
    ]
    return render_template('popular_russian_rappers.html', images=images)
