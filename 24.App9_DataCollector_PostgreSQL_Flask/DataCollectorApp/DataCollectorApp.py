from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

from email_sender import send_email

from sqlalchemy.sql import func

import secrets

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = secrets.db_credentials_local
# app.config['SQLALCHEMY_DATABASE_URI'] = secrets.db_credentials_heroku

db = SQLAlchemy(app)

#### Have to create tables in DB: ####
# run python console:
# from DataCollectorApp import db
# db.create_all()
######################################

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success/', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form['height_name']


        if db.session.query(Data).filter(Data.email == email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            average_hight = db.session.query(func.avg(Data.height)).scalar()
            average_hight = round(average_hight)

            count = db.session.query(Data.height).count()

            send_email(email, height, average_hight, count)

            return render_template('success.html')

        return render_template('index.html', text = "Email already used")



if __name__ == '__main__':
    app.run(debug=True)
