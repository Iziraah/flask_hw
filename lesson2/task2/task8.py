# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".

 
from flask import Flask, redirect, render_template, request, flash, url_for

import secrets
print(secrets.token_hex())


app = Flask(__name__)
app.secret_key = 'token'

@app.route('/flash/', methods=['GET','POST'])
def nameFlash_page():
    if request.method == 'POST':
        name = request.form['name']
        flash(f'Рады тебя видеть, {name}', 'success')
        # return render_template('hello_flash.html')
        return render_template('hello_flash.html', name = name)
    return render_template('nameFlash.html')

if __name__ == '__main__':
    app.run(debug=True)
    