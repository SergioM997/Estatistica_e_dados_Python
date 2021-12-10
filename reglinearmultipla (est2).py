# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:21:51 2020

@author: User
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm

base = pd.read_csv('mt_cars.csv')
base = base.drop(['Unnamed: 0'],axis = 1)

X = base.iloc[:,2].values #Serve pra delimitar qual coluna que sera reglin
y = base.iloc[:,0].values
correlacao = np.corrcoef(X,y)
X=X.reshape(-1,1)

modelo = LinearRegression()
modelo.fit(X,y)
Intercept = modelo.intercept_
Coef = modelo.coef_
Score = modelo.score(X,y)

previsoes = modelo.predict(X)
modelo_ajustado = sm.ols(formula = 'mpg ~ disp', data=base)
modelo_treinado = modelo_ajustado.fit()
sumario = modelo_treinado.summary

plt.scatter(X,y)
plt.plot(X,previsoes,color='red')

X1 = base.iloc [:,1:4].values
y1 = base.iloc[:,0].values
modelo2 = LinearRegression()
modelo2.fit(X1,y1)

modelo2.score(X1,y1)
modelo_ajustado2 = sm.ols(formula = 'mpg ~ cyl + disp + hp', data=base)
modelo_treinado2 = modelo_ajustado2.fit()
modelo_treinado2.summary


