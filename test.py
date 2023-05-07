# -*- coding: utf-8 -*-
"""
Submitted on 7th May 2023

SUBMISSION ASSIGNMENT 10 

@authors: Fabian Metz | Amin Oueslati | Oskar Krafft | Paul Sharratt
"""
# Imports the required sorting functions from the bucket module
from bucket_recursive import recursive_bucket_sort
from bucket import bucketSort


# Define an array of mixed data types
array_mixed = [-4, 42, 32, 23, 25, 52, -1.3, 47, 751, 100,0.1,10,0.2]

# Define an array specifically for floating-point values
array_floats=[0.1,0.11,0.13,0.893,0.2]

# Define an array specifically for integer values
array_ints=[42, 32, 23, 25, 52, 47]

# Use the recursive_bucket_sort function to sort the mixed, float, ints arrays using recursive bucket sort
print(recursive_bucket_sort(array_mixed))
print(recursive_bucket_sort(array_floats)) 
print(recursive_bucket_sort(array_ints))

