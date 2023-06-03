import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

data = pd.read_csv('D:\\Web\\Projects\\DSBDA - Copy\\winequalityN.csv')
print(data.head())

data['type'] = data['type'].map({'white': 0, 'red': 1}).astype(int)
data['pH'].fillna(value=round(data['pH'].mean()), inplace=True)
data['fixed acidity'].fillna(value=round(data['fixed acidity'].mean()), inplace=True)
data['volatile acidity'].fillna(value=round(data['volatile acidity'].mean()), inplace=True)
data['citric acid'].fillna(value=round(data['citric acid'].mean()), inplace=True)
data['residual sugar'].fillna(value=round(data['residual sugar'].mean()), inplace=True)
data['chlorides'].fillna(value=round(data['chlorides'].mean()), inplace=True)
data['free sulfur dioxide'].fillna(value=round(data['free sulfur dioxide'].mean()), inplace=True)
data['total sulfur dioxide'].fillna(value=round(data['total sulfur dioxide'].mean()), inplace=True)
data['density'].fillna(value=round(data['density'].mean()), inplace=True)
data['sulphates'].fillna(value=round(data['sulphates'].mean()), inplace=True)
data['alcohol'].fillna(value=round(data['alcohol'].mean()), inplace=True)

x = data.drop('quality', axis=1)
print(x)
y = data['quality'].apply(lambda y_value: 1 if y_value >= 7 else 0)
print(y)

# Splitting Training and Test Set
# Since we have a very small dataset, we will train our model with all available data.
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=3)
X_train.head()
print(y.shape, Y_train.shape, Y_test.shape)

model = RandomForestClassifier()
model.fit(X_train, Y_train)

X_test_pred = model.predict(X_test)
test_accuracy = accuracy_score(X_test_pred, Y_test)
print("Accuracy: ", test_accuracy)


# Saving model to disk
pickle.dump(model, open('model.pkl', 'wb'))

'''
# Loading model to compare the results
model = pickle.load(open('model.pkl', 'rb'))
print(model.predict([[2, 9, 8]]))
'''