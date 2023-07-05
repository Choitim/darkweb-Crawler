from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/main', method=['GET'])
def main():
    print(request)
    return 'main', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4040)