#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 01:17:05 2020

@author: bruno
"""
import numpy as np
import matplotlib.pyplot as plt
import re 
import glob as gl
import pandas as pd

list_models = gl.glob("*.txt")

arreglos = ['A4','A13']
profundidad = [310, 280]

plt.figure(figsize=(5,8),edgecolor="b")

for model in list_models:
    pat = re.search(r'([A]\d+)',model)
    ind = (arreglos.index(pat.group(1)))
    mod = pd.read_table(model, sep = " ", skiprows= 5, header=None)
    h = mod.loc[:,0].values
    vs = mod.loc[:,2].values
    vm = np.zeros(2*len(h))
    pm = np.zeros(2*len(h))
    for j in range(0,len(h)):
        vm[((j)*2)] = vs[j]
        vm[((j)*2)+1] = vs[j]
        if (j < max(range(0,len(h)))):
            pm[((j)*2)+1] = sum(h[0:j+1])
            pm[((j)*2)+2] = sum(h[0:j+1])
        else:
            pm[((j)*2)+1] = sum(h[0:j+1]) + 100
    pmb = pm[pm < profundidad[ind]]
    pmb = np.append(pmb,profundidad[ind])
    vmb = vm[pm < profundidad[ind]]
    vmb = np.append(vmb,vmb[-1])
    plt.plot(vmb,pmb,'k')

plt.show()
plt.gca().invert_yaxis()
plt.xlabel("Vs (m/s)", fontsize=13)
plt.xticks(fontsize=11)
plt.ylabel("Profundidad (m)", fontsize=13)
plt.yticks(fontsize=11)
plt.title("Modelos de velocidad Cluster 4",fontsize=14)
plt.grid()

plt.savefig("Models_cliuster4-13.png")