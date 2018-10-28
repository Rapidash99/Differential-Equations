import numpy as np
from math import exp
from matplotlib import pyplot as plt
from matplotlib import ticker as tck

"""
1st variant
y' = -y - x
B17-02
Vyacheslav Vasilev
"""

"""Function that read initial conditions from the console"""


def read():
    print("\nWrite down the x0 below")

    while True:
        try:
            x0 = float(input())
            break
        except ValueError:
            print("x0 must be a float value\nPlease, try again")

    print("Write down the X below")

    while True:
        try:
            X = float(input())
            if X < x0:
                print("X must be above x0\nPlease, try again")
                continue
            break
        except ValueError:
            print("X must be a float value\nPlease, try again")

    print("Write down the y0 below")

    while True:
        try:
            y0 = float(input())
            break
        except ValueError:
            print("y0 must be a float value\nPlease, try again")

    print("Write down the number of steps below")

    while True:
        try:
            count = int(input())
            if count <= 0:
                print("Number of steps must be above zero\nPlease, try again")
                continue
            elif count == 1:
                print("Number of steps could not be equal 1 because of logic reasons\nPlease, try again")
                continue
            break
        except ValueError:
            print("Number of steps must be an integer value\nPlease, try again")

    print("Write down the grid step by x below")

    while True:
        try:
            x_step = float(input())
            if x_step <= 0:
                print("Grid step by x must be positive\nPlease, try again")
                continue
            break
        except ValueError:
            print("Grid step by x must be a float value\nPlease, try again")

    print("Write down the grid step by y below")

    while True:
        try:
            y_step = float(input())
            if y_step <= 0:
                print("Grid step by y must be positive\nPlease, try again")
                continue
            break
        except ValueError:
            print("Grid step by y must be a float value\nPlease, try again")

    return x0, X, y0, count, x_step, y_step


"""Class of our methods that contains all attributes and functions"""


class NumericalMethods:
    """Constructor"""

    def __init__(self, x0, X, y0, count):
        self.x0 = x0
        self.X = X
        self.y0 = y0
        self.count = count

        self.x = np.linspace(x0, X, count)  # x-axis is the same for each method, so just x
        self.h = self.x[1] - self.x[0]  # step h
        self.y1 = np.zeros(count)  # creating array of y's for Euler method and filling it by 0's
        self.y2 = self.y1.copy()  # creating array of y's for Improved Euler method and filling it by 0's
        self.y3 = self.y1.copy()  # creating array of y's for Runge-Kutta method and filling it by 0's
        self.y4 = self.y1.copy()  # creating array of y's for Exact method and filling it by 0's
        self.y5 = self.y1.copy()  # creating array of y's for Euler's errors and filling it by 0's
        self.y6 = self.y1.copy()  # creating array of y's for Improved Euler's errors and filling it by 0's
        self.y7 = self.y1.copy()  # creating array of y's for Runge-Kutta's errors and filling it by 0's

    """Euler method's function that calculates resulting graph's y-axis and put it in the y1 array"""

    def euler(self):
        x = self.x
        y = self.y1
        h = self.h

        for i in range(1, self.count):
            y[i] = y[i - 1] + h * (-x[i - 1] - y[i - 1])

    """Improved Euler method's function that calculates resulting graph's y-axis and put it in the y2 array"""

    def improved_euler(self):
        x = self.x
        y = self.y2
        h = self.h

        for i in range(1, self.count):
            y[i] = y[i - 1] + h * (-(x[i - 1] + (h / 2)) - (y[i - 1] + (h / 2) * (-x[i - 1] - y[i - 1])))

    """Runge-Kutta method's function that calculates resulting graph's y-axis and put it in the y3 array"""

    def runge_kutta(self):
        x = self.x
        y = self.y3
        h = self.h

        for i in range(1, self.count):
            k1 = -x[i - 1] - y[i - 1]
            k2 = -(x[i - 1] + (h / 2)) - (y[i - 1] + ((h * k1) / 2))
            k3 = -(x[i - 1] + (h / 2)) - (y[i - 1] + ((h * k2) / 2))
            k4 = -(x[i - 1] + h) - (y[i - 1] + h * k3)

            y[i] = y[i - 1] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    """Exact solution's function that calculates resulting graph's y-axis and put it in the y4 array"""

    def exact(self):
        x = self.x
        y = self.y4

        """
        y' = -y - x
        y = c * e^(-x) - x + 1
        c = (y + x - 1) / (e^(-x))
        y = c * e^(-x) - x + 1
        """

        c = (self.y0 + self.x0 - 1) / exp(-self.x0)

        for i in range(self.count):
            y[i] = (c * exp(-x[i])) - x[i] + 1

    """Function that calculates each plot"""

    def calculate(self):
        self.euler()  # y for Euler
        self.improved_euler()  # y for Improved Euler
        self.runge_kutta()  # y for Runge-Kutta
        self.exact()  # y for Exact

        for i in range(len(self.x)):
            self.y5[i] = self.y4[i] - self.y1[i]  # y for Euler truncation errors
            self.y6[i] = self.y4[i] - self.y2[i]  # y for Improved Euler truncation errors
            self.y7[i] = self.y4[i] - self.y3[i]  # y for Runge-Kutta truncation errors

    """
    Function that draws 3 plots:
    1) Exact solution
    2) Euler, Improved Euler, Runge-Kutta solutions
    3) Truncation errors for Euler, Improved Euler, Runge-Kutta solutions
    """

    def draw(self, x_step, y_step):
        """Drawing plot for exact solution"""

        pl1 = plt.subplot(311)
        pl1.plot(self.x, self.y4, 'm', label="Exact")

        pl1.xaxis.set_major_locator(tck.MultipleLocator(base=x_step))
        pl1.yaxis.set_major_locator(tck.MultipleLocator(base=y_step))

        plt.legend(loc='upper right')
        plt.grid(True)
        plt.xlabel("x")
        plt.ylabel("y")

        """
        Drawing plots for Euler, Improved Euler, Runge-Kutta method's solutions
        They're the same for my differential equation y' = -y - x, so they're lie on each other
        """

        pl2 = plt.subplot(312)
        pl2.plot(self.x, self.y1, 'b', label="Euler")
        pl2.plot(self.x, self.y2, 'g', label="Improved Euler")
        pl2.plot(self.x, self.y3, 'r', label="Runge-Kutta")

        pl2.xaxis.set_major_locator(tck.MultipleLocator(base=x_step))
        pl2.yaxis.set_major_locator(tck.MultipleLocator(base=y_step))

        plt.legend(loc='upper right')
        plt.grid(True)
        plt.xlabel("x")
        plt.ylabel("y")

        """
        Drawing plots of truncation errors for Euler, Improved Euler, Runge-Kutta method's solutions
        """

        pl3 = plt.subplot(313)
        pl3.plot(self.x, self.y5, 'b', label="Euler's Errors")
        pl3.plot(self.x, self.y6, 'g', label="Improved Euler's Errors")
        pl3.plot(self.x, self.y7, 'r', label="Runge-Kutta's Errors")

        pl3.xaxis.set_major_locator(tck.MultipleLocator(base=x_step))
        pl3.yaxis.set_major_locator(tck.MultipleLocator(base=y_step))

        plt.legend(loc='upper right')
        plt.grid(True)
        plt.xlabel("x")
        plt.ylabel("y")

        """Show plots"""
        plt.show()


"""Read initial conditions and grid steps from the console"""
x0, X, y0, count, x_step, y_step = read()

"""Create numerical methods for initial conditions, read from console"""
num = NumericalMethods(x0, X, y0, count)

"""Calculate them"""
num.calculate()

"""Draw them for grid steps x and y"""
num.draw(x_step, y_step)
