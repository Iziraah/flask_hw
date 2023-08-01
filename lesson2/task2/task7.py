# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.



from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/square/', methods=['GET','POST'])
def square_page():
    # result
    if request.method == 'POST':
        number = int(request.form['num1'])
        result = number * number
        return render_template('result.html', result1 = result)
    return render_template('square.html')

if __name__ == '__main__':
    app.run(debug=True)