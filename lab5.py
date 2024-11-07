from flask import Blueprint, render_template, request, make_response, redirect, session
import traceback

lab5 = Blueprint('lab5', __name__)

@lab5.route('/lab5/')
def lab():
    return render_template('lab5/index.html')

@lab5.route('/lab5/login')
def login():
    return render_template('lab5/login.html')

@lab5.route('/lab5/register')
def register():
    return render_template('lab5/register.html')

@lab5.route('/lab5/list')
def list():
    return render_template('lab5/list.html')

@lab5.route('/lab5/create')
def create():
    return render_template('lab5/create.html')
