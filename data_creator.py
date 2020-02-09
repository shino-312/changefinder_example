#!/usr/bin/env python
import sys
import random

def makeUniformData(length, value):
    return [value]*length

def makeSlopeData(length, slope, start_value):
    return [slope*float(i) + start_value for i in range(length)]

def addWhiteNoise(target, mean, sigma):
    return [t + random.gauss(mean, sigma) for t in target]

def showHelp():
    print('========================================================================')
    print('This script creates new data and saves to a file.')
    print('If you want to change data characteristics, edit this script directly.')
    print('========================================================================')
    print('Argument:')
    print(' 1st arg: File name for output')
    print('========================================================================')
    print('Example:')
    print('./data_creator hoge.dat')
    print('========================================================================')

if __name__ == '__main__':

    args = sys.argv
    if len(args) == 2:
        sigma = 1.0
        data_phase1 = addWhiteNoise(makeUniformData(100, 0.0), 0, sigma)
        data_phase2 = addWhiteNoise(makeSlopeData(30, 0.3, 0.0), 0, sigma)
        data_phase3 = addWhiteNoise(makeUniformData(100, 9.0), 0, sigma)
        data = data_phase1 + data_phase2 + data_phase3

        file_name = args[1]
        with open(file_name, 'w') as f:
            f.write('\n'.join([str(d) for d in data]))
            print('Saved %s' % file_name)

    else:
        print('Wrong argument is specified.')
        showHelp()
        sys.exit(1)

