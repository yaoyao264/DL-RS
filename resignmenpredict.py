# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:54:39 2020

@author: ally6
"""

import pandas as pd
hr = pd.read_csv('F://ZOOM/人工智能/推荐系统与机器学习课件/推荐系统与机器学习作业/第一课/rs6-attrition-predict/train.csv')
col_names = hr.columns.tolist()
print("Column names:")
print(col_names)
print("nSample data:")
hr.head()

hr.dtypes
hr.isnull().any()
hr.shape
hr['Department'].unique()
hr['Attrition'].value_counts()
hr.groupby('Attrition').mean()
hr.groupby('Department').mean()
hr.groupby('MonthlyIncome').mean()

#matplotlib inline
import matplotlib.pyplot as plt
pd.crosstab(hr.Department,hr.Attrition).plot(kind='bar')
plt.title('Turnover Frequency for Department')
plt.xlabel('Department')
plt.ylabel('Frequency of Turnover')
plt.savefig('department_bar_chart')

table=pd.crosstab(hr.MonthlyIncome, hr.Attrition)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Salary Level vs Turnover')
plt.xlabel('Salary Level')
plt.ylabel('Proportion of Employees')
plt.savefig('salary_bar_chart')

num_bins = 10
hr.hist(bins=num_bins, figsize=(20,15))
plt.savefig("hr_histogram_plots")
plt.show()

cat_vars=['Department','MonthlyIncome']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(hr[var], prefix=var)
    hr1=hr.join(cat_list)
hr=hr1

hr.drop(hr.columns[[5, 19]], axis=1, inplace=True)
hr.columns.values

hr_vars=hr.columns.values.tolist()
y=['Attrition']
X=[i for i in hr_vars if i not in y]

feature_labels = np.array(['satisfaction_level', 'last_evaluation', 'time_spend_company', 'Work_accident', 'promotion_last_5years', 'department_RandD', 'department_hr', 'department_management', 'salary_high', 'salary_low'])
importance = rf.feature_importances_
feature_indexes_by_importance = importance.argsort()
for index in feature_indexes_by_importance:
    print('{}-{:.2f}%'.format(feature_labels[index], (importance[index] *100.0)))