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

b = np.ndarray(shape=(3,2),dtype=int,buffer=np.array([1,2,3,4,5,6]))
b2 = np.eye(4,k=2)   #k means 对角线移动方向以及数量
b3 = np.identity(4)  # identity matrix
print b2
print b3



print np.linspace(0,7,10) # linspace函数通过指定初始值、终值以及元素个数来创建一维数组

s1 = "1,23,4,56,7"    # from string get the numpy
print np.fromstring(string=s1,dtype=np.float64,sep=',')

"""
fromfunction函数由第一个参数作为计算每个数组元素的函数（函数对象或者lambda表达式均可），第二个参数为数组的形状
"""
def func(x,y):
    return (x+1)*(y+1)

print np.fromfunction(func,(7,7))

print np.fromfunction(lambda i,j:i+j,(3,3),dtype=np.int64)  # use lambda function

print '\n'

"""
different use with  ndarray matrix 
like : 
diag函数返回一个矩阵的对角线元素、或者创建一个对角阵，对角线由参数k控制

diagflat函数以输入作为对角线元素，创建一个矩阵，对角线由参数k控制

tri函数生成一个矩阵，在某对角线以下元素全为1，其余全为0，对角线由参数k控制

tril函数输入一个矩阵，返回该矩阵的下三角矩阵，下三角的边界对角线由参数k控制

triu函数与tril类似，返回的是矩阵的上三角矩阵

vander函数输入一个一维数组，返回一个范德蒙德矩阵
"""

matrix = np.arange(1,17).reshape(4,4)
print matrix
print np.diag(matrix,k=1)  # diag 对角线元素组成的array  with the k change
print np.diag(np.diag(matrix),k=0)  # build diag matrix

print np.diagflat([1,2,3],k=-1)

print np.tri(3,3,k=0)

print np.tril(matrix,k=-1)   #low matrix

print np.vander([2,4,3,5],N=4)

for item in matrix.flat:
    print item