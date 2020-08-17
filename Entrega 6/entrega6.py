# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:31:52 2020

@author: ignacio
"""

from time import perf_counter

import scipy.linalg as spLinalg
import numpy as np

from numpy import float32 

def matriz_laplaceana(N, d=float32):
    L = -(np.eye(N, k=-1, dtype=d)) + 2 * \
        (np.eye(N, dtype=d)) + -(np.eye(N, k=+1, dtype=d))
    return L    

Ns=[2, 5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100, 125, 160, 200, 250, 350, 500, 600, 800, 1000, 2000, 3000, 5000]

Ncorridas = 5

names = ["A_invB_inv.txt", "A_invB_npSolve.txt", "A_invB_spSolve.txt", "A_invB_spSolve_symmetric.txt", "A_invB_spSolve_pos.txt", "A_invB_spSolve_pos_overwrite.txt"]

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
        
        #ocupando np.linalg.solve(A, B)
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = np.linalg.solve(A, B)
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][1] = dt
        
        #ocupando spLinalg.solve(A, B)
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = spLinalg.solve(A, B)
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][2] = dt
        
        #ocupando spLinalg.solve(A, B, assume_a="sym")
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = spLinalg.solve(A, B, assume_a = "sym")
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][3] = dt
        
        #ocupando spLinalg.solve(A, B, assume_a="pos")
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = spLinalg.solve(A, B, assume_a = "pos")
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][4] = dt
        
        #ocupando spLinalg.solve(A, B, assume_a="pos", ow_a=True, ow_b=True)
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = spLinalg.solve(A, B, assume_a = "pos", overwrite_a=True, overwrite_b=True)
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][5] = dt
        
               
        
    print ("dts: ", dts)

    dts_mean = [np.mean(dts[:,j]) for j in range(len(files))]
    
    print ("dts_mean: ", dts_mean)  
    
    
    #escribir en el archivo de texto los resultados
    for j in range(len(files)):
        files[j].write(f"{N} {dts_mean[j]}\n")
        files [j].flush()
             
[file.close() for file in files]

        