import numpy as np 
import matplotlib.pyplot as plt

"""
Plotting exercise. 
Fourier series are used to approximate periodic functions with a sum of sine and cosine functions.
In this exercise we have a look at a rectangular pulse. The aim is to plot this rectangular pulse, the individual 
terms of the fourier series and the approximation obtained by the fourier series. Therefore go through the code and 
work on the TODOS."""


def fourier_rechteck_puls(x, amp=1, depth=2000):
    """
    :param x:
        array like. Used as x values to calculate values of fourier series
    :param amp:
        Amplitude of rectangular pulse
    :param depth:
        Number of terms of series calculated
    :return:
        2 dimensional array with single terms of fourier series
    """
    f_g = []
    for i in range(1, depth + 1):
        f = 4 * amp / np.pi * np.sin((2 * i - 1) * x) / (2 * i - 1)  # i-th term of the fourier series is calculated
        f_g.append(f.tolist())  # i-th term is added to list
    return f_g

    
if __name__ == '__main__':
    # TODO: define x axis from - 2 pi to 2 pi-. HINT: check out numpy arange or numpy linspace
    x_axis = np.linspace(-np.pi, np.pi, 101)
    #x_axis = np.linspace(-2*np.pi, 2*np.pi, 101)

    fig = plt.figure(figsize =(10, 25))  # reference to figure object
    ax = fig.add_subplot(311)  # reference to axis object (this is where you actually plot something)

    # TODO: Plot a rectangular pulse, which is 1 if x is between -2 pi and -pi or between 0 and pi and
    #                                         -1 if x is between -pi and 0 or pi and 2 pi
    #       check out np.ones() and np.where() or use lists
    y_axis = []
    for x in x_axis:
        if x <0:
            y_axis.append(-1)
        else:
            y_axis.append(1)

    ax.set_title('sex.com', fontsize=30 )
    ax.plot(x_axis, y_axis)

    fourier_sol = fourier_rechteck_puls(x_axis)
    # TODO: Plot the solution of the fourier series, the sum as well as the single terms.

    axf = fig.add_subplot(312)
    for x in fourier_sol:
        axf.plot(x_axis, x)
    
    axsum = fig.add_subplot(313)
    sum = np.sum(fourier_sol, axis = 0)
    axsum.plot(x_axis, sum)

    plt.show()





