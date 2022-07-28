import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

#dataset = pd.read_csv('deportes.csv')
#inputs = dataset.drop(columns=['deporte'])
#outputs = dataset['deporte']

#modelo = DecisionTreeClassifier()
#modelo.fit(inputs, outputs)

#joblib.dump(modelo, 'deportes-ml.joblib')

modelo = joblib.load('deportes-ml.joblib')

predicciones = modelo.predict([ [1, 24], [2,33] ])
predicciones
array(['Football', 'Basket'], dtype=object)