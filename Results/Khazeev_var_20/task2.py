import math
from csv import DictWriter

file = open('data.csv', 'w', newline = '')
 
with file:
    header = ['x_i', 'n', 'sum1', 'sum2']
    writer = DictWriter(file, fieldnames = header)
    writer.writeheader()
        
a = float(-25)
b = float(0)
h = (b-a)/100
x = a

while x <= b:
    sum = 0
    ordered_sum = 0
    coefficient = x
    coefficients = [coefficient]
    n = 0
    while abs(coefficient) > 1e-8:
        n += 1
        coefficient *= ((-1) * math.factorial(2*n-1) * (2*n-1) * x**2)/((2*n+1) * math.factorial(abs(2*n+1)))
        coefficients.append(coefficient)

    coefficients.pop()

#Наивное суммирование
    for i in range(n):
        sum += coefficients[i]

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if coefficients[j] > coefficients[j + 1]:
                placeholder = coefficients[j]
                coefficients[j] = coefficients[j + 1]
                coefficients[j + 1] = placeholder

#Сумма по возрастанию слагаемых
    for i in range(n):
        ordered_sum += coefficients[i]

    dict = {'x_i': '%.15e' % x, 
            'n': n, 
            'sum1': '%.15e' % sum,
            'sum2': '%.15e' % ordered_sum}
 
    with open('data.csv', 'a', newline = '') as f_object:
 
        dictwriter_object = DictWriter(f_object, fieldnames=header)
        dictwriter_object.writerow(dict)
        f_object.close()

    x += h

