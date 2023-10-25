import os
import random
import time
import statistics as stats

def runGivenTests():
    print('Test File A:')
    print('==============================================================')
    os.system('C:\dev\gitlab\csc372\Project1\Project1\Project1\Project1 C:\dev\gitlab\csc372\Project1\Project1\Project1\TestFiles\A-file.txt')

    print('\nTest File B:')
    print('==============================================================')
    os.system(
        'C:\dev\gitlab\csc372\Project1\Project1\Project1\Project1 C:\dev\gitlab\csc372\Project1\Project1\Project1\TestFiles\B-oneLine.txt')

    print('\nTest File C:')
    print('==============================================================')
    os.system(
        'C:\dev\gitlab\csc372\Project1\Project1\Project1\Project1 C:\dev\gitlab\csc372\Project1\Project1\Project1\TestFiles\C-oneStage.txt')

    print('\nTest File D:')
    print('==============================================================')
    os.system(
        'C:\dev\gitlab\csc372\Project1\Project1\Project1\Project1 C:\dev\gitlab\csc372\Project1\Project1\Project1\TestFiles\D-twoStage.txt')

    print('\nTest File E:')
    print('==============================================================')
    os.system(
        'C:\dev\gitlab\csc372\Project1\Project1\Project1\Project1 C:\dev\gitlab\csc372\Project1\Project1\Project1\TestFiles\E-threeStage.txt')

    print('\nTest File F:')
    print('==============================================================')
    os.system(
        'C:\dev\gitlab\csc372\Project1\Project1\Project1\Project1 C:\dev\gitlab\csc372\Project1\Project1\Project1\TestFiles\F-twoLine.txt')

    print('\nTest File G:')
    print('==============================================================')
    os.system(
        'C:\dev\gitlab\csc372\Project1\Project1\Project1\Project1 C:\dev\gitlab\csc372\Project1\Project1\Project1\TestFiles\G-noTransfer.txt')

    print('\nTest File H:')
    print('==============================================================')
    os.system(
        'C:\dev\gitlab\csc372\Project1\Project1\Project1\Project1 C:\dev\gitlab\csc372\Project1\Project1\Project1\TestFiles\H-noTravel.txt')

    print('\nTest File I:')
    print('==============================================================')
    os.system(
        'C:\dev\gitlab\csc372\Project1\Project1\Project1\Project1 C:\dev\gitlab\csc372\Project1\Project1\Project1\TestFiles\I-large.txt')


def makeTestFile(stages: int, routes: int):
    new_file = open('NewTestFile.txt', 'w')
    new_file.write(str(routes) + ' ' + str(stages) + '\n')
    for i in range(0, routes):
        for j in range(0, stages):
            new_file.write(str(random.randrange(100)) + ' ')
        new_file.write('\n')

    for i in range(0, stages):
        for j in range(0, routes):
            for k in range(0, routes):
                new_file.write(str(random.randrange(50)) + ' ')
            new_file.write('\n')


def runRandGenTestCases(numTestCases: int, maxStages: int = 20, maxRoutes: int = 20):
    runTimes = []
    i = 0
    while i < numTestCases:
        for j in range(1, maxStages):
            for k in range(1, maxRoutes):
                makeTestFile(j, k)
                start = time.time()
                os.system('C:\dev\gitlab\csc372\Project1\Project1\Project1\Project1 NewTestFile.txt -t')
                end = time.time()
                diff = end-start
                runTimes.append(diff)
                print('Test ' + str(i + 1) + ': ' + '\nSize: ' + str(j) + 'x' + str(k))
                print('Time Taken: ' + '%.4f seconds\n' % diff)
        i += 1

    return runTimes

def testingIncStages(numTestCases, routes, maxStages = 20):
    runTimes = []
    for i in range(1, maxStages + 1):
        testTimes = []
        for j in range(0, numTestCases):
            makeTestFile(i, routes)
            start = time.time()
            os.system('C:\dev\gitlab\csc372\Project1\Project1\Project1\Project1 NewTestFile.txt -t')
            end = time.time()
            diff = end - start
            testTimes.append(diff)
        runTimes.append(stats.mean(testTimes))

        print('ran ' + str(numTestCases) + ' Test cases at ' + str(i) + 'x' + str(routes))

    return runTimes

def testingIncRoutes(numTestCases, stages, maxRoutes = 20):
    runTimes = []
    for i in range(1, maxRoutes + 1):
        testTimes = []
        for j in range(0, numTestCases):
            makeTestFile(stages, i)
            start = time.time()
            os.system('C:\dev\gitlab\csc372\Project1\Project1\Project1\Project1 NewTestFile.txt -t')
            end = time.time()
            diff = end - start
            testTimes.append(diff)
        runTimes.append(stats.mean(testTimes))
        print('ran ' + str(numTestCases) + ' Test cases at ' + str(stages) + 'x' + str(i))

    return runTimes

def testingIncBoth(numTestCases, maxBoth):
    runTimes = []
    for i in range(1, maxBoth + 1):
        testTimes = []
        for j in range(0, numTestCases):
            makeTestFile(i, i)
            start = time.time()
            os.system('C:\dev\gitlab\csc372\Project1\Project1\Project1\Project1 NewTestFile.txt -t')
            end = time.time()
            diff = end - start
            testTimes.append(diff)
        runTimes.append(stats.mean(testTimes))
        print('ran ' + str(numTestCases) + ' Test cases at ' + str(i) + 'x' + str(i))

    return runTimes

