import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import scipy.special as sp


def sum_lst(x):

    coefficient = 1.0/x
    coefficients = [coefficient]
    summ1 = 0
    summ2 = 0
    n = 0
    while abs(coefficient) > 1e-8:
        n += 1
        coefficient *= -1.0*(math.exp(1)-n)*(x+n-1)/((x+n)*n)
        coefficients.append(coefficient)
        if n == 100:
            break
    coefficients.pop()

    for i in range(n):
        summ1 += (coefficients[i])

    for i in range(n-1):
        for j in range(n-1-i):
            if (coefficients[j]) > (coefficients[j+1]):
                coefficients[j], coefficients[j +
                                              1] = (coefficients[j+1]), (coefficients[j])
    for i in range(n):
        summ2 += (coefficients[i])

    res = ['{:.15f}'.format(x),
           n, '{:.15f}'.format(summ1), '{:.15f}'.format(summ2)]
    return res


a = 2
b = 3
data = pd.DataFrame(columns=['x_i', 'n', 'sum1', 'sum2'])


delta = (b-a)/100

t = a
while t <= b:
    data.loc[len(data.index)] = sum_lst(t)
    t += delta

data['x_i'] = data['x_i'].astype(float)
data['n'] = data['n'].astype(int)
data['sum1'] = data['sum1'].astype(float)
data['sum2'] = data['sum2'].astype(float)
data.to_csv('result.csv')
