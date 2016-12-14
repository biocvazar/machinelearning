from __future__ import unicode_literals

__author__ = 'Bio'

import pandas
from pandas.io.parsers import read_csv
from pandas.tools.plotting import radviz
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVR
from sklearn import datasets, svm

print(SVR, KNeighborsRegressor, LogisticRegression)

data_set = read_csv("DataTypes.csv", ';', encoding='utf8')
del data_set['Номер']
# print(data_set)

test_data = read_csv('TestData.csv', ';', encoding='utf8')
del test_data['Номер']
# print(test_data)

materials = {'дерево': 2, 'метал': 3, 'пластик': 1}
colors = {'жовтий': 1, 'червоний': 2, 'зелений': 3, 'фіолетовий': 4, 'рожевий': 5}
knn = KNeighborsRegressor(n_neighbors=3)

knn.fit(data_set[['Діметр зразка, см', 'Колір зразка', 'Вага зразка, г', 'Товщина зразка, мм', 'Матеріал зразка']],
        data_set[['Тип зразка']])

print("Тип зразка за методом KNN: ",
      knn.predict(test_data[['Діметр зразка, см', 'Колір зразка', 'Вага зразка, г', 'Товщина зразка, мм',
                             'Матеріал зразка']]))
matplotlib.rc('font', family='Arial')
radviz(data_set, 'Тип зразка')
test_data['Тип зразка'] = knn.predict(test_data[['Діметр зразка, см', 'Колір зразка', 'Вага зразка, г',
                                                 'Товщина зразка, мм', 'Матеріал зразка']])
plt.title("Вхідні дані")
plt.show()
data_set = data_set.append(test_data)
radviz(data_set, 'Тип зразка')
plt.title("KNN (k=3)")
plt.show()

data_set_svc = read_csv("DataTypes.csv", ';', encoding='utf8')
del data_set_svc['Номер']

test_data_svc = read_csv('TestData.csv', ';', encoding='utf8')
del test_data_svc['Номер']


svc = svm.SVC()
svc.fit(data_set_svc[['Діметр зразка, см', 'Колір зразка', 'Вага зразка, г', 'Товщина зразка, мм', 'Матеріал зразка']],
        data_set_svc[['Тип зразка']])

test_data_svc['Тип зразка'] = svc.predict(
    test_data_svc[['Діметр зразка, см', 'Колір зразка', 'Вага зразка, г', 'Товщина зразка, мм',
                   'Матеріал зразка']])
data_set_svc = data_set_svc.append(test_data_svc)

print("Тип зразка за методом SVC: ", svc.predict(
    test_data_svc[['Діметр зразка, см', 'Колір зразка', 'Вага зразка, г', 'Товщина зразка, мм',
                   'Матеріал зразка']]))
radviz(data_set_svc, 'Тип зразка')
plt.title("SVC")
plt.show()