from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:leo.steve@localhost:5432/duka'
db=SQLAlchemy(app)
class User(db.Model):
    __tablename__= 'user'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), nullable=False)
    email=db.Column(db.String(), unique=True)
with app.app_context():
    db.create_all()

@app.route('/')
def hello():
    new_user=User(name="stevoh",email="steveleo254@gmail.com")
    db.session.add(new_user)
    db.session.commit()
    new_user2= User(name="john",email="john2544@gmail.com")
    db.session.add(new_user2)
    db.session.commit()
    return "hi"

app.run()