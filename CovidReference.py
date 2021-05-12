#!/usr/bin/env python
# coding: utf-8

# In[115]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import html5lib


# In[133]:


DF=pd.read_html("https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US:en")
df=DF[0]
def table():
    print (df)


# In[141]:


#print (df[0].describe().round())
#df1=df
#df1=df1[df1['Recovered'] != '—']
#print (df1.head(10))
#print (df1['Deaths'].cumsum())


# In[142]:


def toptable():
    df1=df
    df1=df1[df1['Recovered'] != '—']
    df1=df1.drop(df1.index[5:13])
    df1=df1.head(6)
    print (df1)
    df1['Recovered']=df1['Recovered'].apply(pd.to_numeric)



# In[143]:


def bargraph():
    toptable()
    fig, ax = plt.subplots(figsize=(13,6))
    index = np.arange(6)
    bar_width = 0.25
    opacity = 0.8

    rects1 = plt.bar(index, df1['Confirmed'], bar_width,
                     alpha=opacity,
                     color='b',
                     label='Confirmed')

    rects2 = plt.bar(index + bar_width, df1['Recovered'], bar_width,
                     alpha=opacity,
                     color='g',
                     label='Recovered')

    rects3 = plt.bar(index + 2*bar_width, df1['Deaths'], bar_width,
                     alpha=opacity,
                     color='black',
                     label='Deaths')
    plt.xlabel('Country')
    plt.ylabel('Population')
    plt.title('Scores by person')
    plt.xticks(index + bar_width, df1['Location'])
    plt.legend()
    plt.tight_layout()
    plt.show()


# In[ ]:





# In[162]:


#dfc=pd.read_csv('/home/gitvizwoir1/covid_19_india.csv')
#dfc.tail(10)


# In[163]:


def lgraph():
    dfc=pd.read_csv('/home/gitvizwoir1/covid_19_india.csv')
    fig, ax = plt.subplots(figsize=(13,6))

    dfc['Date']=pd.to_datetime(dfc['Date'], format='%d/%m/%y') 
    #print(dfc.dtypes)
    dfd=dfc.groupby("Date")["Confirmed"].sum()
    print(dfd.tail(5))
    plt.xlabel('Time')
    plt.ylabel('Population')
    type(dfd)
    plt.plot(dfd)
    #dfd.describe()
    #print(dfd['Confirmed'])
    #plt.plot(dfd['Date'])


# In[101]:





# In[ ]:





# In[ ]:





# In[165]:





# In[144]:


bargraph()


# In[164]:


lgraph()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




