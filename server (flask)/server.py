# Note : the UI makes call to the backend and the backend makes get and
#  post calls to the server  to get the results.


# importing flask here
# flask is a python library used for developing web applications
# flask is a module which allows to write a python service, to solve HTTP request

from flask import Flask, request, jsonify
import util

app = Flask(__name__)  # created app using this line


# creates a URL path to run our app. append 'hello' to that URL to get our function output

# We are writing 2 routines(Functions)
# 1) for returning locations
# 2) for predicting price using model

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price',
           methods=['GET', 'POST'])  # GET to receive data from server and POST to send data to server
def predict_home_price():
    # storing paremeters needed for price prediction into local vaiables
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
        # passing these values to our util file function
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response  # returns the value


if __name__ == "__main__":  # main function
    print('Starting flask server for home price prediction....')
    util.load_saved_artifacts()
    app.run()  # line to run our app
