# -*- coding: utf-8 -*-
"""
Submitted on 7th May 2023

SUBMISSION ASSIGNMENT 10 

@authors: Fabian Metz | Paul Sharratt | Amin Oueslati | Oskar Krafft 

"""
import math #to call math.floor() in order to prevent endless recursion on floating points.

def bucketSort(array):
    bucket = []
    """
    Args:
        array (list): The list of integers and/or floating-points to be sorted.
        
    Returns:
        list: A sorted version of the input array.
        
    Please note: We amended bucketSort() to handle floating-point numbers
    We added math.ceil() to round up and created bucket range sizes with min() and max(). 
    """

    # Find the maximum and minimum values in the array
    max_value = max(array)
    min_value = min(array)

    num_buckets = len(array)

    # Create empty buckets
    for i in range(num_buckets):
        bucket.append([])

    # Calculate the range size for each bucket
    range_size = math.ceil((max_value - min_value + 1) / num_buckets)

    # Insert elements into their respective buckets
    for j in array:
        index_b = int((j - min_value) / range_size)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(num_buckets):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(num_buckets):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array
