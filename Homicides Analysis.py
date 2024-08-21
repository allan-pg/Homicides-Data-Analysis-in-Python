#!/usr/bin/env python
# coding: utf-8

# In[112]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')
plt.style.use('ggplot')


# In[113]:


df = pd.read_csv(r'C:\Users\Admin\Desktop\csv files\homicide_by_countries.csv')
df


# In[114]:


data = df.copy()


# In[115]:


data.info()


# In[116]:


data.isna().any()


# In[117]:


data.shape


# In[118]:


data.sample()


# In[119]:


data.dtypes


# In[120]:


cols = ['Rate', 'Count', 'Year']

for i in cols:
    print(i)
    data[i] = data[i].astype(int)


# In[121]:


data.dtypes


# In[122]:


data.head()


# In[123]:


data.nunique()


# In[124]:


data.columns


# In[125]:


data['Location'].unique()


# In[126]:


data['Rate'].unique()


# In[127]:


data['Year'].unique()


# In[129]:


cor = data.corr()


# In[131]:


sns.heatmap(cor, annot = True)
plt.show


# In[132]:


data.describe() 


# ### 1. Total homicides per Year

# In[133]:


total_homicides = data.groupby('Year')['Count'].sum().sort_values(ascending = False)
total_homicides


# In[134]:


plt.figure(figsize = (9, 6))
sns.lineplot(markers = True, data = total_homicides)
plt.title('Total Homicides from 2006 - 2020')
plt.show()


# In[135]:


data.sample()


# ### 2. Total number of homicides by location (Top 5)

# In[136]:


homicides_per_location = data.groupby('Location')['Count'].sum().sort_values(ascending = False).head(5)
homicides_per_location


# In[137]:


homicides_per_location.plot(x = 'Location', kind = 'pie', autopct = '%1.2f%%')


# ### 3. Total number of homicides by region

# In[198]:


homicides_per_region = data.groupby('Region')['Count'].sum().sort_values(ascending = True).head(10)
homicides_per_region


# In[199]:


plt.figure(figsize =(9, 5))
homicides_per_region.plot(kind = 'barh', x = homicides_per_region.values, y = homicides_per_region.index)
plt.title("Total Homicides per Region")
plt.show()


# In[140]:


data.sample()


# ### 4. Total homicides by subregion

# In[141]:


homicides_per_subregion = data.groupby('Subregion')['Count'].sum().sort_values(ascending = False)
homicides_per_subregion


# In[142]:


plt.figure(figsize = (9, 5))
sns.barplot(x = homicides_per_subregion.index, y = homicides_per_subregion.values, color = 'red')
plt.title("Total Homicides Per Region")
plt.xticks(rotation = 'vertical')
xlabel = 'None'
plt.show()


# In[144]:


filt = (data['Location'] == 'Kenya')
data[filt]


# In[163]:


filt = (data['Year'] > 2016)
df3 = data[filt][['Region', 'Year', 'Count']].reset_index(drop = True)
df3


# In[184]:


df1 = data[data['Region'].isin(['Asia', 'Europe'])]
df1.reset_index(drop = True)


# ### 5. Comparison of Homicides from the year 2017 going Forward in Asia and Europe

# In[185]:


df1 = df1[df1['Year'] > 2016][['Region', 'Year', 'Count']]
df1


# In[186]:


df1 = df1.groupby(['Region', 'Year']).sum()['Count']
df1


# In[187]:


df_unstacked = df1.unstack(level = 0)


# In[188]:


df_unstacked


# In[190]:


df_unstacked.index = df_unstacked.index.astype('int').astype('str')


# In[192]:


df_unstacked.plot(kind = 'line', figsize = (9, 6))
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Number of Homicides from 2017 - 2021 in Asia vs Europe')
plt.show()


# ### 6. Total Rate of Homicides per Year

# In[196]:


df2 = data.groupby('Year')['Rate'].sum().sort_values(ascending = False)
df2


# In[201]:


df2.plot(kind = 'bar', figsize = (9, 6))
plt.title('Rate of Homicides by Year')
plt.ylabel('Sum of Rate')
plt.show()


# In[204]:


df4 = data.groupby('Subregion')['Count'].mean().sort_values().round(2)
df4


# In[205]:


df4.index


# In[206]:


df4.values


# In[208]:


data = {
    'Category': df4.index,
    'Values': df4.values,
    'Info': df4.values
}
data1 = pd.DataFrame(data)
data1


# In[212]:


fig = px.treemap(data1, path = ['Category'], values = 'Values', title = 'Treemap')
fig.update_traces(hovertemplate = 'Category: %{label}<br>Values: %{value}')
fig.show()


# In[ ]:




