#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from tqdm import trange


# In[2]:


base_url = "https://search.shopping.naver.com/detail/detail.nhn?nvMid=21668252146&NaPm=ct%3Dkb6aggq0%7Cci%3Dec981f90116084215113b82d6e940ad9dfc83d29%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D640c1e2e4b1812cd0dcf740c6bd69df4babb2cbe"
response = requests.get(base_url)
print(response)


# In[3]:


soup = bs(response.text,'html.parser')


# In[4]:


content = soup.select("#_review_list > li")
print(len(content))


# In[5]:


myText = content[1].select("div > div.atc")[0].get_text(strip=True)
print(myText)


# In[ ]:




