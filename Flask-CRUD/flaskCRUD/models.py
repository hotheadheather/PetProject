import datetime
from multiprocessing import Value
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
 
db =SQLAlchemy()
 
class donationModel(db.Model):
    __tablename__ = "donations"
 
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String())

    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    gender = db.Column(db.String())
    foodtype = db.Column(db.String(80))
    amount = db.Column(db.Integer())
    weight = db.Column(db.String())

   
 
    def __init__(self,date,first_name,last_name,email,gender,foodtype,amount,weight):
        self.date = date
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.gender = gender
        self.foodtype =foodtype
        self.amount = amount
        self.weight = weight

      
 
    def __repr__(self):
        return f"{self.first_name}:{self.last_name}"