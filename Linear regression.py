#code
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class LinearRegression:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.learning_rate = learning_rate
        self.iterations = iterations

    def fit(self, X, y):
        #no. of training examples = m, no. of features = n
        self.m, self.n = X.shape
        self.W = np.zeros(self.n)
        self.b = 0
        self.X = X
        self.y = y

        for i in range(self.iterations):
            self.update_weights()
        
        return self
    
    def update_weights(self):
        dW = - ( 2 * ( self.X.T ).dot( self.Y - Y_pred )  ) / self.m 
        db = - 2 * np.sum( self.Y - Y_pred ) / self.m  

        self.W = W - self.learning_rate*dW
        self.b = b - self.learning_rate*db

    def predict(self, X):
        return X.dot(self.W) + self.b
    
