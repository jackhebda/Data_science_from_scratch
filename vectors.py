# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:05:27 2020

@author: Jacek
"""
import math

def vector_add(v, w):
    return [vi + wi for vi, wi in zip(v, w)]

def vector_subtract(v, w):
    return [vi - wi for vi, wi in zip(v, w)]

def vector_sum(vectors):
    result = vectors[0]
    for vi in vectors[1:]:
        result = vector_add(result,vi)
    return result

def scalar_mul(c, vector):
    return [c * vi for vi in vector]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_mul(1/n, vector_sum(vectors))

def dot(v, w):
    return sum(vi * wi for vi, wi in zip(v,w)) 
    
def sum_of_sqares(v):
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_sqares(v))

def distance(v, w):
    return magnitude(vector_subtract(v, w))


print(distance([1, 1 ,2], [3, 4, 1]))
