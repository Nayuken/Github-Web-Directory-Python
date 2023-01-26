from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from GPRWD_webscrapper import execute_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pythongit.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#create our a database model for our flask app to attach to
class repos(db.Model):
    repository_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    url = db.Column(db.String(250))
    created_date = db.Column(db.Date, default=datetime.utcnow)
    last_push = db.Column(db.Date, default=datetime.utcnow)
    description = db.Column(db.String(250))
    star_num = db.Column(db.Integer)

# execute our API call
# with app.app_context():
#     execute_db()

@app.route('/')
def index():
    execute_db()
    db.create_all()
    users = repos.query.order_by(repos.star_num).all()
    return render_template('basic_table.html', users=users)
if __name__ == '__main__':
    app.run()