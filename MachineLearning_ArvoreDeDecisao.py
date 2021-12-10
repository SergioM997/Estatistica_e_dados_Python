
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
import graphviz
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier

credito = pd.read_csv('Credit.csv')
previsores = credito.iloc[:,0:20].values
classe = credito.iloc[:,20].values

labelencoder = LabelEncoder()
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
previsores[:,1] = labelencoder.fit_transform(previsores[:,1])
previsores[:,2] = labelencoder.fit_transform(previsores[:,2])
previsores[:,3] = labelencoder.fit_transform(previsores[:,3])
previsores[:,4] = labelencoder.fit_transform(previsores[:,4])
previsores[:,5] = labelencoder.fit_transform(previsores[:,5])
previsores[:,6] = labelencoder.fit_transform(previsores[:,6])
previsores[:,7] = labelencoder.fit_transform(previsores[:,7])
previsores[:,8] = labelencoder.fit_transform(previsores[:,8])
previsores[:,9] = labelencoder.fit_transform(previsores[:,9])
previsores[:,10] = labelencoder.fit_transform(previsores[:,10])
previsores[:,11] = labelencoder.fit_transform(previsores[:,11])
previsores[:,12] = labelencoder.fit_transform(previsores[:,12])
previsores[:,13] = labelencoder.fit_transform(previsores[:,13])
previsores[:,14] = labelencoder.fit_transform(previsores[:,14])
previsores[:,15] = labelencoder.fit_transform(previsores[:,15])
previsores[:,16] = labelencoder.fit_transform(previsores[:,16])
previsores[:,17] = labelencoder.fit_transform(previsores[:,17])
previsores[:,18] = labelencoder.fit_transform(previsores[:,18])
previsores[:,19] = labelencoder.fit_transform(previsores[:,19])

X_treinamento, X_teste, y_treinamento, y_teste= train_test_split(previsores, classe, test_size = 0.3, random_state=0)

arvore = DecisionTreeClassifier()
arvore.fit(X_treinamento, y_treinamento)

export_graphviz(arvore, out_file = 'tree.dot')

previsoes = arvore.predict(X_teste)
taxa_acerto = accuracy_score(y_teste, previsoes)
