# -*- coding: utf-8 -*-
"""
Submitted on 19th April 2023

SUBMISSION ASSIGNMENT 8 

@authors: Fabian Metz | Amin Oueslati | Oskar Krafft | Paul Sharratt
"""

def recursive_radix_sort(arr, exp=1):
    """
    Sorts an array of integers using recursive radix sort algorithm.

    :param arr: A list of integers to be sorted.
    :param exp: The current digit position (default is 1 for the least significant digit).
    :return: A sorted list of integers.
    """
    # Base case: all digits have been processed
    if not arr or exp > len(str(max(arr))):
        return arr

    # Create 10 empty buckets (0-9)
    buckets = [[] for _ in range(10)]

    # Iterate through the input data and place each element in the appropriate bucket
    for num in arr:
        digit = (num // (10 ** (exp - 1))) % 10
        buckets[digit].append(num)

    # Recursively sort each bucket using the next digit position
    sorted_buckets = [recursive_radix_sort(bucket, exp + 1) for bucket in buckets] # THE ERROR IS HERE BUCKETS ARE EMPTY ON RECURSIVE CALL

    # Concatenate the sorted buckets to form a new sequence
    return [num for bucket in sorted_buckets for num in bucket]
