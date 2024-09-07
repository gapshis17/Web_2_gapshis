from flask import Flask, redirect, url_for
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
    <footer>
        &copy; Альбинас Гапшис, ФБИ-23, 3 курс, 2024
    </footer>
</body>
</html>
"""
@app.route("/lab1/oak")
def oak():
    return '''
<!DOCTYPE html>
<html>
<head>
     <link rel="stylesheet" href="{{ url_for('static', filename='lab1.css') }}">
</head>
<body>

    <h1>Дуб</h1>
    <img src="''' + url_for('static', filename='oak.jfif') +'''">
</body>
</html>
'''