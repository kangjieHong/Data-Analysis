# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd

# pandas中最重要的数据结构是 Series & DataFrame 序列和数据框

arr1 = np.array([5,10,2,4,7])
print arr1
print type(arr1)

#通过一维数组创建序列
s1 = pd.Series(arr1)
print s1
print type(s1)

dic1 = {'a':10,'b':20,'c':30,'d':40,'e':50}
print dic1
print type(dic1)

#通过字典创建序列
s2 = pd.Series(dic1)
print s2
print type(s2)

#DataFrame的创建
# first way
arr2 = np.array(np.arange(12).reshape(4,3))
print arr2
print type(arr2)

#通过二维数组创建数据框
df1 = pd.DataFrame(arr2)
print df1
print type(df1)