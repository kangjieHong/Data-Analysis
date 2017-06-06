# -*- coding: UTF-8 -*-
import numpy as np

# build a dimension array
# different with list

ls1 = range(10)
a = list(ls1)
print a
print type(a)
#range 单纯的列表

#numpy

ls2 = np.arange(10)
b = list(ls2)
print ls2
print b
print type(ls2)
#numpy.ndarray  一维数组

arr1 = np.array((1,2,3,4,10,12))
print arr1
print type(arr1)
#numpy.ndarray
#由元组序列组成的一维数组

arr2 = np.array([1,2,3,4,5,6])
print arr2
print type(arr2)
#numpy.ndarray
#由列表序列组成的一维数组

#二维数组的创建/-> 列表套列表/元组套元组

arr3 = np.array(((1,1,2,3),(5,8,13,21),(34,55,89,144)))
print arr3
print arr3[2][3] #144

arr4 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print arr4[2][3] #12

#special
print np.ones(3) #return 1*3 所有元素为1
print np.ones([3,4]) #return 3*4 all numbers are 1
np.zeros(3)
print np.zeros([3,4])
np.empty([3,4]) # 空数组

#.shape return the rows/cols
print arr3.shape
#.dtype return the class of array
print arr3.dtype
#.ravel()  is a function 把数组拉直/多维数组将为一维数组
print arr3
a = arr3.ravel()
print a

#another way flatten 把数组拉直
b = arr3.flatten()
print b

# 两者区别 ravel() / flatten()
# ravel方法生成的是原数组的视图，无需占有内存空间，
# 但视图的改变会影响到原数组的变化。
# 而flatten方法返回的是真实值，其值的改变并不会影响原数组的更改。

#example:while change b to watch wether the arr3 is changed or not?
b[:3] = 0
print arr3

#example:while change a to watch wether the arr3 is changed or not?
a[:3] = 0
print arr3   #[[  0   0   0   3]
            #  [  5   8  13  21]
            #  [ 34  55  89 144]]

print arr3.ndim  # 二维数组
t = np.ones([3,4,5])
print t.ndim    # 三维数组