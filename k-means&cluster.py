#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


# In[31]:


plt.style.use("seaborn-whitegrid")
plt.rc("figure", autolayout=True)
plt.rc("axes", 
       
      labelweight="bold", 
      labelsize="large",
      titleweight="bold",
      titlesize=14,
      titlepad=10,)

df=pd.read_csv("/home/yagmurtumuklu/Desktop/aaaaa/housing.csv")
X=df [ [ "latitude" , "longitude" ]]
X.head()


# In[43]:


#cluster feature oluşturma

kmeans = KMeans(n_clusters=10)
X["Cluster"] = kmeans.fit_predict(X)
X["Cluster"] = X["Cluster"].astype("category")

X.head


# In[44]:


sns.relplot(x="longitude", y="latitude", hue="Cluster", data=X, height=6,);


# In[ ]:





# In[ ]:




