from flask import Blueprint, redirect, url_for,render_template,request,session
from db import db
from db.models import users,articles
from werkzeug.security import check_password_hash, generate_password_hash


lab8 = Blueprint('lab8', __name__)


@lab8.route("/lab8/")
def lab():
    
    return render_template('/lab8/lab8.html')

@lab8.route('/lab8/register/', methods = ['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')
    
    login_form = request.form.get('login')
    password_form = request.form.get('password')

    if not login_form or not password_form:
        return render_template('lab8/register.html', error='Все поля должны быть заполнены')

    login_exists = users.query.filter_by(login = login_form).first()
    if login_exists:
        return render_template('lab8/register.html', error = 'Такой пользователь уже существует')
    
    password_hash = generate_password_hash(password_form)
    new_user = users(login = login_form, password = password_hash)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/lab8/')


@lab8.route('/lab8/login/', methods = ['GET','POST'])
def login():
    return render_template('/lab8/login.html')

@lab8.route('/lab8/articles/')
def article_list():
    return render_template('/lab8/articles.html')

@lab8.route('/lab8/articles/create', methods=['GET', 'POST'])
def create_article():
    return redirect('/lab8/articles')
