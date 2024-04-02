#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>', 200

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter, 200

@app.route('/count/<int:parameter>')
def count(parameter):
    result = ''
    for num in range(parameter):
        result += str(num) + '\n'
    return result, 200

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2), 200
    elif operation == '-':
        return str(num1 - num2), 200
    elif operation == '*':
        return str(num1 * num2), 200
    elif operation == 'div':
        return str(num1 / num2), 200
    elif operation == '%':
        return str(num1 % num2), 200
    else:
        return f'invalid operation: {operation}', 404
    





if __name__ == '__main__':
    app.run(port=5555, debug=True)
