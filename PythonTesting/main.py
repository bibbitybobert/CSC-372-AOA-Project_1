import TestFunctions as tests
import matplotlib.pyplot as plt
import scipy


if __name__ == '__main__':
    max_inc = 70
    x_axis = list(range(1, max_inc+1))
    data1 = tests.testingIncStages(50, 5, max_inc)
    plt.subplot(1, 3, 1)
    plt.plot(x_axis, data1, 'ro', label='Incrementing number of stages\nRoute size: '+str(5))

    data2 = tests.testingIncRoutes(50, 5, max_inc)
    plt.subplot(1, 3, 2)
    plt.plot(x_axis, data2,  'bo', label='Incrementing number of routes\nStages size: '+str(5))

    data3 = tests.testingIncBoth(10, 50)
    plt.subplot(1, 3, 3)
    x_axis2 = list(range(1, 50 + 1))
    plt.plot(x_axis2, data3, 'go', label='Incrementing both at the same time')

    plt.xlabel('size of incremented variable')
    plt.ylabel('time to run algorithm (in seconds)')
    plt.xlim(1, max_inc)
    plt.legend()
    plt.show()


