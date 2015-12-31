import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
    plot_2d([[1, 2, 3, 4], [1, 2, 3, 4]])
