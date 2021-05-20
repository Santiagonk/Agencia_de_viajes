import pandas as pd
import numpy as np

from utils import Utils

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class Models:

    def grid_training(self, X, y):

        print(list(X.iloc[1,:]))
        rfc = RandomForestClassifier(min_samples_leaf=10, min_samples_split=10)
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
        rfc.fit(X_train, y_train)
        score = rfc.score(X_test, y_test)
        model = rfc.base_estimator_
        utils = Utils()
        utils.model_export(rfc,score)
