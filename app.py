from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello to the calc app"


@app.route('/add', methods=['GET'])
def add():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is not None and b is not None:
        result = a + b
        return jsonify(a=a, b=b, result=result)
    else:
        return jsonify(error="Missing data for 'a' or 'b'"), 400

@app.route('/sub', methods=['GET'])
def sub():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is not None and b is not None:
        result = a - b
        return jsonify(a=a, b=b, result=result)
    else:
        return jsonify(error="Missing data for 'a' or 'b'"), 400

@app.route('/mul', methods=['GET'])
def mul():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is not None and b is not None:
        result = a * b
        return jsonify(a=a, b=b, result=result)
    else:
        return jsonify(error="Missing data for 'a' or 'b'"), 400

@app.route('/div', methods=['GET'])
def div():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is not None and b is not None:
        if b == 0:
            return jsonify(error="Cannot divide by zero"), 400
        result = a / b
        return jsonify(a=a, b=b, result=result)
    else:
        return jsonify(error="Missing data for 'a' or 'b'"), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
