import math
from math import asinh

# Функция для расчета точной суммы
def hyperbolic_arcsine_sum(x_val):
    return (1/x_val) * asinh (1 / x_val)

# Функция для расчета коэффициента ряда
def series_coeff(i_term, x_val):
    numerator = (-1) ** (i_term) * (math.factorial(2 * i_term)) * x_val ** (-2 * i_term - 2)
    denominator = (4 ** i_term) * (2 * i_term + 1) * (math.factorial(i_term)) ** 2
    coeff = numerator / denominator
    return coeff

# Наивная сумма
def naive_series_sum(num_terms, x_val):
    naive_sum = 0.0
    for i in range(num_terms):
        naive_sum += series_coeff(i, x_val)
    return naive_sum

# Функция для поиска подходящего n
def appropriate_n_value(x_val, precision_threshold):
    n_val = 0
    while abs(series_coeff(n_val, x_val)) > precision_threshold:
        n_val += 1
    return n_val

# Сумма с использованием алгоритма Кэхена
def kahan_algorithm_sum(n_terms, x_val):
    k_sum = 0.0
    comp = 0.0  # компенсация
    for i in range(n_terms):
        y_val = series_coeff(i, x_val) - comp
        temp = k_sum + y_val
        comp = (temp - k_sum) - y_val
        k_sum = temp
    return k_sum

# Сумма с сортировкой слагаемых
def sorted_components_sum(n_terms, x_val):
    coeffs = [series_coeff(i, x_val) for i in range(n_terms)]
    coeffs.sort()  # сортируем, так как требуется возрастание
    return sum(coeffs)

# Вывод результатов на экран
def display_results(point_name, x_value, precision):
    n_value = appropriate_n_value(x_value, precision)
    exact_value = hyperbolic_arcsine_sum(x_value)
    print(f"--- Точка {point_name} ---")
    print(f"Количество слагаемых n: {n_value}")
    print(f"Точное значение        : {exact_value:.15f}")

    for sum_func, desc in [(naive_series_sum, "наивная"), (sorted_components_sum, "с сортировкой"), (kahan_algorithm_sum, "Кэхен")]:
        result = sum_func(n_value, x_value)
        deviation = abs(exact_value - result)
        print(f"{desc.capitalize()} сумма  : {result:.15f}")
        print(f"Отклонение от точного : {deviation:.15f}")
    print()

# Задаем значения и точность
FIRST_POINT = 100
SECOND_POINT = 9 / 8
PRECISION = 10 ** (-12)

display_results('Первая', FIRST_POINT, PRECISION)
display_results('Вторая', SECOND_POINT, PRECISION)