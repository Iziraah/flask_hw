# Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.

 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/name/')
def name_page():
    name1 = 'Ivan'
    return render_template('hello.html', name = name1)

@app.route('/pic/')
def pic_page():
    return render_template('pic.html')

@app.route('/upload/')
def upload_page():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)