from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_locality_names')
def get_locality_names():
    response = jsonify({
        'locality': util.get_locality_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    area_in_sqft = float(request.form['area_in_sqft'])
    locality = request.form['locality']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(locality, area_in_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
