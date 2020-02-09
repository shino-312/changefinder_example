#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import changefinder

class ChangeFinderTester():
    def __init__(self, tag):
        # tag is just a name(string) to distinguish test kinds
        self.tag = tag

    def execute(self, data, r, order, smooth):
        cf = changefinder.ChangeFinder(r, order, smooth)
        score = self.getNormalized([cf.update(d) for d in data])

        self.plot_result(data, r, order, smooth, score)

    def plot_result(self, data, r, order, smooth, score):
        change_point_index = np.array(score).argmax()

        plt.title('tag:%s, r:%f, order:%d, smooth:%d, cp:%d'
                % (self.tag, r, order, smooth, change_point_index))

        plt.plot(data, label='Data', color='blue')
        plt.plot(score, label='Anomaly Score', color='red')
        plt.vlines(np.array(score).argmax(), min(data), max(data), linestyle='dashed')
        plt.savefig('out_%s_%f_%d_%d.png' % (self.tag, r, order, smooth))
        plt.clf()  # Clear(reset) canvas

    def getNormalized(self, lst):
        min_value = min(lst)
        max_value = max(lst)
        return [(x - min_value) / (max_value - min_value) for x in lst]
