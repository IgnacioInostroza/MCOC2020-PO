# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 19:02:51 2020

@author: ignacio
"""

from time import perf_counter

import scipy as sp
import scipy.linalg as spLinalg
import numpy as np

from numpy import float32 
def matriz_laplaceana(N, d=float32):
    L = -(np.eye(N, k=-1, dtype=d)) + 2 * \
        (np.eye(N, dtype=d)) + -(np.eye(N, k=+1, dtype=d))
    return L    

Ns=[2, 5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100, 125, 160, 200, 250, 350, 500, 600, 800, 1000, 2000, 5000]

Ncorridas = 10

names = ["A_invB_inv.txt", "A_invB_npSolve.txt"]

files = [open(name, "w") for name in names]

for N in Ns:
    dts = np.zeros((Ncorridas, len(files)))
    print (f"N={N}")
    
    for i in range(Ncorridas):
        print(f"i = {i}")
        
        #invirtiendo y multiplicando
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = A_inv@B
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][0] = dt
        
        #ocupando np.linalg.solve(A,B)
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = np.linalg.solve(A, B)
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][1] = dt
        
    print ("dts: ", dts)

    dts_mean = [np.mean(dts[:,j]) for j in range(len(files))]
    
    print ("dts_mean: ", dts_mean)  
    
    
    #escribo en el archivo de texto los resultados
    for j in range(len(files)):
        files[j].write(f"{N} {dts_mean[j]}\n")
        files [j].flush()
             
[file.close() for file in files]
        
        
        
        
        
        