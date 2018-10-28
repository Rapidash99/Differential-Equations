import numpy as np
from matplotlib import pyplot as plt

"""
1st variant
y' = -y - x
B17-02
Vyacheslav Vasilev
"""

"""Function that read count of steps from the console"""


def read():
    print("\nWrite down the number of steps below")

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

    return count


"""Main class of our methods that contains all attributes and functions"""


class NumericalMethods:
    """Constructor"""

    def __init__(self, x0, x_last, y0, count):
        self.x0 = x0
        self.x_last = x_last
        self.y0 = y0
        self.count = count

        self.x = np.linspace(x0, x_last, count)  # x axis is the same for each method, so just x
        self.h = self.x[1] - self.x[0]  # step h
        self.y1 = np.zeros(count)  # creating array of y's for each method and filling them by 0's
        self.y2 = self.y1.copy()
        self.y3 = self.y1.copy()
        self.y4 = self.y1.copy()
        self.y5 = self.y1.copy()
        self.y6 = self.y1.copy()
        self.y7 = self.y1.copy()

    """Euler method's function that calculate resulting graph's y axis and put it in y1 array"""

    def euler(self):
        x = self.x
        y = self.y1
        h = self.h

        for i in range(1, self.count):
            y[i] = y[i - 1] + h * (-x[i - 1] - y[i - 1])

    """Improved Euler method's function that calculate resulting graph's y axis and put it in y2 array"""

    def improved_euler(self):
        x = self.x
        y = self.y2
        h = self.h

        for i in range(1, self.count):
            y[i] = y[i - 1] + h * (-(x[i - 1] + (h / 2)) - (y[i - 1] + (h / 2) * (-x[i - 1] - y[i - 1])))

    """Runge-Kutta method's function that calculate resulting graph's y axis and put it in y3 array"""

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

    """Exact solution's function that calculate resulting graph's y axis and put it in y4 array"""

    def exact(self):
        x = self.x
        y = self.y4

        """
        y = c * e^(-x) - x + 1
        
        for IVP, my exact solution is
        
        1 = c * e^(0) - 0 + 1     =>     c = 0
        y = 0 * e^(-x) - x + 1
        y = -x + 1
        """

        for i in range(self.count):
            y[i] = -x[i] + 1

    """Function that calculate each plot"""

    def calculate(self):
        self.euler()  # y for Euler
        self.improved_euler()  # y for Improved Euler
        self.runge_kutta()  # y for Runge-Kutta
        self.exact()  # y for Exact

        np.zeros(self.count)
        np.zeros(self.count)
        np.zeros(self.count)

        for i in range(len(self.x)):
            self.y5[i] = self.y4[i] - self.y1[i]  # y for Euler truncation errors
            self.y6[i] = self.y4[i] - self.y2[i]  # y for Improved Euler truncation errors
            self.y7[i] = self.y4[i] - self.y3[i]  # y for Runge-Kutta truncation errors

    """
    Function that draw 3 plots:
    1) Exact solution
    2) Euler, Improved Euler, Runge-Kutta solutions
    3) Truncation errors for 2)
    """

    def draw(self):
        """Drawing plot for exact solution"""
        plt.subplot(311)
        plt.plot(self.x, self.y4, 'm', label="Exact")

        plt.legend(loc='upper right')
        plt.grid(True)
        plt.xlabel("x")
        plt.ylabel("y")

        """
        Drawing plots for Euler, Improved Euler, Runge-Kutta method's solutions
        They're the same for my differential equation y' = -y - x, so they're lie on each other
        """
        plt.subplot(312)
        plt.plot(self.x, self.y1, 'b', label="Euler")
        plt.plot(self.x, self.y2, 'g', label="Improved Euler")
        plt.plot(self.x, self.y3, 'r', label="Runge-Kutta")

        plt.legend(loc='upper right')
        plt.grid(True)
        plt.xlabel("x")
        plt.ylabel("y")

        """
        Drawing plots of truncation errors for Euler, Improved Euler, Runge-Kutta method's solutions
        """

        plt.subplot(313)
        plt.plot(self.x, self.y5, 'b', label="Euler's Errors")
        plt.plot(self.x, self.y6, 'g', label="Improved Euler's Errors")
        plt.plot(self.x, self.y7, 'r', label="Runge-Kutta's Errors")

        plt.legend(loc='upper right')
        plt.grid(True)
        plt.xlabel("x")
        plt.ylabel("y")

        """Show plots"""
        plt.show()


"""Read count of steps from the console"""
count = read()

"""Create numerical methods for x0 = 0, X = 10, y0 = 1, count"""
num = NumericalMethods(0, 10, 1, count)

"""Calculate them"""
num.calculate()

"""Draw them"""
num.draw()
