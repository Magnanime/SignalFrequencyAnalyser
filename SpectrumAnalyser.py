import numpy
import matplotlib.pyplot as plot
import scipy.fftpack




def square_wave_creator(x_axis,square_accuracy):
    y = 0
    temp = 1
    for z in range(0, square_accuracy):
        y = y + numpy.sin(x_axis*temp)/temp
        temp = temp + 2
    return y


def main():
    N = 500
    # sample spacing
    T = 1.0 / 10
    x = numpy.linspace(0.0, N * T, N)
    y = square_wave_creator(x,50) # Creating a square wave like signal from pure sine waves


    fig, ax = plot.subplots()
    ax.plot(x,y)
    plot.grid()
    plot.xlabel("Time axis")
    plot.ylabel("Amplitude axis")
    plot.title("Time domain")
    plot.show()

    yfour = scipy.fftpack.fft(y)
    xfour = numpy.linspace(0.0, 1.0 / (2.0 * T), N / 2)

    fig1, ax1 = plot.subplots()
    ax1.plot(xfour, 2.0 / N * numpy.abs(yfour[:N // 2]))
    plot.xlabel("Frequency axis")
    plot.ylabel("Amplitude axis")
    plot.title("Frequency domain")
    plot.grid()
    plot.show()

if __name__ == "__main__":
    main()