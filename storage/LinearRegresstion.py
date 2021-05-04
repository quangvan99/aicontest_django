# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 15:37:48 2020

@author: Admin
"""

import numpy as np
from numpy import genfromtxt
# import matplotlib.pyplot as plt

def nomarlize(feartures):
    min_feartures = np.min(feartures, axis = 0)
    max_feartures = np.max(feartures, axis = 0)
    mean_feartures = np.mean(feartures, axis = 0)
    return (feartures - mean_feartures)/(max_feartures - min_feartures)
        
def handle(path):
    data = genfromtxt(path, delimiter=',', skip_header=1)
    feartures  = data[:,:-1]
    y_truth = data[:,-1:]
    data_size = feartures.shape[0]
    
    feartures = nomarlize(feartures)
    
    # vector [x, 1]
    feartures = np.c_[feartures, np.ones((data_size, 1))]
    #[ w, b]
    theta = np.random.rand(feartures.shape[1], 1) 
    
    m = data_size
    eta = 0.1
    epoch_max = 500
    losses = [] # for debug
    
    for epoch in range(epoch_max):
        for i in range(0, data_size, m):
            
            # Pick sample
            x = feartures[i:i+m,:]
            y = y_truth[i:i+m]
    
            # Foward and predict
            z = x.dot(theta)
    
            # Tính loss để debug
            loss = (z - y)**2
            losses.append(loss.mean())
    
            # Tính gradient
            gradient_z = (z - y)
            gradient = x.T.dot(gradient_z)/m
            
            # Update trọng số
            theta = theta - eta*gradient
    
    return "pdsdf"

print(handle('BostonHousing.csv'))
# zoomGraph = 200
# plt.plot(losses[:zoomGraph])
