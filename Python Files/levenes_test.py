#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from scipy import stats

df = pd.read_csv("C:/Users/yasin/Desktop/Ülkeler/countries.csv")

df.plot.scatter("averageTemperature","usdprice")


# In[5]:


import numpy as np

df['averageTemperature'].fillna(df['averageTemperature'].mean(), inplace=True)
df['usdprice'].fillna(df['usdprice'].mean(), inplace=True)

result=stats.levene(df['averageTemperature'], df['usdprice'])
print(result)


# In[6]:


df['averageTemperature'].corr(df['usdprice'])


# In[7]:


df['averageTemperature'].corr(df['usdprice'], method='spearman')


# In[8]:


stats.pearsonr(df['usdprice'],df['averageTemperature'])


# In[9]:


stats.spearmanr(df['usdprice'],df['averageTemperature'])


# In[10]:


stats.kendalltau(df['usdprice'],df['averageTemperature'])






