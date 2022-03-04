import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    # open the connection to the database
    conn = sqlite3.connect('california_house_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # fetch data from the deployments table
    cur.execute("select * from test")
    rows_deploy = cur.fetchall()
    conn.close()
    return render_template('test.html', rows_deploy=rows_deploy)

@app.route('/train')
def train():
    # open the connection to the database
    conn = sqlite3.connect('california_house_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # fetch data from the status table
    cur.execute("select * from train")
    rows_status = cur.fetchall()
    conn.close()
    return render_template('train.html', rows_status=rows_status)