# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 23:47:12 2023

@author: david
"""

import random

num_simulations = 10000
num_successes = 0

for i in range(num_simulations):
    rolls = [random.randint(1, 6) for j in range(3)]
    if 6 in rolls:
        num_successes += 1

prob_estimate = num_successes / num_simulations
print("Estimated probability of rolling at least one six in three rolls:", prob_estimate)