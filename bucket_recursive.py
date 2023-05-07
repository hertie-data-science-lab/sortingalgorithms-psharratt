#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Submitted on 7th May 2023

SUBMISSION ASSIGNMENT 10 

@authors: Fabian Metz | Paul Sharratt | Amin Oueslati | Oskar Krafft 

"""


def recursive_bucket_sort(array, bucket_size=5):
    """
    Sorts an array using a recursive bucket sort algorithm.
    
    Args:
        array (list): The list of integers and/or floating-points to be sorted.
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
    range_size = max_value - min_value
    # Create empty buckets
    buckets = [[] for _ in range(bucket_size + 1)]
    
    for j in array:
        # Calculate bucket index j should be placed in
        index_b = int((j - min_value) / range_size * bucket_size)
        # Add j to corresponding bucket
        buckets[index_b].append(j)

    # Sort the elements of each bucket recursively
    sorted_buckets = []
    for i in range(bucket_size + 1):
        if len(buckets[i]) > 0:
            sorted_bucket = recursive_bucket_sort(buckets[i])
            sorted_buckets.extend(sorted_bucket)

    return sorted_buckets
