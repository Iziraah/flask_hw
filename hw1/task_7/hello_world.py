from flask import Flask
from flask import render_template

app = Flask(__name__)

# new*
@app.route('/index/')
def news():
    context_1 = [
        {
            'header': 'Ураган в Нови Саде.',
            'description': 'Разрушительной силы прошел ураган в Нови Саде в среду. В городе повалены деревья, пострадало множество крыш. К сожалению, есть жертвы.',
            'date': '20.07.2023',
        },
        {
            'header': 'Животные и "Соко".',
            'description': 'Новые правила провоза животных в скоростных поездах "Соко".',
            'date': '23.07.2023',
        },
        {
            'header': 'Непогода в Кралево.',
            'description': 'Град размером с теннисный мяч прошел в городе Кралево. Пострадавших нет.',
            'date': '22.07.2023',
        },
        
    ]
    return render_template('index.html', context = context_1)


if __name__== '__main__':
    app.run()