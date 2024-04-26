# -*- coding: utf-8 -*-
"""Practical4(boston).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ce_6OtTnVV4hzZGQ1EPXdpkbIFnjbih1
"""

import numpy as np
import pandas as pd
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
data = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv")

print(data.head())

data.shape

data.isnull().sum()

X = data.drop(columns=['medv'])
y = data['medv']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

X_train = np.c_[np.ones(X_train.shape[0]), X_train]
X_test = np.c_[np.ones(X_test.shape[0]), X_test]

coefficients = np.linalg.inv(X_train.T @ X_train) @ X_train.T @ y_train

y_pred = X_test @ coefficients

mean_y = np.mean(y_test)
sst = np.sum((y_test - mean_y)**2)
ssr = np.sum((y_pred - mean_y)**2)
score = ssr / sst

print("Model Score:", score)