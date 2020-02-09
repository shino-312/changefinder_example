import random

def makeUniformData(length, value):
    return [value]*length

def makeSlopeData(length, slope, start_value):
    return [slope*float(i) + start_value for i in range(length)]

def addWhiteNoise(target, mean, sigma):
    return [t + random.gauss(mean, sigma) for t in target]

