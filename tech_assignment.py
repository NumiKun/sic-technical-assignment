from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def terima_data():
    try:
        data = request.get_json()

        temperature = data.get('temperature')
        humidity = data.get('humidity')

        if temperature is None or humidity is None:
            return jsonify({"error": "Invalid data"})

        print(f"Data yang diterima - Temperature: {temperature}, humidity: {humidity}")

        return jsonify({"message": "Data received successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
