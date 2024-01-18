# app/models.py
from flask_sqlalchemy import SQLAlchemy
from app import  db   #Error que no me dejaba realizar consultas 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    cuenta = db.Column(db.String(20), unique=True, nullable=False)
    saldo = db.Column(db.Float, default=0.0)

    # Relación con cuentas
    accounts = db.relationship('Account', backref='user', lazy=True)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(20), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    balance = db.Column(db.Float, default=0.0)
