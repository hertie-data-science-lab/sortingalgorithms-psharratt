#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Submitted on 7th May 2023

SUBMISSION ASSIGNMENT 10 

Authors: Fabian Metz | Amin Oueslati | Oskar Krafft | Paul Sharratt

Testing recursive_bucket_sort() on:
    - random arrays of mixed data types, including negative and repeated values
    - an empty array

"""

from recursive_bucket import recursive_bucket_sort
import random

def generate_random_array(size, min_value, max_value):
    """
    Generates a random array with a specified size, containing integers and floats.
    
    Args:
        size (int): The size of the array.
        min_value (int or float): The minimum value for generated numbers.
        max_value (int or float): The maximum value for generated numbers.

    Returns:
        list: a randomly generated array.

    """
    array = []
    for _ in range(size):
        if random.choice([True, False]):
            # Generate a random integer
            array.append(random.randint(min_value, max_value))
        else:
            # Generate a random float with two decimal places
            array.append(round(random.uniform(min_value, max_value), 2))
    return array

random_array_1 = generate_random_array(10, 1, 20)
random_array_2 = generate_random_array(5, -2, 2)
empty_array = []

print("Random Test Array 1:", random_array_1, "\nSorted Test Array 1:", recursive_bucket_sort(random_array_1), sep='')
print("Random Test Array 2:", random_array_2, "\nSorted Test Array 2:", recursive_bucket_sort(random_array_2), sep='')
print("Empty Array:", empty_array, "\nSorted Empty Array:", recursive_bucket_sort(empty_array), sep='')
