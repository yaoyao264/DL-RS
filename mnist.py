# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:47:30 2020

@author: ally6
"""
import tensorflow as tf
import numpy as np 
from sklearn import tree
from sklearn.model_selection import train_test_split #进行训练集数据集划分
from sklearn.tree import DecisionTreeClassifier

data=np.load('F:\ZOOM\人工智能\推荐系统与机器学习课件\推荐系统与机器学习作业\第一课\mnist.npz') 

train_x, train_y, test_x, test_y  = data['x_train'], data['y_train'], data['x_test'], data['y_test']


train_x = train_x.reshape(train_x.shape[0], 28, 28, 1)
test_x = test_x.reshape(test_x.shape[0], 28, 28, 1)
train_x = train_x / 255
test_x = test_x / 255
train_y = tf.keras.utils.to_categorical(train_y, 10)
test_y = tf.keras.utils.to_categorical(test_y, 10)

train_x, train_y, test_x, test_y=train_test_split(train_x, train_y,test_size=0.3)

clf = tree.DecisionTreeClassifier()  #实例化，全部选择了默认的参数
clf.fit(train_x, train_y)               #拟合
score=clf.score(test_x, test_y)         #模型评分
print(score)
