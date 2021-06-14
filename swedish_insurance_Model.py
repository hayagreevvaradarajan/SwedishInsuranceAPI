# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 22:26:19 2021

@author: hayag
"""
#importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

#importing the dataset
dataset = pd.read_csv("Swedish Insurance.csv")
X = dataset.iloc[:, :-2].values
y = dataset.iloc[:, -1].values

#Splitting data into training and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

#Building the linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

#Printing the accuracy
score = regressor.score(X_test, y_test)*100.0

#Visulising the training set
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'green')
plt.title("Number of claims vs Total payment (Training set)")
plt.xlabel("Number of claims")
plt.ylabel("Total payment")
plt.show()

#Visulising the test set
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'green')
plt.title("Number of claims vs Total payment (Test set)")
plt.xlabel("Number of claims")
plt.ylabel("Total payment")
plt.show()

#Dumping the model into a pickle file
pickl = {'regressor' : regressor}
pickle.dump(pickl, open('models'+".p","wb"))