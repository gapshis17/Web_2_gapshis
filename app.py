from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
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

    <footer>
        &copy; Альбинас Гапшис, ФБИ-23, 3 курс, 2024
    </footer>
</body>
</html>
"""