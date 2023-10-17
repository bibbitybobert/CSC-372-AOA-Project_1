import TestFunctions as tests
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = tests.testingIncStages(10, 5, 70)
    plt.plot(data, 'ro', label='Incrementing number of stages')

    data = tests.testingIncRoutes(10, 5, 70)
    plt.plot(data, 'bo', label='Incrementing number of routes')
    plt.xticks(plt.xticks()[0][1::5])
    plt.legend()
    plt.show()


