import numpy as np
import pandas as pd

epsilon = 1e-8
omega_values = np.linspace(5, 10, num=101)

def compute_zeta_function(arg):
    term = 1
    direct_sum = 0
    sequence = np.array([])
    for power in np.arange(1, 101):
        term = 1 / (power ** arg)
        sequence = np.append(sequence, term)
        direct_sum += term
    corrected_sum = kahan_summation(sequence)
    return f'{direct_sum:.15f}', f'{corrected_sum:.15f}'

def kahan_summation(terms):
    summ = 0
    compensation = 0
    for val in terms:
        adjusted_val = val - compensation
        total = summ + adjusted_val
        compensation = (total - summ) - adjusted_val
        summ = total
    return summ

zeta_dataframe = pd.DataFrame(columns=['x_value', 'DirectSum', 'KahanSum'])

for omega_idx, omega in enumerate(omega_values):
    direct_sum, compensated_sum = compute_zeta_function(omega)
    zeta_dataframe.loc[omega_idx] = [f'{omega:.2f}', direct_sum, compensated_sum]

zeta_dataframe.to_csv('zeta_data.csv', index=False)
print(zeta_dataframe)