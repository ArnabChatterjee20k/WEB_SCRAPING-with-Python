#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs
import requests


# In[2]:
topic="winter"

link=f"https://en.wikipedia.org/wiki/{topic}"
requests.get(link).status_code


# In[3]:


page=requests.get(link)
soup=bs(page.content,"html.parser")
# print(soup.prettify())


# In[4]:


body=soup.body
data=""
new=[]
for i in body.find_all("p"):
    data+=i.text
    for j in i.find_all("a"):
        new.append(str(j.text))
        


# In[5]:


for i in new:
    if i in data:
        data=data.replace(i,"")
    

for i in new:
    if i in data:
        print("true")
    
    


# In[6]:



data


# In[7]:


with open("test.txt","w",encoding="utf8") as f:
        f.write(data)
    


# In[ ]:





# In[ ]:




