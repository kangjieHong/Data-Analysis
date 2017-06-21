# -*- coding: UTF-8 -*-

import csv as csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.ensemble import BaggingRegressor
from sklearn.learning_curve import  learning_curve

csv_file_object = csv.reader(open("/home/perfecum/下载/bmw-browsers.csv",'rb'))
header = csv_file_object.next()
data = []

for row in csv_file_object :
    data.append(row)

data = np.array(data)

df = pd.read_csv('/home/perfecum/下载/bmw-browsers.csv',header=0)

print df.describe()

#plt.subplot2grid((2,3),(0,0))

fig = plt.figure()
fig.set(alpha=0.2)

purchase_0 = df.Dealership[df.Purchase == 0].value_counts()
purchase_1 = df.Dealership[df.Purchase == 1].value_counts()
img = pd.DataFrame({'not-purchase':purchase_0,'purchase':purchase_1})
img.plot(kind='bar',stacked=True)
plt.title('Dealership & purchase')
#plt.xlabel('Dealership')
plt.ylabel('number of Purchase')
#plt.show()

purchase_0 = df.Financing[df.Purchase == 0].value_counts()
purchase_1 = df.Financing[df.Purchase == 1].value_counts()
img = pd.DataFrame({'not-purchase':purchase_0,'purchase':purchase_1})
img.plot(kind='bar',stacked=True)
plt.title('Financing & purchase')
#plt.xlabel('Stay in Showroom')
plt.ylabel('number of Purchase')
plt.xlabel('Financing or not')

plt.show()

#print df[['Dealership','M5']].mean()
#df['M5'].hist(range=(0,1))
#p.show()
# data[:,[0,7]]
# data.T[[0,7]]  Dealership  / Purchase


#-----------modeling------

tran_df = df.filter(regex='Dealership|Showroom|ComputerSearch|M5|3Series|Z4|Financing|Purchase')
tran_np = tran_df.as_matrix()

#-----------output------
y = tran_np[:,7]

#-----------input------
x = tran_np[:,:7]

clf = linear_model.LogisticRegression(C=1.0,penalty='l1',tol=1e-6)

#-----------use bagging------
bagging_clf = BaggingRegressor(clf,n_estimators=20,max_features=1.0,max_samples=0.8,bootstrap=True, bootstrap_features=False, n_jobs=-1)
bagging_clf.fit(x,y)

print clf

#-----------testdata------
test = pd.read_csv('/home/perfecum/下载/test.csv',header=0)
test_df = test.filter(regex='Dealership|Showroom|ComputerSearch|M5|3Series|Z4|Financing')
print test_df
test_np = test_df.as_matrix()

predictions = bagging_clf.predict(test_df)

print predictions


#-----------something test------
train_sizes, train_scores, test_scores = learning_curve(
    clf, x, y, cv=10, n_jobs=1,train_sizes=np.linspace(.05, 1., 20), verbose=0)
train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)
ylim = None
if True:
        plt.figure()
        plt.title('Something')
        if ylim is not None:
            plt.ylim(*ylim)
        plt.xlabel(u"numbers of train")
        plt.ylabel(u"Score")
        plt.gca().invert_yaxis()
        plt.grid()

        plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std,
                         alpha=0.1, color="b")
        plt.fill_between(train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std,
                         alpha=0.1, color="r")
        plt.plot(train_sizes, train_scores_mean, 'o-', color="b", label="Trian set")
        plt.plot(train_sizes, test_scores_mean, 'o-', color="r", label="Verification set")

        plt.legend(loc="best")

        plt.draw()
        plt.show()
        plt.gca().invert_yaxis()

midpoint = ((train_scores_mean[-1] + train_scores_std[-1]) + (test_scores_mean[-1] - test_scores_std[-1])) / 2
diff = (train_scores_mean[-1] + train_scores_std[-1]) - (test_scores_mean[-1] - test_scores_std[-1])

