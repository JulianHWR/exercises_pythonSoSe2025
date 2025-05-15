# -*- coding: utf-8 -*-
"""
Created on Thu May 15 09:50:11 2025

@author: s_kircher24
"""

import matplotlib.pyplot as plt

a = 1
r = -1
n = 5
s_n = []

summe = 0
for k in range(0, n+1):
    summe += a * r**k
    s_n.append(summe)
    
plt.plot(s_n)    