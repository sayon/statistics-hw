from math import sin, exp, pow
from random import uniform 

def myf(x):
    return sin(x + exp(-x))
def myf2(x):
    return (1.0 / sin(x)** (1/3.0)) ** 2

def montecarlo(left, right, f, amount):
    acc = 0.0
    for i in xrange(0, amount):
        acc = acc + f(uniform(left, right))    
    return acc/amount


print "First task: montecarlo for integral from 0 to 1 of f(x) = sin(x + exp(-x)):" , montecarlo(0.0, 1.0, myf, 100000) 
print "Third task: montecarlo for integral from 0 to 1 of f(x) = sin(x)^(-2/3):" , montecarlo(0.0, 1.0, myf2, 10000000) 
