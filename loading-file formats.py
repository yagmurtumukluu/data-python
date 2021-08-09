#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip3 install pandas')


# In[3]:


get_ipython().system('which python')


# In[4]:


import pandas  as pd


# In[5]:


#FILE OKUMA


# In[6]:


get_ipython().system('pwd examples/diamonds.txt.csv')


# In[7]:


df = pd.read_csv('/home/yagmurtumuklu/Downloads/diamonds.txt')
df


# In[8]:


pandas.read_csv('/home/yagmurtumuklu/Downloads/diamonds.txt', header=None )


# In[9]:


pd.read_csv('/home/yagmurtumuklu/Downloads/diamonds.txt', 
                header = 0, #bak buna
                names = ['sütun1', 'sütun2', 'sütun3', 'sütun4', 'sütun5'])


# In[10]:


names = ['sütun1', 'sütun2', 'sütun3', 'sütun4', 'sütun5']
pd.read_csv('/home/yagmurtumuklu/Downloads/diamonds.txt', names = names)


# In[11]:


#alanlari ayirmak-bosluk birakmak

list(open('/home/yagmurtumuklu/Downloads/diamonds.txt'))


# In[12]:


result = pd.read_csv('/home/yagmurtumuklu/Downloads/diamonds.txt' , sep ='\s,')

result


# In[ ]:





# In[ ]:




