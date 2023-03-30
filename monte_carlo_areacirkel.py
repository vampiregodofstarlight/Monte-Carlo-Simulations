# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 01:22:54 2023

@author: david
"""

import random

num_points = 1000000
inside_circle = 0

for i in range(num_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        inside_circle += 1

pi_estimate = 4 * (inside_circle / num_points)
print("Estimated value of pi:", pi_estimate)
