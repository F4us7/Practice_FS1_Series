import math
#Для первой точки
x = 10
sum = 0
ordered_sum = 0
coefficient = 1/(4*x**4)
coefficients = [math.log(2*(x**2)), coefficient]
n = 1

while abs(coefficient) > 1e-12:
    n += 1
    coefficient *= ((-1) * math.factorial(2*n-1))/(4*(x**4)*(n)**2*math.factorial(abs(2*n-3)))
    coefficients.append(coefficient)

coefficients.pop()

#Наивное суммирование
for i in range(n):
    sum += coefficients[i]

kahan_sum = 0
c = 0

#Сумма по алгоритму Кэхена
for i in range(n):
    y = coefficients[i] - c
    t = kahan_sum + y
    z = t - kahan_sum
    c = z - y
    kahan_sum = t

for i in range(n-1):
    for j in range(n-1-i):
        if coefficients[j] > coefficients[j+1]:
            placeholder = coefficients[j]
            coefficients[j] = coefficients[j+1]
            coefficients[j + 1] = placeholder

#Сумма по возрастанию слагаемых
for i in range(n):
    ordered_sum += coefficients[i]

value = math.asinh(100)

print("x:  ", x, ",    n:  ", n, ".")
print('{:>19}'.format('∞'))
print("f(x) = ln(2x^2) - Σ((-1)^n*(2n-1)!!)/(2n*(2n)!!*x^(4n)) : ", value, ";")
print('{:>20}'.format('n=1'))
print("sum_1 (naive):    ", sum, ",    delta_1:  ", value - sum, ";")
print("sum_2 (ordered):  ", ordered_sum, ",    delta_2:  ", value - ordered_sum, ";")
print("sum_3 (Kahan):    ", kahan_sum, ",    delta_3:  ", value - kahan_sum, ".", end = '\n\n')



#Для второй точки
x = 3/(2*math.sqrt(2))
sum = 0
ordered_sum = 0
coefficients.clear()
coefficient = 1/(4*x**4)
coefficients = [math.log(2*x**2), coefficient]
n = 1

while abs(coefficient) > 1e-12:
    n += 1
    coefficient *= ((-1) * math.factorial(2*n-1))/(4*(x**4)*(n)**2*math.factorial(abs(2*n-3)))
    coefficients.append(coefficient)

coefficients.pop()

#Наивное суммирование
for i in range(n):
    sum += coefficients[i]

kahan_sum = 0
c = 0

#Сумма по алгоритму Кэхена
for i in range(n):
    y = coefficients[i] - c
    t = kahan_sum + y
    z = t - kahan_sum
    c = z - y
    kahan_sum = t

for i in range(n-1):
    for j in range(n-1-i):
        if coefficients[j] > coefficients[j+1]:
            placeholder = coefficients[j]
            coefficients[j] = coefficients[j+1]
            coefficients[j+1] = placeholder

#Сумма по возрастанию слагаемых
for i in range(n):
    ordered_sum += coefficients[i]

value = math.asinh(8/7)

print("x:  ", x, ",    n:  ", n, ".")
print('{:>19}'.format('∞'))
print("f(x) = ln(2x^2) - Σ((-1)^n*(2n-1)!!)/(2n*(2n)!!*x^(4n)) : ", value, ";")
print('{:>20}'.format('n=1'))
print("sum_1 (naive):    ", sum, ",    delta_1:  ", value - sum, ";")
print("sum_2 (ordered):  ", ordered_sum, ",    delta_2:  ", value - ordered_sum, ";")
print("sum_3 (Kahan):    ", kahan_sum, ",    delta_3:  ", value - kahan_sum, ".")

