import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def plot_2d(data):
    # Create a new Figure and Axes
    fig, ax = plt.subplots()
    x = data[0]
    y = data[1]
    scatter_plot = ax.scatter(x, y)
    plt.show()

if __name__ == '__main__':
    plot_2d([[1, 2, 3, 4], [1, 2, 3, 4]])
