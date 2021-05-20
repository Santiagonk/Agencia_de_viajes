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
