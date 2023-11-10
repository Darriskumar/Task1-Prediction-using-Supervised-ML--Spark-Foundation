#!/usr/bin/env python
# coding: utf-8

# # Darris Femilia
# # Task1- Spark Foundation
# # Prediction using Supervised ML

# In[1]:


#import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  
from sklearn import metrics 


# In[2]:


#reading data in link

data = pd.read_csv("http://bit.ly/w-data")
print("Data imported successfully")
data.head()


# In[3]:


#statistics about the dataset
correlation=data.describe()
correlation


# In[4]:


#checking null values

data.isnull().sum()


# In[5]:


# Plotting the distribution of scores
data.plot(x='Hours', y='Scores', style='o')  
plt.title('Hours vs Percentage')  
plt.xlabel('Hours Studied')  
plt.ylabel('Percentage Score')  
plt.show()


# In[6]:


x =data.iloc[:,:-1]
y = data['Scores']


# In[7]:


#split dataset into train and test data

x_train, x_test, y_train, y_test = train_test_split(x, y, 
                            test_size=0.25, random_state=3) 


# In[8]:


#training 

regressor = LinearRegression()  
regressor.fit(x_train, y_train)


# In[9]:


# Predicting the scores for test values

y_predict= regressor.predict(x_test)


# In[10]:


# calculate r2_score 

from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_predict)
r2
     


# In[11]:


regressor.predict([[9.25]])

