
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/message/', methods=['GET','POST'])
def message_page():
    if request.method == 'POST':
        message = request.form['login']
        number_of_words = len([word for word in message.split()])
        return render_template('message_result.html', number_of_words = number_of_words)
    return render_template('send.html')

if __name__ == '__main__':
    app.run(debug=True)