
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/calculate/', methods=['GET','POST'])
def calculate_page():
    # result
    if request.method == 'POST':
        number1 = int(request.form['num1'])
        number2 = int(request.form['num2'])
        entry = request.form['todo']
        if entry == '+':
            result = number1 + number2
            return render_template('result.html', result1 = result)
        if entry == '-':
            result = number1 - number2
            return render_template('result.html', result1 = result)
        if entry == '*':
            result = number1 * number2
            return render_template('result.html', result1 = result)
        if entry == '/':
            result = number1 / number2
            return render_template('result.html', result1 = result)
    return render_template('calkulate.html')

if __name__ == '__main__':
    app.run(debug=True)