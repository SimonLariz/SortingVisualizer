"""Entry point for the sorting visualizer"""

import sorting_algorithms
import utils


def main():
    """Main function for the sorting visualizer"""
    print("Sorting Visualizer")
    random_array = utils.generate_random_array(20, 200)
    print("Unsorted arr", random_array)
    # Generator object returned by bubble_sort
    print("Bubble sort")
    bubble_sort_generator = sorting_algorithms.bubble_sort(random_array.copy())
    # Iterate over the generator object
    for arr in bubble_sort_generator:
        print(arr)
    print("Selection sort")
    selection_sort_generator = sorting_algorithms.selection_sort(random_array.copy())
    for arr in selection_sort_generator:
        print(arr)

    return 0


if __name__ == "__main__":
    main()
