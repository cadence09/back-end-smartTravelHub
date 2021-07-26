from app import db;
from sqlalchemy import JSON

class Travelposts(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    title=db.Column(db.String)
    country=db.Column(db.String)
    state=db.Column(db.String)
    days=db.Column(db.ARRAY(JSON))
    