# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:49:56 2020

@author: Jacek
"""

def median(vector):
    n = len(vector)
    vector = sorted(vector)
    if n % 2 == 1:
        return vector[n//2]
    
    else:
        return (vector[n//2 - 1] + vector[n//2])/2

def shape(A):
    n = len(A)
    k = len(A[0]) if A else 0
    return n, k

def get_column(A, j):
    return [Ai[j] for Ai in A]

def make_matrix(n, k , function):
    return [[function(i, j) 
            for j in range(k)]
            for i in range(n)]
    
def one(n, k):
    return 1 if n == k else 0

print(median([1,2,3,4,5,6]))