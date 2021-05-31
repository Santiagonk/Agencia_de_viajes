import pandas as pd
import joblib

class Utils:
    def load_from_csv(self, path):
        return pd.read_csv(path, usecols=['duracion_estadia', 'genero', 'edad', 'ninos', 'tipo_acomodacion',
        'COL', 'ES', 'IT', 'NL', 'PE', 'UK', 'US'])

    def features_target(self, dataset, y):
        X = dataset.drop(y, axis = 1)
        y = dataset[y]

        return X, y

    def model_export(self, model, score):
        print(score)
        joblib.dump(model, './models/best_model.pkl')

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