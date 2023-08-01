from flask import Flask, render_template, session, redirect, url_for, request, make_response
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route('/')
def main_page():
    return render_template('base.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        response = make_response(redirect('/logged/'))
        response.set_cookie('user_name', name)
        response.set_cookie('user_email', email)
        return response
    return render_template('logged.html')


@app.route('/logged/')
def welcome():
    user_name = request.cookies.get('user_name')
    if user_name:
        return render_template('logged.html', name=user_name)
    else:
        return redirect('/')


@app.route('/logout/')
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('user_name')
    response.delete_cookie('user_email')
    return response


if __name__ == '__main__':
    app.run(debug=True)