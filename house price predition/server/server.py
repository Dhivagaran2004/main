from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_name')
def get_location_name():
    response=jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('access-control-allow-orginal' , '*')

    return response
@app.route('/get_estimate_price',methods=['post'])
def get_estimate_price():
    total_sqft =float(request.form['total_sqft'])
    locations = request.form(['locations'])
    bhk = int(request.form(['bhk']))
    bath = int(request.form(['bath']))

    response = jsonify({
        'estimate_price': util.get_estimate_price(locations,total_sqft,bhk,bath)
    })

    response.headers.add('access-control-allow-orginal' , '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask server for home price prediction...")
    util.load_saved_artifacts()
    app.run()
