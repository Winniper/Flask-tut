from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!!"

@app.route('/greet/<name>') #Dynamic URL
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:number1>/<int:number2>') #Type casting for numbers
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)