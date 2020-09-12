import matplotlib.pyplot as plt
import numpy as np


def linear_function(x, coeff, displ):
    return coeff * x + displ


def power_function(x, exp, coeff, displ):
    return coeff * x ** exp + displ


def gamma_precipitation(temperature):
    params = [129811, -145706, 53297, -6270.4]
    polynomial: float = 0
    order = len(params) - 1
    for i, p in enumerate(params):
        polynomial += p * temperature ** (order - i)
    return polynomial


def carbide_precipitation(temperature):
    params = [-3721.5, 7061.9, -4173, 796.32]
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


plt.rcParams.update({'font.size': 14})
max_dpa = 60
fig, ax = plt.subplots()
ax.plot(np.linspace(.3, .8, 200), gamma_precipitation(np.linspace(.3, .8, 200)), "#85d22e")
ax.plot(np.linspace(.414, .606, 200), carbide_precipitation(np.linspace(.414, .606, 200)), "g-")
ax.vlines(.414, 0, max_dpa, colors="g")  # lower sigma-precipitation limit
ax.vlines(.606, 0, max_dpa, colors="g")  # upper sigma-precipitation limit
ax.plot(np.linspace(.3, .8, 200), hardening(np.linspace(.3, .8, 200)), "k-")  # hardening (model 2) limit
ax.vlines(.3, hardening(.3), max_dpa, colors="k")
ax.vlines(.3, 0, max_dpa, colors="k", linestyles="dashed")  # hardening (model 1) limit
ax.fill_between(np.linspace(.15, .4, 200), 2.5, 25, facecolor='#CFCFCF')  # brittle failure region
ax.plot(np.linspace(0, .8, 200), swelling(np.linspace(0, .8, 200)), "y-")
ax.vlines(.4, 0, max_dpa, linestyles="dotted", colors="r")  # thermal creep limit
ax.plot(np.linspace(.465, .8, 200), matrix_strengthening(np.linspace(.465, .8, 200)), "b-")
ax.plot(np.linspace(.44, .465, 200), matrix_strengthening(np.linspace(.44, .465, 200)), "b--")
ax.plot(np.linspace(.465, .8, 200), he_embrittlement(np.linspace(.465, .8, 200)), "c-")
ax.set_title("Material mechanisms of SS316")
ax.set_xlabel('homologous Temperature')
ax.set_ylabel('Dose [dpa]')
ax.set_xlim(.25, .65)
ax.set_ylim(0, max_dpa)
plt.show()
