from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Students(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(120), nullable = False)
    last_name = db.Column(db.String(120), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    gender = db.Column(db.String(5), nullable = False)
    group = db.Column(db.String(15), nullable = False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable = False)
    
class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    faculty_name = db.Column(db.String(120), nullable = False)
    students = db.relationship('Students', backref='faculty')
    