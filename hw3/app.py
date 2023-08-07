from flask import Flask, render_template, session, redirect, url_for, request, make_response
from models import db, User
from flask_wtf import FlaskForm, CSRFProtect
from secrets import token_hex
from forms import RegistrationForm


app = Flask(__name__)
app.config['SECRET_KEY'] = token_hex()
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)



@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('DB OK!')


@app.route('/')
def index():
    return make_response(redirect('/register/'))
    # return render_template('base.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user_name = form.user_name.data
        user_last_name = form.user_last_name.data
        user_email = form.user_email.data
        user_password = form.user_password.data
        confirm_password = form.confirm_password.data
        new_user = User(user_first_name=user_name,
                        user_last_name=user_last_name,
                        user_email=user_email)
        db.session.add(new_user)
        db.session.commit()
        user_id = new_user.id
        return make_response(redirect(f'/register-successful/{user_id}'))
    return render_template('register.html', form=form)


@app.route('/register-successful/<int:user_id>', methods=['GET', 'POST'])
def successful_reg(user_id):
    last_user = User.query.filter_by(id=user_id).order_by(User.id.desc()).first()
    if last_user:
        name = last_user.user_first_name
        email = last_user.user_email
        return render_template('register-successful.html', user_name=name, user_email=email)
    else:
        return "User not found"


@app.route('/new-reg/')
def new_reg():
    return make_response(redirect('/'))


if __name__ == '__main__':
    app.run(debug=True)
