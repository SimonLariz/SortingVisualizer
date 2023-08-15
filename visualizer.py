"""Visualizer for sorting algorithms with matplotlib"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Visualizer:
    """Class for visualizing sorting algorithms"""
    def __init__(self, arr, max_val, title="Sorting Visualizer"):
        self.arr = arr
        self.fig, self.ax = plt.subplots()
        self.fig.set_facecolor("lightgray")
        self.ax.set_title(title, size=15)
        self.bar_rects = self.ax.bar(range(len(arr)), arr, align="edge")
        self.ax.set_xlim(0, len(arr))
        self.ax.set_ylim(0, max_val * 1.1)
        self.text = self.ax.text(0.02, 0.95, "", transform=self.ax.transAxes)
        self.iteration = 0
        self.text.set_text(f"# of operations: {self.iteration}")

    def update(self, frame):
        """Update the graph"""
        self.iteration += 1
        self.text.set_text(f"# of operations: {self.iteration}")
        for rect, val in zip(self.bar_rects, frame):
            rect.set_height(val)
    
    def animate_plot(self, generator):
        """Animate the plot"""
        anim = animation.FuncAnimation(self.fig, self.update, frames=generator, interval=1,repeat=False, cache_frame_data=False)
        self.fig.canvas.manager.set_window_title("Sorting Visualizer")
        plt.show()

