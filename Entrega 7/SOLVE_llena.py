# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 16:59:30 2020

@author: ignacio
"""

from numpy import *
from scipy.linalg import solve
from time import perf_counter
#from scipy import savetxt
import numpy as np


def matriz_laplaciana_llena(N,t=np.float32):
    A=np.identity(N,t)*2
    for i in range(N):
        for j in range(N):
            if i +1 == j:
                A[i,j] = -1
            if i -1 == j:
                A[i,j] = -1
    return A            
    

Ns=[2, 5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100, 125, 160, 200, 250, 350, 500, 600, 800, 1000, 2000]

Ncorridas = 4

for i in range(Ncorridas):
    
    dtens=[] #Lista para tiempos de ensamblado
    dtsol=[] #Lista para tiempos de solucion
    
    name=(f"solve_llena_corrida{i}.txt") #creo los archivos corresponden a cada corrida que seran lineas grises
    
    fid=open(name, "w")
    
    for N in Ns:
        print(f"corrida{i}:")
        print(f"N={N}")
         
        t1=perf_counter()
        
        A=matriz_laplaciana_llena(N)
        b=np.ones(N)
        
        t2=perf_counter()
        
        x=solve(A, b)
        
        t3=perf_counter()
        
        dt1 = t2 - t1 #Tiempo de ensamblado
        dt2 = t3 - t2 #Tiempo de solucion 
        
        dtens.append(dt1) #agrego tiempo ensamblado
        dtsol.append(dt2) #agrego tiempo solucion 
        
        fid.write(f"{N} {dt1} {dt2}\n")
        
        print(f"tiempo de ensamblado = {dt1}")
        print(f"tiempo de solucion = {dt2}\n")
    
        fid.flush()
        
fid.close()   
        
        
 
               
        
