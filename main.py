# -*- coding: utf-8 -*-
"""
Submitted on 7th May 2023

SUBMISSION ASSIGNMENT 10 

@authors: Fabian Metz | Amin Oueslati | Oskar Krafft | Paul Sharratt
"""
from bucket import recursive_bucket_sort, bucketSort


array = [42, 32, 23, 25, 52, 47, 751, 100,0.1,10,0.2]
array_floats=[0.1,0.11,0.13,0.893,0.2]
array_ints=[42, 32, 23, 25, 52, 47]

print(bucketSort(array))

print(recursive_bucket_sort(array))
print(recursive_bucket_sort(array_floats)) 
print(recursive_bucket_sort(array_ints))