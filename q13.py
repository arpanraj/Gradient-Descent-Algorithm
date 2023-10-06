#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 09:23:45 2022

@author: arpanrajpurohit
"""

import numpy as np

LEARNING_RATES = [0.1, 0.01, 0.001]
STEPS          = 500
EXPERIMENTS    = 3
X0_LOW_AND_MAX = [-10, 10]
TRIALS         = 10

def equation(x, y):
    return (5*x*x) + (40*x) + (y*y) - (12*y) + 127

def derivative(x, y):
    return np.array([(10*x)+40, 2*y - 12])

def gradient_descent(X0, learning_rate, steps):
    X_prev = X0
    for i in range(steps):
        X_new = X_prev - learning_rate*derivative(X_prev[0], X_prev[1]) 
        X_prev = X_new
    return X_prev

def experiment(learning_rate, trials):
    best_X = None
    for trial in range(trials):
        x0 = np.random.uniform(low=X0_LOW_AND_MAX[0], high=X0_LOW_AND_MAX[1], size=(2,))
        gd = gradient_descent(x0, learning_rate, STEPS)
        if (best_X is None) or (equation(gd[0], gd[1])<equation(best_X[0], best_X[1])):
            best_X = gd
            return gd

for exp in range(EXPERIMENTS): 

    print('\nExperiment - '+ str(exp+1))
    
    for learning_rate in LEARNING_RATES:
        exp_ans = experiment(learning_rate,TRIALS)
        print('\nlearning rate - ' + str(learning_rate))
        print('experiment XY - ' + str(exp_ans))
        print('experiment equation' + str(equation(exp_ans[0], exp_ans[1])))