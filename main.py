"""Entry point for the sorting visualizer"""

import sorting_algorithms
import utils
import visualizer

def main():
    """Main function for the sorting visualizer"""
    print("Sorting Visualizer")
    random_array = utils.generate_random_array(300, 200)
    selection_sort_generator = sorting_algorithms.selection_sort(random_array)
    myVisualizer = visualizer.Visualizer(random_array, 200, "Selection Sort")
    myVisualizer.animate_plot(selection_sort_generator)
    return 0


if __name__ == "__main__":
    main()
