# models/titanic.py
import numpy as np
import pickle
import joblib
import pandas as pd


class Titanic:
    model = None

    def __init__(self):
        """Inicializa o modelo
        """
        self.load_model()

    def load_model(self, path='.ml-model/_titanic.pkl'):
        """Carrega o modelo treinado
        """
        # carrrega o modelo usando a biblioteca apropriada
        switcher = {
            # '.pkl': pickle.load(open(path, 'rb')),
            '.pkl': joblib.load(path),
            '.joblib': joblib.load(path)
        }
        self.model = switcher.get(path[-4:], "Modelo não suportado")
        return self

    def predict_survival(self, passenger):
        """Faz a predição de sobrevivência ou morte de um passageiro do Titanic
        """
        print(f"Fazendo predição do passageiro {passenger}")

        # criar um dataframe com os dados do passageiro formatando as colunas para compatibilidade com o modelo
        data = {
            'Pclass': [passenger.pclass],
            'Sex': [passenger.sex],
            'Age': [passenger.age],
            'SibSp': [passenger.sibsp],
            'Parch': [passenger.parch],
            'Fare': [passenger.fare],
            'Embarked': [passenger.embarked],
            'Cabin': [passenger.cabin]
        }
        df = pd.DataFrame(data)

        # fazer a predição
        survival = self.model.predict(df)
        return int(survival[0])
