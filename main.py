"""Entry point for the sorting visualizer"""

import sorting_algorithms
import utils


def main():
    """Main function for the sorting visualizer"""
    print("Sorting Visualizer")
    random_array = utils.generate_random_array(20, 200)
    print(random_array)
    sorted_array = sorting_algorithms.bubble_sort(random_array)
    print(sorted_array)

    return 0


if __name__ == "__main__":
    main()
