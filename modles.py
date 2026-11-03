from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    department = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    phone = db.Column(db.String(15))
    joining_date = db.Column(db.Date)
