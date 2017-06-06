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
print arr3.size #return number of array  12
print arr3.T # transform of arr3 转置

#如果数组的数据类型为复数的话，
# real方法可以返回复数的实部，imag方法返回复数的虚部。
print arr3.real

np.hstack((arr3,arr4))  #np.column_stack((arr3,arr4)) 效果一样
#横向拼接arr3和arr4两个数组，但必须满足两个数组的行数相同
np.vstack((arr3,arr4)) #np.row_stack((arr3,arr4)) 效果一样
#纵向拼接arr3和arr4两个数组，但必须满足两个数组的列数相同。

arr5 = np.array(np.arange(24))
print arr5
a = arr5.reshape(4,6)  #reshape()函数和resize()函数可以重新设置数组的行数和列数
print a  #rows 4; cols 6
a = arr5.reshape(2,3,4)
print a.ndim

#bool index
#布尔索引，即索引值为True和False，需要注意的是布尔索引必须输数组对象。
log = np.array([True,False,False,True,True,False])
logT = np.array([True,False,True,False])
arr9 = np.array(np.arange(24).reshape(6,4))
print arr9
print arr9[log]  #return index中为True的行
print arr9.T[logT] #return index中为True的列

print arr9[-log] #return index 中为False的行
print arr9.T[logT] #return index 中为False的列


#举一个场景，一维数组表示区域，二维数组表示观测值，
# 如何选取目标区域的观测？
print '\n'
area = np.array(['A','B','A','C','A','B','D'])
observes = np.array(np.arange(21).reshape(7,3))
print observes[area=='A']
print '\n'
print observes[(area == 'A')|(area == 'D')]
#返回所有A区域和D区域的观测。
print '\n'
print observes[area == 'A'][:,[0,2]]
#返回A区域的所有行，且只获取第1列与第3列数据。


arr10 = np.arange(1,29).reshape(7,4)
print arr10[[4,1,3,5]]  #按照指定顺序返回指定行!!!!

arr10[[4,1,5]][:,[0,2,3]] #返回指定的行与列
#is like a function ix_()
arr10[np.ix_([4,1,5],[0,2,3])] #简单方法返回指定行列的二维数组


print arr10[[4,1,5],[0,2,3]]#这与上面的返回结果是截然不同的，
                    # 上面返回的是二维数组，而这条命令返回的是一维数组。
#array([17,  7, 24]) 相当于 返回[4,0],[1,2],[5,3]
print arr10[4,0]
