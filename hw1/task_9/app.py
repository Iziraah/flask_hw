from flask import Flask
from flask import render_template

app = Flask(__name__)

# new*

@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/sum/<int:num_1>/<int:num_2>')
def sum_numer(num_1, num_2):
    return f'Sum: {num_1 + num_2}'

if __name__== '__main__':
    app.run()