import TestFunctions as tests
import matplotlib.pyplot as plt
import scipy


if __name__ == '__main__':
    max_inc = 70
    x_axis = list(range(1, max_inc+1))
    data1 = tests.testingIncStages(50, 5, max_inc)
    plt.subplot(1, 4, 1)
    plt.plot(x_axis, data1, 'ro', label='Incrementing number of stages\nRoute size: '+str(5))
    plt.xlabel('Number of routes')
    plt.ylabel('avg time to run algorithm (in seconds)')
    plt.title("Incremening number of stages.\n50 test cases per increment\nroutes: 5, stages: 1-" + str(max_inc))

    data2 = tests.testingIncRoutes(50, 5, max_inc)
    plt.subplot(1, 4, 2)
    plt.plot(x_axis, data2,  'bo', label='Incrementing number of routes\nStages size: '+str(5))
    plt.xlabel('number of stages')
    plt.ylabel('avg time to run algorithm (in seconds)')
    plt.title("Incremening number of routes.\n50 test cases per increment\nstages: 5, routes: 1-" + str(max_inc))

    data3 = tests.testingIncBoth(10, 50)
    plt.subplot(1, 4, 3)
    x_axis2 = list(range(1, 50 + 1))
    plt.plot(x_axis2, data3, 'go', label='Incrementing both at the same time')
    plt.xlabel('number of routes & stages (routes == stages)')
    plt.ylabel('avg time to run algorithm (in seconds)')
    plt.title("Incremening both stages and routes at the same time.\n10 test cases per increment\nRoutes & stages: 1-50")

    plt.subplot(1, 4, 4)
    plt.plot(x_axis, data1, 'ro', label='Incrementing number of stages\nRoute size: '+str(5))
    plt.plot(x_axis, data2, 'bo', label='Incrementing number of routes\nStages size: ' + str(5))
    plt.plot(x_axis2, data3, 'go', label='Incrementing both at the same time')
    plt.xlabel('number of incremented variable')
    plt.ylabel('avg time to run algorithm (in seconds)')
    plt.title("Comparison between three previous graphs")
    plt.xlim(1, max_inc)
    plt.legend()
    plt.show()


