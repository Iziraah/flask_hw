from flask import Flask
from flask import render_template

app = Flask(__name__)

# new*
@app.route('/index/')
def hello_world():
    context_1 = [
        {
            'name': 'Ivan',
            'surname': 'Ivanov',
            'age': 48,
            'average_score': 4.5
        },
        {
            'name': 'Svetlana',
            'surname': 'Solnceva',
            'age': 28,
            'average_score': 4.3
        },
        {
            'name': 'Jack',
            'surname': 'Nikolson',
            'age': 18,
            'average_score': 3.8
        }
    ]
    return render_template('index.html', context = context_1)

@app.route('/about/')
def about():
    return 'about'

@app.route('/contact/')
def contact():
    return 'contact'

@app.route('/sum/<int:num_1>/<int:num_2>')
def sum_numer(num_1, num_2):
    return f'Sum: {num_1 + num_2}'

if __name__== '__main__':
    app.run()