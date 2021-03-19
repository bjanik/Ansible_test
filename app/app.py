import os

from flask import Flask

from db import Database

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/inc")
def increment():
    '''Increment id value'''
    db.increment_id()
    return "ID was incremented"

@app.route("/id")
def get_id():
    id = db.get_id()
    return str(id)

if __name__ == '__main__':
    with Database() as db:
        db.create_table()
        app.run(host='0.0.0.0', port=4000, debug=True)