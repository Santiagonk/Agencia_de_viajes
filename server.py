import joblib
import numpy as np
from utils import toPredictedArray

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
import json

app = Flask(__name__)

#POSTMAN PARA PRUEBAS
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        dataInput = request.data
        X_test = np.array(toPredictedArray(dataInput))
        prediction = int(model.predict(X_test.reshape(1,-1))[0])
    else:
        X_test = np.array([4, 1, 39, 1, 0, 1, 0, 0, 0, 0, 0])
        prediction = int(model.predict(X_test.reshape(1,-1))[0])
    return jsonify(
                    {"Prediccion": prediction}
                )

if __name__ == "__main__":
    model = joblib.load('./models/best_model.pkl')
    app.run(port=8080)