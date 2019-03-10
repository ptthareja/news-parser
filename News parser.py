#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
pd.options.display.max_colwidth=500


# In[2]:


class News:
    def __init__(self, term):
        self.term = term
        self.url = 'https://www.google.com/search?q={0}&source=lnms&tbm=nws'.format(self.term)
        self.title = []
        self.date = []
        self.link = []
        self.df = pd.DataFrame()
    
    def run(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for n in range(10):
            self.title.append(soup.find_all('div', {'class': 'g'})[n].a.get_text())
            self.link.append(soup.find_all('div', {'class': 'g'})[n].a['href'].split('/url?q=')[1].split('&sa=U')[0])
            self.date.append(soup.find_all('div', {'class': 'g'})[n].span.get_text().split(' - ')[1])
        self.df = pd.concat([pd.Series(self.date), pd.Series(self.title), pd.Series(self.link)], axis=1).rename({0:'Date/Time', 1:'Keywords', 2:'URL'}, axis=1)
        
        return self.df


# In[3]:


a = News('Haryana Cabinet Approves Delhi-Gurugram-SNB RRTS Corridor')
df = a.run()


# In[4]:


df


# In[5]:


name = ('News Results for '+a.term)+'.csv'
df.to_csv(name, index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




