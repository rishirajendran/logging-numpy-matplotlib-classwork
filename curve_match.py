import numpy as np
import matplotlib.pyplot as plt


def main():

    with open('curve_to_match.dat') as f:
        time = f.readline().strip('\n').split(',')
        signal = f.readline().strip('\n').split(',')

    time_vals = [float(val) for val in time]
    signal_vals = [float(val) for val in signal]

    plt.plot(time_vals, signal_vals)

    amp1 = 1
    amp2 = 2
    freq1 = 2
    freq2 = 3

    time_arr = np.array(time_vals)

    curve1 = amp1 * np.sin(freq1 * time_arr)
    curve2 = amp2 * np.cos(freq2 * time_arr)

    test_curve = curve1 + curve2
    plt.plot(time_vals, test_curve, 'r')


if __name__ == "__main__":
    main()
