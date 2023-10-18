#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


#Loading the dataset
data = pd.read_csv("C:\\Users\\AbiramiSV\\Downloads\\Dataset\\PublicTransportDataset.CSV", low_memory=False)


# In[4]:


#Displaying the first 20 rows
data.head(20)


# In[5]:


# Dropping records which have duplicate values
data.drop_duplicates(inplace=True)


# In[6]:


# Filling missing values with mean
data.fillna(data.mean(), inplace=True)


# In[7]:


# Printing the first few rows
print(data.head())


# In[8]:


# Generating descriptive statistics of the dataset
print(data.describe())


# In[9]:


# Generating concise summary of the dataset
print(data.info())


# In[11]:


# Shape of the dataset
print(data.shape)


# In[12]:


# Displaying first few rows after preprocessing
data.head()


# In[ ]:




