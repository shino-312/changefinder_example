#!/usr/bin/env python

import itertools
import datetime
import sys
from changefinder_tester import ChangeFinderTester

def showHelp():
    print('============================================')
    print('This script reads data from .dat and finds a change point with ChangeFinder.')
    print('Before running this script, you need to create data with data_creator.py.')
    print('')
    print('Many combinations of parameters will be tested. See variables: r_list etc.')
    print('Final result will be PNG files.')
    print('============================================')
    print('Argument:')
    print(' 1st arg: File name of data')
    print('========================================================================')
    print('Example:')
    print('./main.py hoge.dat')
    print('========================================================================')


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        showHelp()
        sys.exit(1)

    data_file = args[1]

    data = []
    with open(data_file, 'r') as f:
        data = [float(d) for d in f.readlines()]
        print('Data %s loaded.' % data_file)

    tester = ChangeFinderTester(data_file)

    # Paramter combinations
    r_list = [0.0008, 0.001, 0.01, 0.1, 0.3]
    order_list = [1, 3, 5]
    smooth_list = [3, 5]

    param_combination = list(itertools.product(r_list, order_list, smooth_list))
    param_len = len(param_combination)

    for i, (r, o, s) in enumerate(param_combination):
        print('[%d/%d] r:%f, order:%d, smooth:%d' % (i, param_len, r, o, s))
        tester.execute(data, r, o, s)

    print('Done')
