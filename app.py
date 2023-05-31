from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    temperature = float(request.form['temperature'])
    unit = request.form['unit']

    if unit == 'celsius':
        converted_temps = {
            'fahrenheit': (temperature * 9/5) + 32,
            'kelvin': temperature + 273.15,
            'rankine': (temperature + 273.15) * 9/5,
        }
    elif unit == 'fahrenheit':
        converted_temps = {
            'celsius': (temperature - 32) * 5/9,
            'kelvin': (temperature - 32) * 5/9 + 273.15,
            'rankine': temperature + 459.67,
        }
    elif unit == 'kelvin':
        converted_temps = {
            'celsius': temperature - 273.15,
            'fahrenheit': (temperature - 273.15) * 9/5 + 32,
            'rankine': temperature * 9/5,
        }
    elif unit == 'rankine':
        converted_temps = {
            'celsius': (temperature - 491.67) * 5/9,
            'fahrenheit': temperature - 459.67,
            'kelvin': temperature * 5/9,
        }
    else:
        converted_temps = {}

    return render_template('index.html', converted_temps=converted_temps, original_unit=unit, original_temp=temperature)

if __name__ == '__main__':
    app.run(debug=True)
