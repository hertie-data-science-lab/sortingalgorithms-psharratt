#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Submitted on 7th May 2023

SUBMISSION ASSIGNMENT 10 

@authors: Fabian Metz | Amin Oueslati | Oskar Krafft | Paul Sharratt

"""
from recursive_bucket import recursive_bucket_sort

"""
Testing recursive_bucket_sort() on:
    - an array of mixed data types
    - an array of floats
    - an array of integers
    - an empty array
"""
array_mixed = [-4, 42, 32, 23, 25, 52, -1.3, 47, 751, 100,0.1,10,0.2]
array_floats = [0.1,0.11,0.13,0.893,0.2]
array_ints =[42, 32, 23, 25, 52, 47]
array_empty = []

# Use the recursive_bucket_sort function to sort the mixed, float, ints arrays 
print(recursive_bucket_sort(array_mixed))
print(recursive_bucket_sort(array_floats)) 
print(recursive_bucket_sort(array_ints))
print(recursive_bucket_sort(array_empty))

