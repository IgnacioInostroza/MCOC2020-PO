# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 20:51:55 2020

@author: ignacio
"""

from numpy import *
#from scipy.linalg import solve
from time import perf_counter
#from scipy import savetxt
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve
import numpy as np              
from scipy.sparse import lil_matrix


def matriz_laplaciana_dispersa(N,t=np.float32):
    A=lil_matrix((N,N))
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i,j] = 2
            if i +1 == j:
                A[i,j] = -1
            if i -1 == j:
                A[i,j] = -1
    return (A) 
    



Ns=[2, 5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100, 125, 160, 200, 250, 350, 500, 600, 800, 1000]

Ncorridas = 4

for i in range(Ncorridas):
    
    dtens=[] #Lista para tiempos de ensamblado
    dtsol=[] #Lista para tiempos de solucion
    
    name=(f"inv_dispersa_corrida{i}.txt") #creo los archivos corresponden a cada corrida que seran lineas grises
    
    fid=open(name, "w")
    
    for N in Ns:
        print(f"corrida{i}:")
        print(f"N={N}")
        t1=perf_counter()

        A_lil=matriz_laplaciana_dispersa(N)
        A_csc=csc_matrix(A_lil)
        B=np.ones(N)
        A_inv = np.linalg.inv(A_csc)
        
        t2=perf_counter()
        
        C = np.matmul(A_inv,B)    
        
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
        
        