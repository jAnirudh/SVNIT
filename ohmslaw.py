# Author: Anirudh Jonnalagadda, PhD
# email: anirudhj@iisc.ac.in

import  numpy
import matplotlib.pyplot as plot

resistance = 5

def get_data(nobs=75, plotfig=True):
    '''Synthetically created Noisy Data for Ohms Law.
    The current vector is equally spaced between 0 & 2.
    
    Input:
    ------
        1. nobs (int)
            number of observations. Default value of 75
    Returns:
    --------
        1. current (numpy.ndarray)
        2. voltage (numpy.ndarray)
    '''
    current = numpy.linspace(0, 2, nobs)
    voltage = resistance * current
    # superimpose a Gaussian Noise with mean 2 and
    # std deviation 1.5
    voltage += numpy.random.normal(0, 1.15, nobs)
    if plotfig: plot_figure(voltage, current)
    return current, voltage

def plot_figure(voltage, current):
    plot.plot(voltage, current, '.', label='Noisy Data', color='black')
    plot.plot(current*resistance, current, '--', label = 'Real')
    plot.legend()
    plot.xlabel('Current, I (Ampere)')
    plot.ylabel('Voltage, V (Volts)')