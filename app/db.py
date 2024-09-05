# app/db.py

import mysql.connector
from flask import jsonify

def conn_db():
    conn = mysql.connector.connect(
        host='mysql-container',
        user='root',
        password='root',
        database='demo'
    )
    return conn

def get_users():
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    users = [{'id': row[0], 'name': row[1], 'email': row[2]} for row in rows]
    return jsonify(users)
