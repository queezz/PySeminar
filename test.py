import numpy as np
import matplotlib.pylab as plt


def testplot():
    """ Just plots some data for our test in Juyter Lab
    """
    x = np.linspace(-1, 1, 100)
    y = x ** 2

    plt.plot(x, y, "C1s-", label="some label")

    plt.legend()
    # plt.grid()
