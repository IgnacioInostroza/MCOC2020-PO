# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:55:48 2020

@author: ignacio
"""

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
    return A    
    
    
    