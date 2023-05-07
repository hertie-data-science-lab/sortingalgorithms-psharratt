# -*- coding: utf-8 -*-
"""
Submitted on 7th May 2023

SUBMISSION ASSIGNMENT 10 

@authors: Fabian Metz | Paul Sharratt | Amin Oueslati | Oskar Krafft 

"""
import math #to call math.floor() in order to prevent endless recursion on floating points.

def recursive_bucket_sort(array, bucket_size=5):
    """
    Sorts an array using a recursive bucket sort algorithm.
    
    Args:
        array (list): The list of integers to be sorted.
        bucket_size (int, optional): The size of each bucket. Defaults to 5.
        
    Returns:
        list: A sorted version of the input array.
    """
    if len(array) <= 1:
        return array

    # Find the maximum and minimum values in the array
    max_value = max(array)
    min_value = min(array)

    # Calculate the range for each bucket
    range_size = (max_value - min_value) / bucket_size

    # Create empty buckets
    buckets = [[] for _ in range(bucket_size + 1)]

    # Insert elements into their respective buckets
    for j in array:
        if isinstance(j, float):
            index_b = min(math.floor((j - min_value) / range_size * bucket_size), bucket_size)
        else:
            index_b = int((j - min_value) / range_size)
        buckets[index_b].append(j)

    # Sort the elements of each bucket recursively
    sorted_buckets = []
    for i in range(bucket_size + 1):
        if len(buckets[i]) > 0:
            sorted_bucket = recursive_bucket_sort(buckets[i])
            sorted_buckets.extend(sorted_bucket)

    return sorted_buckets



def bucketSort(array):
    bucket = []
    """
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
