#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


data=pd.read_csv('data.csv')


# In[4]:


data


# In[5]:


data.columns = ['id', 'name', 'artists', 'duration_ms', 'release_date', 'year',
       'acousticness', 'danceability', 'energy', 'instrumentalness',
       'liveness', 'loudness', 'speechiness', 'tempo', 'positivity', 'mode',
       'key', 'popularity', 'explicit']
data.columns


# In[6]:


artist_one_name = "Lata Mangeshkar"
artist_two_name = "Red Velvet"
# 'acousticness', 'danceability', 'energy', 'instrumentalness',
# 'liveness', 'loudness', 'speechiness', 'tempo', 'positivity', 'mode',
# 'key', 'popularity', 'explicit'
measure_x = "energy"
measure_y = "danceability"


# In[7]:


artist_one = data[data['artists'].astype(str).str.contains(artist_one_name)]
artist_two = data[data['artists'].astype(str).str.contains(artist_two_name)]
print("Artist one:",len(artist_one))
print("Artist two:",len(artist_two))

if len(artist_one) == 0 or len(artist_two) == 0:
    print("ERROR: One of the artists isn't available")


# In[8]:


artist_one_x = artist_one[measure_x]
artist_two_x = artist_two[measure_x]
artist_one_y = artist_one[measure_y]
artist_two_y = artist_two[measure_y]


# In[9]:


import matplotlib.pyplot as plt


# In[13]:


plt.scatter(artist_one_x, artist_one_y, marker="o", label=artist_one_name)
plt.scatter(artist_two_x, artist_two_y, marker="^", label=artist_two_name)
plt.ylabel(measure_y)
plt.xlabel(measure_x)
plt.legend()


# In[13]:


sns.histplot(data['popularity'],kde=True)


# In[ ]:




