#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
data = pd.read_csv('./wp.csv')


# In[12]:


time= data['time']
temp = data['temperatureMax']
uvindex = data["uvIndex"]
humidity = data['humidity']


# In[14]:


plt.scatter(time,temp,color='green', alpha=0.4)
plt.ylabel('temperatureMax', fontsize = 15)
plt.xlabel('time', fontsize = 15)


# In[15]:


plt.plot(time,temp,color='green', alpha=0.6)
plt.ylabel('temperatureMax', fontsize = 15)
plt.xlabel('time', fontsize = 15)


# In[16]:


plt.plot(temp,uvindex, color='green', alpha=0.8)
plt.ylabel('uvindex', fontsize = 15)
plt.xlabel('temperatureMax', fontsize = 15)


# In[17]:


plt.scatter(temp,uvindex)
plt.ylabel('uvindex', fontsize = 15)
plt.xlabel('temperatureMax', fontsize = 15)


# In[18]:


plt.plot(temp,humidity, color='red', alpha=0.8)
plt.ylabel('humidity', fontsize = 15)
plt.xlabel('temperatureMax', fontsize = 15)


# In[21]:


plt.plot(time,uvindex, color='pink')
plt.ylabel('uvindex', fontsize = 15)
plt.xlabel('temperatureMax', fontsize = 15)


# In[ ]:




