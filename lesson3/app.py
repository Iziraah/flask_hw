import random
from flask import Flask, render_template
from models import db, Students, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

db.init_app(app)

@app.route('/')
def index():
    return 'Hello world'

@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('База данных создана!')
    
@app.route('/createdb/')
def create_db():
    db.create_all()
    print('ok')
    
@app.route('/add-faculty/')
def addfaculty():
    count = 2
    for faculty in range(1, count + 1):
        new_faculty = Faculty(faculty_name = f'faculty{faculty}')
        db.session.add(new_faculty)
    db.session.commit()
    return f'ok! Faculty'                          

@app.route('/add-student/')
def addstudent():
    count = 5
    for student in range(1, count + 1):
        new_student = Students(first_name = f'name{student}',
                               last_name = f'last_name{student}',
                               age = random.randint(10, 30),
                               gender = random.choice(['male', 'female']),
                               group = random.choice(['1A', '2B', '3C']),
                               faculty_id = random.choice([1, 2]))
        db.session.add(new_student)
    db.session.commit()
    return f'ok! Student' 

@app.route('/show-student/')
def show_student():
    students = Students.query.all()
    context = {'students': students}
    return render_template('base.html', **context)
    # return "hi"
    
if __name__ == '__main__':
    app.run(debug=True)