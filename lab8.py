from flask import Blueprint, redirect, url_for,render_template,request,session

lab8 = Blueprint('lab8', __name__)


@lab8.route("/lab8/")
def lab():
    
    return render_template('/lab8/lab8.html')

@lab8.route('/lab8/register/', methods = ['GET','POST'])
def register():
    return render_template('/lab8/register.html')


@lab8.route('/lab8/login/', methods = ['GET','POST'])
def login():
    return render_template('/lab8/login.html')

@lab8.route('/lab8/articles/')
def article_list():
    return render_template('/lab8/articles.html')

@lab8.route('/lab8/articles/create', methods=['GET', 'POST'])
def create_article():
    return redirect('/lab8/articles')
