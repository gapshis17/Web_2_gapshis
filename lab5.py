from flask import Blueprint, render_template, request, make_response, redirect, session
import traceback
import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash

lab5 = Blueprint('lab5', __name__)


@lab5.route('/lab5/')
def lab():
    return render_template('lab5/index.html', login = session.get('login'))


def db_connect():
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='albinas_gapshis_konwledge_base',
        user='albinas_gapshis_konwledge_base',
        password='123'
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()


@lab5.route('/lab5/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab5/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not login or not password:
        error_message = 'Заполните все поля!'
        return render_template('lab5/login.html', error=error_message)

    try:
        conn, cur = db_connect()
        
        cur.execute("SELECT login, password FROM users WHERE login = %s;", (login,))
        user = cur.fetchone()

        if not user:
            db_close(conn, cur)
            return render_template('lab5/login.html', error='Логин и/или пароль не верны')
        
        if not check_password_hash(user['password'], password):
            db_close(conn, cur)
            return render_template('lab5/login.html', error='Логин и/или пароль не верны')

        db_close(conn, cur)

        # Устанавливаем логин пользователя в сессию
        session['login'] = login

        return render_template('lab5/success_login.html', login=login)

    except psycopg2.Error as e:
        # Логирование ошибки
        print(f"Ошибка при работе с базой данных: {e}")
        return render_template('lab5/login.html', error='Ошибка при входе. Попробуйте позже.')



@lab5.route('/lab5/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')

    login = request.form.get('login')
    password = request.form.get('password')

    # Проверка наличия логина и пароля
    if not login or not password:
        error_message = 'Заполните все поля!'
        if not login:
            error_message = 'Логин не может быть пустым!'
        elif not password:
            error_message = 'Пароль не может быть пустым!'
        return render_template('lab5/register.html', error=error_message)

    try:
        conn, cur = db_connect()
        
        # Проверка на существование пользователя
        cur.execute("SELECT login FROM users WHERE login = %s;", (login,))
        if cur.fetchone():
            db_close(conn, cur)
            return render_template('lab5/register.html', error='Такой пользователь уже существует')

        password_hash = generate_password_hash(password)
        # Добавление нового пользователя
        cur.execute("INSERT INTO users (login, password) VALUES (%s, %s);", (login, password_hash))
        db_close(conn, cur)

        return render_template('lab5/success.html', login=login)

    except Exception as e:
        # Предоставляем сообщение об ошибке пользователю
        return render_template('lab5/register.html', error='Ошибка регистрации: ' + str(e))

@lab5.route('/lab5/list')
def list():
    return render_template('lab5/list.html')


@lab5.route('/lab5/create')
def create():
    return render_template('lab5/create.html')
