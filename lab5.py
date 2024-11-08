from flask import Blueprint, render_template, request, make_response, redirect, session
import traceback
import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

lab5 = Blueprint('lab5', __name__)


@lab5.route('/lab5/')
def lab():
    return render_template('lab5/index.html', login = session.get('login'))


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
        conn = psycopg2.connect(
            host='127.0.0.1',
            database='albinas_gapshis_konwledge_base',
            user='albinas_gapshis_konwledge_base',
            password='123'
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute("SELECT login, password FROM users WHERE login = %s;", (login,))
        user = cur.fetchone()

        if not user:
            cur.close()
            conn.close()
            return render_template('lab5/login.html', error='Логин и/или пароль не верны')
        
        if user['password'] != password:
            cur.close()
            conn.close()
            return render_template('lab5/login.html', error='Логин и/или пароль не верны')

        cur.close()
        conn.close()

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
        # Подключение к базе данных
        conn = psycopg2.connect(
            host='127.0.0.1',
            database='albinas_gapshis_konwledge_base',
            user='albinas_gapshis_konwledge_base',
            password='123'
        )
        cur = conn.cursor()
        
        # Проверка на существование пользователя
        cur.execute(sql.SQL("SELECT login FROM users WHERE login = %s;"), (login,))
        if cur.fetchone():
            return render_template('lab5/register.html', error='Такой пользователь уже существует')

        # Добавление нового пользователя
        cur.execute(sql.SQL("INSERT INTO users (login, password) VALUES (%s, %s);"), (login, password))
        conn.commit()
        return render_template('lab5/success.html', login=login)

    except Exception as e:
        # Предоставляем сообщение об ошибке пользователю
        return render_template('lab5/register.html', error='Ошибка регистрации: ' + str(e))
    
    finally:
        # Закрытие курсора и соединения
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()


# @lab5.route('/lab5/register', methods = ['GET', 'POST'])
# def register():
#     if request.method == 'GET':
#         return render_template('lab5/register.html')
    
#     login = request.form.get('login')
#     password = request.form.get('password')

#     if not (login or password):
#         return render_template('lab5/register.html', error='Заполните все поля!')

#     if not login:
#         return render_template('lab5/register.html', error='Логин не может быть пустым!')

#     if not password:
#         return render_template('lab5/register.html', error='Пароль не может быть пустым!')

#     conn = psycopg2.connect(
#         host = '127.0.0.1',
#         database = 'albinas_gapshis_konwledge_base',
#         user = 'albinas_gapshis_konwledge_base',
#         password = '123'
#     )
#     cur = conn.cursor()

#     cur.execute(f"SELECT login FROM users WHERE login='{login}';")
#     if cur.fetchone():
#         cur.close()
#         conn.close()
#         return render_template('lab5/register.html',
#                                 error = 'Такой пользователь уже существует')

#     cur.execute(f"INSERT INTO users (login, password) VALUES ('{login}', '{password}');")
#     conn.commit()
#     cur.close()
#     conn.close()          
#     return render_template('lab5/success.html', login=login)


@lab5.route('/lab5/list')
def list():
    return render_template('lab5/list.html')


@lab5.route('/lab5/create')
def create():
    return render_template('lab5/create.html')
