from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_first_name = db.Column(db.String(80), nullable=False)
    user_last_name = db.Column(db.String(80), nullable=False)
    user_email = db.Column(db.String(120), nullable=False)
    user_password = db.Column(db.String(120), nullable=False)
    register_at = db.Column(db.DateTime, default=datetime.utcnow())