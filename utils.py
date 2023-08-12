"""Collection of utility functions for the sorting visualizer"""
from random import randint


def generate_random_array(size, max_val):
    """Generate a random array of integers"""
    return [randint(1, max_val) for _ in range(size)]
