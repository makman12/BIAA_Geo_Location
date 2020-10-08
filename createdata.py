#!/usr/bin/env python
# coding: utf-8

# In[19]:


import wikipedia
from Gmap import gmap
from getpleides import getple
from getty2 import getgetty
import pandas as pd


# In[5]:


def wikisearch(query):
    q=wikipedia.search(query)[0]
    coordinates=wikipedia.WikipediaPage(q).coordinates
    x=float(coordinates[0])
    y=float(coordinates[1])
    coordinates=[x,y]
    return q, coordinates


# In[68]:


def createdata(Name, City, Modern):
    columns=[
 'Ancient Site',
 'Modern Province',
 'Modern Site',
 'Place Type',
 'Google Adress',
 'Google Coordinates',
 'Getty Name',
 'Getty ID', "Getty Coordinates", "Getty All Names",
 'Pleiades Name',
 'Pleiades ID',
 'Pleiades Coordinates',
 'Wiki Name',
 'Wiki Coordinates']
    query=Name
    data=pd.DataFrame(columns=columns)
    data=data.append(pd.Series(), ignore_index=True)
    data.iloc[0]['Modern Province']=City
    
    if Modern:
        data.iloc[0]["Modern Site"]=Name
    else:
        data.iloc[0]["Ancient Site"]=Name
    
    googledata=gmap(query)
    data.iloc[0]['Google Coordinates']=googledata[0:2]
    data.iloc[0]['Google Adress']=googledata[2]
    try:
        wikidata=wikisearch(query)
        data.iloc[0]['Wiki Name']=wikidata[0]
        data.iloc[0]['Wiki Coordinates']=wikidata[1]
        source=wikidata
    except:
        wikidata=False
        source=googledata
    try:
        gettydata=getgetty(source[0],source[1])
        data.iloc[0]['Getty Name']=gettydata[0][1]
        data.iloc[0]['Getty ID']=gettydata[0][0]
        data.iloc[0]['Getty All Names']=gettydata[0][2]
        data.iloc[0]['Getty Coordinates']=gettydata[0][3]
    except:
        gettydata=False
    try:
        pledata=getple(source[0],source[1])
        data.iloc[0]['Pleiades Name']=pledata[0][0]
        data.iloc[0]['Pleiades ID']=pledata[0][1]
        data.iloc[0]['Pleiades Coordinates']=pledata[0][2]
    except:
        pledata=False
        
    
    return(data)

