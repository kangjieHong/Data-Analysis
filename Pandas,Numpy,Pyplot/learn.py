# -*- coding: UTF-8 -*-

import numpy as np
import sys
from datetime import datetime

"""
    numpy加法的便捷性ComputerSearch
"""
def numpysum(n):
    a = np.arange(n)**2
    b = np.arange(n)**3
    c = a + b

    return c

def pythonsum(n):
    a = range(n)
    b = range(n)
    c = []

    for i in range(len(a)):
        a[i] = i**2
        b[i] = i**3
        c.append(a[i]+b[i])

    return c
def test(n):
    start = datetime.now()
    c = pythonsum(n)
    delta = datetime.now() - start
    print "The last 2 elements of the sum",c[-2:]
    print "PythonSum elapsed time in mircoseconds ",delta.microseconds
    start = datetime.now()
    c = numpysum(n)
    delta = datetime.now() - start
    print "The last 2 elements of the sum",c[-2:]
    print "NumpySum elapsed time in mircoseconds ", delta.microseconds
    print '\n'

test(1000)
test(2000)
test(3000)

print np.arange(5)   #array
print range(5)   #list
print '\n'
a = np.array([[0,1,2,3,4],[2,3,4,5,6]])   #numpy must be alignment
print a
print a.shape  #output: (2,5) one dimension is 2, one dimension is 5
print a[1][3]

b = np.arange(24).reshape(2,3,4)
print b
print b[:,1]

"""
 reavel() & flatten() different
"""
q = b.ravel()   #ravel() is  a view of numpy
q[0] = 100
print b[0,0,0]    #change q is to change b
print q

q = b.flatten()  #flatten() ids a new memory
q[0] =88
print b[0,0,0]    #change q is not to change b
print q

