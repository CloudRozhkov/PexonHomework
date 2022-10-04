from flask import Flask, render_template, url_for, request, g
from FDataBase import FDataBase
import sqlite3
import os

# configuration
DATABASE = '/flask-app-test/pexon_zertifikate.db'
DEBUG = True
SECRET_KEY = 'hjhvjkjh748jdkjnv0573kdjhj'

app = Flask(__name__)
app.config.from_object(__name__)

# root path to Database
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'pexon_zertifikate.db')))

# connect to DB
def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

# helper funktion to create DB
def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()
# connect to DB wenn noch nicht vorhanden
def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.route("/", methods=["POST", "GET"])
def zert():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        print(request.form)
    return render_template('index.html', zert = dbase.getZert())

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

if __name__ == "__main__":
    app.run(debug=True)
