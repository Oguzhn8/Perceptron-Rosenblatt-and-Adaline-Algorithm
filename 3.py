import math
import random
import numpy as np
from copy import deepcopy

data = []
#define the data dots
for i in range(5):
    for j in range(5):
        for k in range(5):
            x_1 = 0.1 + i / 5
            x_2 = 0.1 + j / 5
            x_3 = 0.1 + k / 5
            y = 0.5 * x_1 * x_2 + (x_2 ** 2) * math.exp(-x_3)
            data.append([[x_1, x_2, x_3], y])

dots = deepcopy(data) 
random.shuffle(dots)
  


dots_train = dots[:70]  #seperate dataset into test and train set
dots_test = dots[70:]

a = 10 ** (-3)
c = 0.1
w_list = [[0, 0, 0, 0]]     #initial weights
for i in range(1000):
    dots = deepcopy(data)
    dots_train = dots[:70]
    error = 0

    for j in range(len(dots_train)):
        dot = dots_train[j][0]
        y_d = dots_train[j][1]
        dot.append(1)
        dot = np.asmatrix(dot)
        dot_T = np.transpose(dot)

        result = np.matmul(w_list[-1], dot_T)
        y = 1 / (1 + math.exp(-a * result))
        y_d = y_d / 1.137                           #normalize 
        step_error = 0.5 * (y_d - y) * (y_d - y)    #step error
        error = error + step_error                  #adding step error to error
        w_new = w_list[-1] + c * (y_d - y) * ((a * math.exp(-a * result)) / ((1 + math.exp(-a * result)) ** 2)) * dot
        w_list.append(w_new)                        #update weights

    total_error = error / 75                        #finding errors

    if total_error < 0.055:                         #stopping criterion
        print("eğitim tamamlandı")
        break

error = 0
for j in range(len(dots_test)):                     #testing
    dot = dots_test[j][0]
    y_d = dots_test[j][1]
    dot.append(1)
    dot = np.asmatrix(dot)
    dot_T = np.transpose(dot)

    result = np.matmul(w_list[-1], dot_T)
    y = 1 / (1 + math.exp(-a * result))
    y_d = y_d / 1.137                              

    step_error = 0.5 * (y_d - y) * (y_d - y)
    error = error + step_error ** 2

total_error = error / 75

print(total_error)                                  #Error rate
