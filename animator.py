# Example of animation from:
# http://stackoverflow.com/questions/9401658/matplotlib-animating-a-scatter-plot

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class AnimatedScatterPlot(object):
    def __init__(self , num_points=50):
        self.num_points = num_points
        self.stream = self.data_stream()
        self.fig, self.ax = plt.subplots()
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=5,
                                           init_func=self.setup_plot, blit=True)

    def setup_plot(self):
        pass

    def data_stream(self):
        pass

    def update(self, i):
        pass

    def show(self):
        plt.show()

def plot_2d(datapoints):
    # Create a new Figure and Axes
    fig, ax = plt.subplots()
    x = []
    y = []
    for point in datapoints:
        x.append(point[0])
        y.append(point[1])
    scatter_plot = ax.scatter(x, y)
    plt.show()


if __name__ == '__main__':
    plot_2d([[1, 1], [2, 2], [3, 3]])
