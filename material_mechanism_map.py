import matplotlib.pyplot as plt
import numpy as np


def linear_function(x, coeff, displ):
    return coeff * x + displ


def power_function(x, exp, coeff, displ):
    return coeff * x ** exp + displ


def precipitation(temperature):
    params = [129811, -145706, 53297, -6270.4]
    polynomial: float = 0
    order = len(params) - 1
    for i, p in enumerate(params):
        polynomial += p * temperature ** (order - i)
    return polynomial


def hardening(temperature):
    params = [-104.57, 70.463]
    return linear_function(temperature, *params)


def swelling(temperature):
    params = [-1338.5, 458.4]
    return linear_function(temperature, *params)


def he_embrittlement(temperature):
    params = [14.8, 2E6, 0]
    return power_function(temperature, *params)


def matrix_strengthening(temperature):
    params = [32.665, 2E12, 0]
    return power_function(temperature, *params)


max_dpa = 60
fig, ax = plt.subplots()
ax.plot(np.linspace(.3, .8, 200), precipitation(np.linspace(.3, .8, 200)), "g-")
ax.plot(np.linspace(.3, .8, 200), hardening(np.linspace(.3, .8, 200)), "k-")
ax.vlines(.3, hardening(.3), max_dpa, colors="k")
ax.plot(np.linspace(0, .8, 200), swelling(np.linspace(0, .8, 200)), "y-")
ax.vlines(.4, 0, max_dpa, linestyles="dotted", colors="r")
ax.plot(np.linspace(.465, .8, 200), he_embrittlement(np.linspace(.465, .8, 200)), "c-")
ax.plot(np.linspace(.465, .8, 200), matrix_strengthening(np.linspace(.465, .8, 200)), "b-")
ax.set_title("Material mechanisms of SS316")
ax.set_xlabel('homologous Temperature')
ax.set_ylabel('Dose [dpa]')
ax.set_xlim(.25, .55)
ax.set_ylim(0, max_dpa)
plt.show()