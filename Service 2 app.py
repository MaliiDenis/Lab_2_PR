from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive-data', methods=['POST'])
def receive_data():
    data = request.json  # Получаем данные из запроса
    return jsonify({"message": "Data received successfully!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
