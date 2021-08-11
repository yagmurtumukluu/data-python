#!/usr/bin/env python
# coding: utf-8

# In[ ]:


feature engineering-example


# In[ ]:


#predict a concrete's compressive strength given its formulation
#(basinc dayanimi test edilecek) 


# In[1]:


get_ipython().system('pip install pandas')
import pandas as pd


# In[3]:


get_ipython().system('pip install sklearn')
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score


# In[31]:


df = pd.read_csv('/home/yagmurtumuklu/Downloads/Concrete_Data.csv')
df.head()


# In[ ]:


#önce, modeli artırılmamış data üzerinde eğiterek bir temel oluştur
#yeni özelliklerin işe yarayıp yaramadıüını görmek için
#feature engineering process.


# In[ ]:


X = df.copy()
y = X.pop("CompressiveStrength")

# modeli train ve puanla

baseline = RandomForestRegressor(criterion="mae", random_state=0)

baseline_score = cross_val_score(baseline, X, y, cv=5, scoring="neg_mean_absolute_error")

baseline_score = -1 * baseline_score.mean()

print(f"MAE Baseline Score: {baseline_score:.4}")


# In[ ]:


# asagidaki cell ile datasete 3 yeni feature eklenecek


# In[ ]:


X = df.copy()
y = X.pop("CompressiveStrength")

# feature ekleme

X["FCRatio"] = X["FineAggregate"] / X["CoarseAggregate"]
X["AggCmtRatio"] = (X["CoarseAggregate"] + X["FineAggregate"]) / X["Cement"]
X["WtrCmtRatio"] = X["Water"] / X["Cement"]

# yeni eklenmis ozelliklerle train and puanla

model = RandomFprestRegressor(crtiterion ="mae", random_satte =0)
scroe = cross_val_score (model, X, y, cv=5, scoring="neg_mean_absolute_error")

score = -1*score.mean()

print(f"MAE Score with Ratio Features: {score:.4})
      


# In[ ]:




