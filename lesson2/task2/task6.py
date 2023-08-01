# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.

 
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/age&name/', methods=['GET','POST'])
def age_name_page():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        print(name, age)
        if age > 80 and age < 14:
            return render_template('error.html')
        else:
            return render_template('Hello.html', age = age, name = name)
    # else:
    #     return render_template('error.html')
    return render_template('age&name.html')

if __name__ == '__main__':
    app.run(debug=True)