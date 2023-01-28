from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from GWDP_API import execute_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./instance/pythongit.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Creates our a database model for our flask app to attach to
class Repos(db.Model):
    repository_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    url = db.Column(db.String(250))
    created_date = db.Column(default=datetime.date)
    last_push = db.Column(default=datetime.date)
    description = db.Column(db.String(250))
    star_num = db.Column(db.Integer)


# executes our API call
with app.app_context():
    execute_db()

    


@app.route('/')
def index():
    db.create_all()
    repos = Repos.query
    return render_template('basic_table.html', Repos_list=repos)


if __name__ == '__main__':
    app.run()
