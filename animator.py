# Based on example of scatter plot animation from:
# http://stackoverflow.com/questions/9401658/matplotlib-animating-a-scatter-plot

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Convert an list of (x, y) to a list of x and a list of y
def points_to_xy(points):
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    return x, y

class AnimatedScatterPlot(object):
    def __init__(self, scatter_plots):
        self.scatter_plots = scatter_plots
        self.stream = self.data_stream()
        self.fig, self.ax = plt.subplots()
        # Interval = ms
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=500,
                                           init_func=self.setup_plot, blit=True)

    def setup_plot(self):
        # Create initial plot based on first call to data_stream generator
        x, y = points_to_xy(next(self.stream))
        self.scat = self.ax.scatter(x=x, y=y, animated=True)
        self.ax.axis([-10, 10, -10, 10])
        # FuncAnimation expects a sequence of artists, so add trailing comma
        return self.scat,

    def data_stream(self):
        # Generator function that yields the next set of points
        for data_points in self.scatter_plots:
            yield data_points

    def update(self, i):
        # Set x and y data
        self.scat.set_offsets(next(self.stream))
        # FuncAnimation expects a sequence of artists, so add trailing comma
        return self.scat,

    def show(self):
        plt.show()

def plot_2d(datapoints):
    # Create a new Figure and Axes
    fig, ax = plt.subplots()
    x, y = points_to_xy(datapoints)
    scatter_plot = ax.scatter(x, y)
    plt.show()


if __name__ == '__main__':
    # Make animation of three scatter plots
    all_plots = [
        [[1, 1], [2, 2], [3, 3]],
        [[1, 2], [2, 2], [3, 2]],
        [[1, 3], [2, 2], [3, 1]],
        [[1, 3], [2, 2], [3, 0]]
    ]
    plotter = AnimatedScatterPlot(all_plots)
    plotter.show()

    # Plot this scatter plot
    # plot_2d([[1, 1], [2, 2], [3, 3]])
