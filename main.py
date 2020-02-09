#!/usr/bin/env python

import matplotlib.pyplot as plt
import changefinder
import datetime
import sys

import data_util as du

def showHelp():
    print('============================================')
    print('*** HOW TO USE ***')
    print('')
    print('3 paramters are required at least.')
    print(' - 1st: discount rate of SDAR model(float)')
    print(' - 2nd: order of SDAR model(int)')
    print(' - 3rd: smoothing window size(int)')
    print('')
    print('Data file can be specified as 4th argument(optional).')
    print('============================================')
    print('*** EXAMPLE ***')
    print('./main 0.01 1 3')
    print('./main 0.35 2 7 input_data.dat')
    print('============================================')

def getNormalized(lst):
    min_value = min(lst)
    max_value = max(lst)
    return [(x - min_value) / (max_value - min_value) for x in lst]

if __name__ == '__main__':
    time_string = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    data = []
    dis_r = 0.1
    arma_order = 1
    smooth_size = 3

    # Get command-line arguments
    args = sys.argv
    argnum = len(sys.argv)
    if not (argnum == 4 or argnum == 5):
        print('Wrong arguments are specified!')
        showHelp()
        sys.exit(1)

    dis_r = float(args[1])
    arma_order = int(args[2])
    smooth_size = int(args[3])

    if argnum == 4:
        print('Create new data')
        data_phase1 = du.addWhiteNoise(du.makeUniformData(100, 0.0), 0, 1.0)
        data_phase2 = du.addWhiteNoise(du.makeSlopeData(5, 1.0, 0.0), 0, 1.0)
        data_phase3 = du.addWhiteNoise(du.makeUniformData(100, 5.0), 0, 1.0)
        data = data_phase1 + data_phase2 + data_phase3
        file_name = '%s.dat' % time_string
        with open(file_name, 'w') as f:
            f.write('\n'.join([str(d) for d in data]))
            print('Saved %s' % file_name)

    elif argnum == 5:
        print('Read data from external files')
        file_name = args[4]
        with open(file_name, 'r') as f:
            data = [float(d) for d in f.readlines()]

    # Apply changefinder
    cf = changefinder.ChangeFinder(
            r=dis_r, order=arma_order, smooth=smooth_size)

    score = [cf.update(d) for d in data]

    # Plot results
    plt.title('ChangeFinder r=%f, order=%d, smooth=%d'
            % (dis_r, arma_order, smooth_size))

    plt.plot(data, label='Data', color='blue')
    plt.plot(score, label='Anomaly Score', color='red')

    plt.savefig('results_%s.png' % time_string)

    print('Done')
