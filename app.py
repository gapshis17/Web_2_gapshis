from flask import Flask, redirect, url_for, render_template
from lab1 import lab1
app = Flask(__name__)
app.register_blueprint(lab1)

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

@app.route('/lab2/popular_russian_rappers')
def popular_russian_rappers():
    images = [
        {'filename': 'lab2_1.jpg', 'alt': 'Scally Milano', 'caption': 'Scally Milano'},
        {'filename': 'lab2_2.jpeg', 'alt': 'Friendly Thug 52 ngg', 'caption': 'Friendly Thug 52 ngg'},
        {'filename': 'lab2_3.jpeg', 'alt': 'Kai Angel', 'caption': 'Kai Angel'},
        {'filename': 'lab2_4.jpeg', 'alt': 'Shaman', 'caption': 'Shaman'},
        {'filename': 'lab2_5.jpeg', 'alt': 'Maybe Baby', 'caption': 'Maybe Baby'}
    ]
    return render_template('popular_russian_rappers.html', images=images)
