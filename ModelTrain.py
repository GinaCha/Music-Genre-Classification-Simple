import numpy
import pandas
import joblib

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.ensemble import ExtraTreesClassifier


def main():
    data_set = pandas.read_csv('data/dataset.csv', index_col=False)
    data_set = numpy.array(data_set)
    print("Dataset shape:", data_set.shape)
    number_of_rows, number_of_cols = data_set.shape

    data_x = data_set[:, :number_of_cols - 1]
    data_y = data_set[:, number_of_cols - 1]

    model = RandomForestClassifier(n_estimators=10, max_depth=None,min_samples_split=2, random_state=0)
    print("Training the model.....")
    model.fit(data_x, data_y)

    joblib.dump(model, 'model.pkl')
    print("Trained and saved the model to project folder successfully.")


if __name__ == '__main__':
    main()
