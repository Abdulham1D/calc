from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/mul', methods=['GET'])
def mul():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is not None and b is not None:
        result = a * b
        return jsonify(a=a, b=b, result=result)
    else:
        return jsonify(error="Missing data for 'a' or 'b'"), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
