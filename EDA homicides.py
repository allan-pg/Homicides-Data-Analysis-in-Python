#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
plt.style.use('ggplot')
import warnings
warnings.filterwarnings('ignore')


# In[33]:


df = pd.read_csv(r'C:\Users\Admin\Desktop\csv files\homicide-data.csv', encoding='unicode_escape')
df


# In[34]:


df.shape


# In[6]:


df.columns


# In[121]:


df = df.rename(columns = {'lat': 'latitude', 'lon' : 'longitude'})


# In[43]:


df = df.dropna(how = 'all')


# In[11]:


df.dtypes


# In[13]:


data = df.copy() 


# In[44]:


df.isna().sum()


# In[16]:


import datetime
import re


# In[46]:


date_col = df['reported_date']
filt = '201511...'
match = date_col.str.match(filt)
df_filtered = df[match]
df_filtered


# In[39]:


i = df_filtered.index
i


# In[30]:


df = df.drop(i)
df


# In[47]:


df['reported_date'] = pd.to_datetime(df['reported_date'])


# In[51]:


df.info()


# In[54]:


df.isna().sum()


# In[61]:


df = df.dropna(how = 'any')
df.isnull().sum()


# In[126]:


cor = df.corr()


# In[127]:


plt.figure(figsize = (11, 6))

sns.heatmap(cor, annot = True, cmap = 'icefire')


# ### Find states with the highest and lowest homicides rate

# In[67]:


top_10_states = df['state'].value_counts().sort_values(ascending = True).head(10)
bottom_10_states = df['state'].value_counts().sort_values(ascending = False).head(10)


# In[72]:


plt.figure(figsize = (18, 6))

plt.subplot(1, 2, 1)
top_10_states.plot(kind = 'barh')
plt.title('Top 10 states with highest homicides')
plt.ylabel('Number of homicides')


plt.subplot(1, 2, 2)
bottom_10_states.plot(kind = 'barh')
plt.title('Bottom 10 states with highest homicides')
plt.ylabel('Number of homicides')
plt.show()


# ### Number of Homicides by city

# In[76]:


top_10_cities = df['city'].value_counts().sort_values(ascending = True).head(10)
bottom_10_cities = df['city'].value_counts().sort_values(ascending = False).head(10)


# In[77]:


plt.figure(figsize = (18, 6))

plt.subplot(1, 2, 1)
top_10_cities.plot(kind = 'barh')
plt.title('Top 10 Cities with highest homicides')
plt.ylabel('Number of homicides')


plt.subplot(1, 2, 2)
bottom_10_cities.plot(kind = 'barh')
plt.title('Bottom 10 Cities with highest homicides')
plt.ylabel('Number of homicides')
plt.show()

# ### Homicides trend over time

# In[79]:


df['Year'] = df['reported_date'].dt.year


# In[80]:


df


# In[81]:


year_homicides = df['Year'].value_counts()


# In[83]:


plt.figure(figsize = (10, 6))

sns.lineplot(data=year_homicides)
plt.title('Homicides per Year')
plt.ylabel('Number of Homicides')
plt.xlabel('Year')
plt.show()


# In[88]:


df['Month_name'] = df['reported_date'].dt.month_name()


# In[89]:


df 


# In[90]:


monthly_homicide = df['Month_name'].value_counts()


# In[91]:


plt.figure(figsize = (10, 6))

sns.lineplot(data = monthly_homicide)
plt.title('Homicides per Month')
plt.ylabel('Number of Homicides')
plt.xlabel('Year')

plt.show()


# In[100]:


df['day_name'] = df['reported_date'].dt.day_name()


# In[101]:


df


# In[102]:


daily_homicide = df['day_name'].value_counts()


# In[103]:


plt.figure(figsize = (10, 6))

sns.lineplot(data = daily_homicide)
plt.title('Homicides per Day')
plt.ylabel('Number of Homicides')
plt.xlabel('Year')

plt.show()


# ### Race Distribution' and Sex Distribution of homicides

# In[93]:


race_counts = df['victim_race'].value_counts()
sex_counts = df['victim_sex'].value_counts()
fig, axs = plt.subplots(1, 2, figsize=(12, 6))


axs[0].pie(race_counts, labels=race_counts.index, autopct='%1.1f%%', startangle=90)
axs[0].set_title('Race Distribution')


axs[1].pie(sex_counts, labels=sex_counts.index, autopct='%1.1f%%', startangle=90)
axs[1].set_title('Sex Distribution')

plt.show()


# ### Homicides per age group

# In[105]:


df = df.replace('', np.nan)


# In[107]:


df['victim_age'] = df['victim_age'].astype(float)


# In[110]:


mean = round(df['victim_age'].mean(), 0)
mean


# In[111]:


df['victim_age'] = df['victim_age'].fillna(mean)


# In[114]:


df['victim_age'] = df['victim_age'].astype(int)


# In[129]:


bins = [0, 20, 40, 60, 80]
labels = ['young', 'middle-aged', 'old', 'very-old']

df['age_bin'] = pd.cut(df['victim_age'], bins, labels=labels)

df


# In[131]:


homicides_age_group = df['age_bin'].value_counts(ascending = False)


# In[134]:


plt.figure(figsize = (10, 6))

homicides_age_group.plot(kind = 'bar')
plt.title('Homicides per age group')
plt.ylabel('Number of Homicides')
plt.xlabel('age group')

plt.show()


# In[136]:


df4 = df.groupby('state')['victim_age'].mean().sort_values().round(2)
df4


# In[138]:


data1 = {
    'Category': df4.index,
    'Values': df4.values,
    'Info': df4.values
}
data2 = pd.DataFrame(data1)
data2


# In[140]:


import plotly.express as px


# In[141]:


fig = px.treemap(data1, path = ['Category'], values = 'Values', title = 'Treemap')
fig.update_traces(hovertemplate = 'Category: %{label}<br>Values: %{value}')
fig.show()


# In[ ]:




