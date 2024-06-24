#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd
import scipy.stats as stats
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols

import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/yasin/Desktop/Ülkeler/countries.csv")
df['usdprice'].fillna(df['usdprice'].mean(), inplace=True)

df['averageTemperature'] = pd.to_numeric(df['averageTemperature'], errors='coerce').fillna(-1)

df['averageTemperature'] = pd.cut(df['averageTemperature'],
                                    bins=[float('-inf'), 10, 25, float('inf')],
                                    labels=['cold', 'normal', 'hot'],
                                    right=False)
rp.summary_cont(df['usdprice'])


# In[41]:


rp.summary_cont(df['usdprice'].groupby(df['averageTemperature']))


# In[42]:


stats.f_oneway(df['usdprice'][df['averageTemperature']=='cold'],
               df['usdprice'][df['averageTemperature']=='normal'],
               df['usdprice'][df['averageTemperature']=='hot'])


# In[43]:


results= ols('usdprice ~ C(averageTemperature)',data=df).fit()
aov_table=sm.stats.anova_lm(results, typ=2)
aov_table

