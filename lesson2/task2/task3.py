
 
from flask import Flask, render_template, request

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

@app.route('/login/', methods=['GET','POST'])
def login_page():
    admin = 'admin'
    admin_pas = 'qwerty'
    if request.method == 'POST':
        log = request.form['login']
        pas = request.form['password']
        print(log, pas)
        if log == admin and pas == admin_pas:
            return render_template('hello.html', name=log)
        else:
            return render_template('error.html')
    # else:
    #     return render_template('error.html')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)