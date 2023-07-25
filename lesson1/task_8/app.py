from flask import Flask
from flask import render_template

app = Flask(__name__)

# new*

@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')

@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')

@app.route('/accesories/')
def accesories():
    return render_template('accesories.html')

if __name__== '__main__':
    app.run()