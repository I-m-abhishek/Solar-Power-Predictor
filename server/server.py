# server.py
from flask import Flask, request, jsonify
from predict_model import predict

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def make_prediction():
    try:
        data = request.json
        input_data = data['input_data']

        # Call the predict function from predict_model.py
        prediction = predict(input_data)

        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
