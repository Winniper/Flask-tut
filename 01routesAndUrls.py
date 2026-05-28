from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('Hello World!!')
    response.status_code = 202
    response.headers['content-type'] = 'application/json'
    return response
    #return "Hello World!!", 200 This is a way to set HTTP Status Codes

@app.route('/greet/<name>', methods=['GET', 'POST']) #Dynamic URL & Methods
def greet(name):
    if request.method == 'GET':
        return f"This is a GET request by {name}"
    elif request.method == 'POST':
        return f"THis is a POST request by {name}"
    else:
        return "This line of code will never be executed"
    

@app.route('/add/<int:number1>/<int:number2>') #Type casting for numbers
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"

@app.route('/handle_url_params') #How to handle URL params
def handle_params():
    if 'greetings' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')

        return f"{greeting}, {name}"
    else:
        return '<h1>Some Parameters are missing</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)