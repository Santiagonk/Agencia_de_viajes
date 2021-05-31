import joblib
import numpy as np


from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
import json

def toPredictedArray(dataInput):
  dataString = str(dataInput)
  dataString = dataString.strip('b')[1:-1]
  dataString = dataString.strip('{').strip('}').replace('"','')
  dataString = dataString.split(',')

  dictionary = {}
  for i in dataString:
    dictionary[i.split(':')[0]] = i.split(':')[1]
  
  y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

  for key in dictionary.keys():
    if key == 'destino':
      if dictionary[key] == 'COL':
        y[4] = 1
      elif dictionary[key] == 'ES':
        y[5] = 1
      elif dictionary[key] == 'IT':
        y[6] = 1
      elif dictionary[key] == 'NL':
        y[7] = 1
      elif dictionary[key] == 'PE':
        y[8] = 1
      elif dictionary[key] == 'UK':
        y[9] = 1
      elif dictionary[key] == 'US':
        y[10] = 1
    
    if key == 'duracionEstadia':    
      y[0] = int(dictionary[key])
    
    if key == 'genero':
      if dictionary[key] == 'F':
        y[1] = 1
    
    if key == 'edad':
      y[2] = int(dictionary[key])
    
    if key == 'ninos':
      if dictionary[key] == 'SI':
        y[3] = 1
  
  return y



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
        print(prediction)
    else:
        X_test = np.array([4, 1, 39, 1, 0, 1, 0, 0, 0, 0, 0])
        prediction = int(model.predict(X_test.reshape(1,-1))[0])
    return jsonify(
                    {"Prediccion": prediction}
                )

if __name__ == "__main__":
    model = joblib.load('./models/best_model.pkl')
    app.run(port=8080)