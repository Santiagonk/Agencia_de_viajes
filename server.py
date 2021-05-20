import joblib
import numpy as np


from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

#POSTMAN PARA PRUEBAS
@app.route('/predict', methods = ['GET'])
def predict():
    X_test = np.array([4, 1, 39, 1, 0, 1, 0, 0, 0, 0, 0])
    prediction = int(model.predict(X_test.reshape(1,-1))[0])
    return jsonify(
                    {"Prediccion": prediction}
                )

if __name__ == "__main__":
    model = joblib.load('./models/best_model.pkl')
    app.run(port=8080)