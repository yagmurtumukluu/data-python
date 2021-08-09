#!/usr/bin/env python
# coding: utf-8

# In[42]:


get_ipython().system('pip install numpy')
get_ipython().system('pip install pandas')
get_ipython().system('pip install scipy')
get_ipython().system('pip install matplotlib')
get_ipython().system('pip install requests')
get_ipython().system('pip install seaborn')


# In[6]:


import requests
import os


# In[8]:


r = requests.get("https://github.com/adambard/learnxinyminutes-docs")
r.status_code
r.text

os.getcwd()

with open ("learnxinyminutes.html", "wb) as f:
           f.write(r.text.encode("UTF-8"))


# In[10]:


fpets = "https://raw.githubusercontent.com/adambard/learnxinyminutes-docs/master/"
fn = "pets.csv"
r = requests.get(fpets + fn)
print(r.text)
with open(fn, "wb") as f:
    f.write(r.text.encode("UTF-8"))


# In[ ]:


# READING CSV FILE


# In[15]:


import pandas as pd
import numpy as np
import scipy as sp

pets= pd.read_csv(fn)

pets


# In[24]:


#ISTENEN INDEXE ERISME


# In[16]:


pets.age[0:2]


# In[17]:


pets.name[0]


# In[19]:


pets["weight"][0]


# In[25]:


#


# In[22]:


sum(pets.age)


# In[23]:


sum(pets.weight)*8+6


# In[ ]:


#MATPLOTLIB


# In[27]:


import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[39]:


plt.hist(pets.age);


plt.scatter(pets.age, pets.weight)

plt.xlabel("age")
plt.ylabel("weight")


# In[43]:


import seaborn as sns


# In[44]:


plt.scatter(pets.age, pets.weight)  #scatter plot; farkli deger compare edilirken
plt.xlabel("age")
plt.ylabel("weight")


# In[ ]:


#DATA CLEANING


# In[46]:


url = "https://raw.githubusercontent.com/adambard/learnxinyminutes-docs/master/hre.csv"


# In[47]:


#bi example daha at


# In[53]:


r = requests.get(url)
fp = "hre.csv"
with open(fp, "wb") as f:
    f.write(r.text.encode("UTF-8"))

hre = pd.read_csv(fp)

hre.head()


# In[ ]:


#clean bırth columns


# In[54]:


from functools import reduce #tekrar bak!!!!


# In[64]:


def extract_yil(v):
    return(pd.Series(reduce(lambda x, y: x + y, map(,v), [])).astype(int))


#.astype: data tipin istediğin tipte değilse dönüşüm yapar
#(sayısal değerler string, string değerler de sayısal değer gibi)


# In[65]:


hre["BirthY"] = extract_yil(hre.Birth)
hre["DeathY"] = extract_yil(hre.Death)


# In[ ]:




