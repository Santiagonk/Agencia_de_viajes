from utils import Utils
from models import Models


if __name__=="__main__":

    utils = Utils()
    models = Models()

    data = utils.load_from_csv("./in/clean_data.csv")
    X, y = utils.features_target(data, ['tipo_acomodacion'])

    models.grid_training(X, y)
    # print(data)