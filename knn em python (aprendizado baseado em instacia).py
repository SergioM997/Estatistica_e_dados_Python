# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 02:55:05 2020

@author: User
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from scipy import stats

iris = datasets.load_iris()
classe = iris.target
previsores = iris.data


X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores,classe,test_size=0.3,random_state=0)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_treinamento, y_treinamento)
previsoes = knn.predict(X_teste)
taxa_acerto=accuracy_score(y_teste,previsoes)