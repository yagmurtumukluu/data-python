#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install numpy')
get_ipython().system('pip install seaborn')


# In[4]:


import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt


# In[46]:


plt.style.use("seaborn-whitegrid")


df = pd.read_csv("/home/yagmurtumuklu/Downloads/autos.csv")

df.head()


# In[47]:



X = df.copy()
y = X.pop("price")

# Label encoding for categoricals
for colname in X.select_dtypes("object"):
    X[colname], _ = X[colname].factorize()
#.factories numerice cevirmek icin


# All discrete features should now have integer dtypes (double-check this before using MI!)
discrete_features = X.dtypes == int
X.dtypes


# In[ ]:


#!!!!!!!!!!!!!!! SORRRRRRRRRR!!!!!!!!!!!!!!!!!!!


# In[48]:


from sklearn.feature_selection import mutual_info_regression

def make_mi_scores(X, y, discrete_features):
    mi_scores = mutual_info_regression(X, y, discrete_features=discrete_features)
    mi_scores = pd.Series(mi_scores, name="MI Scores", index=X.columns)
    mi_scores = mi_scores.sort_values(ascending=False)
    return mi_scores

mi_scores = make_mi_scores(X, y, discrete_features)
mi_scores[::3]  # show a few features with their MI scores


# In[ ]:


#CIZIM

def plot_mi_scores(scores):
    
    scores = scores.sort_values(ascending=True)
    
    width = np.arange(len(scores))
    
    ticks = list(scores.index)
    
    plt.barh(width, scores)
    plt.yticks(width, ticks)
    plt.title("Mutual Information Scores")
    
    
    
plt.figure(dpi=100, figsize=(8, 5))
plot_mi_scores(mi_scores)

