from flask import Flask, Blueprint, render_template, request, make_response, redirect, session, url_for, current_app
import traceback
import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
import os
from os import path

lab6 = Blueprint('lab6', __name__)

@lab6.route('/lab6/')
def main():
    return render_template('lab6/lab6.html')

def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':    
        conn = psycopg2.connect(
            host='127.0.0.1',
            database='albinas_gapshis_konwledge_base',
            user='albinas_gapshis_konwledge_base',
            password='123'
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

@lab6.route('/lab6/json-rpc-api/', methods=['POST'])
def api():
    data = request.json
    id = data['id']

    login = session.get('login')
    if not login:
        return {
            'jsonrpc': '2.0',
            'error': {
                'code': 1,
                'message': 'Unauthorized'
            },
            'id': id
        }

    conn, cur = db_connect()

    if data['method'] == 'info':
        cur.execute("SELECT number, tenant, price FROM offices")
        offices = cur.fetchall()
        db_close(conn, cur)
        return {
            'jsonrpc': '2.0',
            'result': [{'number': office['number'], 'tenant': office['tenant'], 'price': office['price']} for office in offices],
            'id': id
        }

    elif data['method'] == 'booking':
        office_number = data['params']
        cur.execute("SELECT tenant FROM offices WHERE number = ?", (office_number,))
        office = cur.fetchone()
        if office and office['tenant'] != '':
            db_close(conn, cur)
            return {
                'jsonrpc': '2.0',
                'error': {
                    'code': 2,
                    'message': 'Already booked'
                },
                'id': id
            }
        cur.execute("UPDATE offices SET tenant = ? WHERE number = ?", (login, office_number))
        db_close(conn, cur)
        return {
            'jsonrpc': '2.0',
            'result': 'success',
            'id': id
        }

    elif data['method'] == 'cancellation':
        office_number = data['params']
        cur.execute("SELECT tenant FROM offices WHERE number = ?", (office_number,))
        office = cur.fetchone()
        if not office or office['tenant'] == '':
            db_close(conn, cur)
            return {
                'jsonrpc': '2.0',
                'error': {
                    'code': 3,
                    'message': 'Office is not booked'
                },
                'id': id
            }
        if office['tenant'] != login:
            db_close(conn, cur)
            return {
                'jsonrpc': '2.0',
                'error': {
                    'code': 4,
                    'message': 'You are not the tenant of this office'
                },
                'id': id
            }
        cur.execute("UPDATE offices SET tenant = NULL WHERE number = ?", (office_number,))
        db_close(conn, cur)
        return {
            'jsonrpc': '2.0',
            'result': 'success',
            'id': id
        }

    db_close(conn, cur)
    return {
        'jsonrpc': '2.0',
        'error': {
            'code': -32601,
            'message': 'Method not found'
        },
        'id': id
    }

if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'
    app.config['DB_TYPE'] = 'sqlite'
    app.register_blueprint(lab6)
    init_db()
    app.run(debug=True)