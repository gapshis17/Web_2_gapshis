from flask import Blueprint, render_template, redirect, url_for, request
from db import db
from db.models import users, articles
from werkzeug.security import generate_password_hash

lab8 = Blueprint('lab8', __name__)


@lab8.route('/lab8/')
def index():
    return render_template('lab8/index.html')


@lab8.route('/lab8/login', methods=['GET', 'POST'])
def login():
    return render_template('lab8/login.html')


@lab8.route('/lab8/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')

    login_form = request.form.get('login')
    password_form = request.form.get('password')

    # Проверка на пустые поля
    if not login_form or not password_form:
        error = "Заполните все поля"
        return render_template('lab8/register.html', error=error)

    # Проверка на существование логина
    login_exists = users.query.filter_by(login=login_form).first()
    if login_exists:
        error = "Такой пользователь уже существует"
        return render_template('lab8/register.html', error=error)

    # Хеширование пароля
    password_hash = generate_password_hash(password_form)

    # Создание нового пользователя
    try:
        new_user = users(login=login_form, password=password_hash)
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        # Обработка ошибки при добавлении в базу данных
        error = f"Ошибка при регистрации: {str(e)}"
        return render_template('lab8/register.html', error=error)

    # Перенаправление на главную страницу после успешной регистрации
    return redirect('/lab8/')


@lab8.route('/lab8/articles', methods=['GET'])
def articles():
    return render_template('lab8/articles.html')


@lab8.route('/lab8/create', methods=['GET', 'POST'])
def create():
    return render_template('lab8/create.html')