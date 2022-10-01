# -*- coding: utf-8 -*-
"""Assignment2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yG1JjTuCZEqDXkVSIIorWp4VY36txXD7

1.Download The Dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

"""2.Load The Dataset"""

# load a data set
data = pd.read_csv('/content/50_Startups.csv')

data.head()

"""3. Perform below visualizations"""

#univariate analysis
sns.distplot(data['Marketing Spend'])

#bivariate analysis
sns.lineplot(data['Profit'], data['R&D Spend'])

#multivariate analyais
sns.scatterplot(data['R&D Spend'], data['Profit'], hue=data['State'])

"""4.Perform descriptive statistics on the dataset"""

data.mean()

data.median()

data.mode()

"""5.Handle the missing values"""

data.isnull().any()

data.isnull().sum()

"""6.Find the outliers and replace the outliers"""

data.quantile([0.1])

data.quantile([0.1,0.5])

data.quantile([0.1,0.9])

"""7.Check for categorical columns and perform encoding"""

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

oneh = preprocessing.OneHotEncoder()

data['R&D Spend'] = le.fit_transform(data['R&D Spend'])

data.head()

"""8.split the data into dependent and independent variables (x and y)"""

x=data.iloc[:,0:12]

x

y = data['Profit']

y

"""9.scale the independent variables"""

x = data.iloc[:,0:1]

from sklearn.preprocessing import StandardScaler, MinMaxScaler
sc = StandardScaler()
x_scaled = sc.fit_transform(x)

x_scaled

"""10.Split the data into train and test"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size = 0.3, random_state = 0)
x_train

x_train.shape

y_train

