# Homicides Data Analysis in Python
![image](https://github.com/user-attachments/assets/d094358f-4385-4b34-8525-1226818571c5)  

## Intoduction

## What is Homicide
Homicide is the killing of a person by another with intent to cause death or serious injury, by any means. It excludes death due to legal intervention and operations of war.  
Study from WHO shows that 19 persons out of 100,000 die by homicide and majority of them are men.
## Data Extraction
I downloaded dataset from <a href="https://www.kaggle.com/datasets/joebeachcapital/homicides">kaggle</a> The dataset contains 12 columns and 52179 rows.

## Import libraries we shall use
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
plt.style.use('ggplot')
import warnings
warnings.filterwarnings('ignore')
```

## Data Cleaning
Date column was not properly formated. I loaded the data to excel. Click on date column    
![image](https://github.com/user-attachments/assets/f3b9bfe1-92de-4b76-ac50-5204f97579ab)  

then on data tab click text to columns.  
![image](https://github.com/user-attachments/assets/94ad6f77-fa0a-4f76-81e1-d12050f7b526)  

Tick delimited and click next,  
![image](https://github.com/user-attachments/assets/8470256e-793f-4362-9654-b7654fcaa95e)  

 tick other and click on next,  
 ![image](https://github.com/user-attachments/assets/02915d68-8d94-4de8-ac2e-22992226f9b5)  

 tick Date checkbox and click on finish  
 ![image](https://github.com/user-attachments/assets/fbd91d29-271d-44c1-bda7-18a842984c89)  
 - Coverted reported date column to a date type using pandas and extracted month name and day name from the same column
```python
df['reported_date'] = pd.to_datetime(df['reported_date'])
df['Year'] = df['reported_date'].dt.year
df['Month_name'] = df['reported_date'].dt.month_name()
df['day_name'] = df['reported_date'].dt.day_name()
```
![image](https://github.com/user-attachments/assets/7db95d68-7d0a-4d18-97b3-9d65e644625a)  
- Dropped rows with null values
```python
df = df.dropna(how = 'any')
```
- Renamed columns lat and lon to a more readable format
```python
df = df.rename(columns = {'lat': 'latitude', 'lon' : 'longitude'})
```
- coverted victims_age to a float and filled nan using mean age
```python
df = df.replace('', np.nan)
df['victim_age'] = df['victim_age'].astype(float)
mean = round(df['victim_age'].mean(), 0)
df['victim_age'] = df['victim_age'].fillna(mean)
```

## Exploratory Data Analysis and Visualisation
1. Find summary information of data set
```python
df.info()
```
2. Conduct descriptive statistics
```python
df.describe()
```
![image](https://github.com/user-attachments/assets/47be9bc1-37ca-4edc-bfb3-80248e6892c9)  

- From this we can see minimum age is 0 and maximum age is zero
- the data is from 2007 - 2017
- number of rows has reduced to 52116 after dropping rows with null values
3. Find the correlation in our data and use a heatmap to visualize findings
```python
cor = df.corr()
plt.figure(figsize = (11, 6))

sns.heatmap(cor, annot = True, cmap = 'icefire')
```
![image](https://github.com/user-attachments/assets/89c37449-7300-4d4c-adb6-999056b68210)  

4. Find states with the highest and lowest homicides rate and visualize your findings
```python
top_10_states = df['state'].value_counts().sort_values(ascending = False).head(10)
bottom_10_states = df['state'].value_counts().sort_values(ascending = True).head(10)

plt.figure(figsize = (18, 6))

plt.subplot(1, 2, 1)
top_10_states.plot(kind = 'bar')
plt.title('Top 10 states with highest homicides')
plt.ylabel('Number of homicides')


plt.subplot(1, 2, 2)
bottom_10_states.plot(kind = 'bar')
plt.title('Bottom 10 states with highest homicides')
plt.ylabel('Number of homicides')
plt.show()
```
![image](https://github.com/user-attachments/assets/07530e55-d9dd-4703-9db7-8d9e1b9fb870)  

5. Number of Homicides by city
```python
top_10_cities = df['city'].value_counts().sort_values(ascending = False).head(10)
bottom_10_cities = df['city'].value_counts().sort_values(ascending = True).head(10)

plt.figure(figsize = (18, 6))

plt.subplot(1, 2, 1)
top_10_cities.plot(kind = 'bar')
plt.title('Top 10 Cities with highest homicides')
plt.ylabel('Number of homicides')


plt.subplot(1, 2, 2)
bottom_10_cities.plot(kind = 'bar')
plt.title('Bottom 10 Cities with highest homicides')
plt.ylabel('Number of homicides')
plt.show()
```
![image](https://github.com/user-attachments/assets/2f2a0026-6379-47c2-826b-b626e610d5d0)  

6. Homicides trend over time
- Yearly
```python
year_homicides = df['Year'].value_counts()

plt.figure(figsize = (10, 6))

sns.lineplot(data=year_homicides)
plt.title('Homicides per Year')
plt.ylabel('Number of Homicides')
plt.xlabel('Year')
plt.show()
```
![image](https://github.com/user-attachments/assets/c3beecde-3cbd-4e2d-a0b0-2bb705d9b327)  

- Monthly
```python
monthly_homicide = df['Month_name'].value_counts()

plt.figure(figsize = (10, 6))

sns.lineplot(data = monthly_homicide)
plt.title('Homicides per Month')
plt.ylabel('Number of Homicides')
plt.xlabel('Year')
plt.xticks(rotation = 'vertical')
xlabel = 'None'

plt.show()
```
![image](https://github.com/user-attachments/assets/9dc2cc5c-0164-4600-a5bb-a3610b78817c)  

- Weekly
```python
daily_homicide = df['day_name'].value_counts()

plt.figure(figsize = (10, 6))

sns.lineplot(data = daily_homicide)
plt.title('Homicides per Day')
plt.ylabel('Number of Homicides')
plt.xlabel('Year')

plt.show()
```
![image](https://github.com/user-attachments/assets/cff37db9-4b38-423e-a12a-c839a49b5311)  

7. Race Distribution' and Sex Distribution of homicides
```python
race_counts = df['victim_race'].value_counts()
sex_counts = df['victim_sex'].value_counts()
fig, axs = plt.subplots(1, 2, figsize=(12, 6))


axs[0].pie(race_counts, labels=race_counts.index, autopct='%1.1f%%', startangle=90)
axs[0].set_title('Race Distribution')


axs[1].pie(sex_counts, labels=sex_counts.index, autopct='%1.1f%%', startangle=90)
axs[1].set_title('Sex Distribution')

plt.show()
```
![image](https://github.com/user-attachments/assets/229dbe33-ea4d-420f-89d4-9e1302dd6848)  

8. Homicides per age group
```python
bins = [0, 20, 40, 60, 80]
labels = ['young', 'middle-aged', 'old', 'very-old']

df['age_bin'] = pd.cut(df['victim_age'], bins, labels=labels)

homicides_age_group = df['age_bin'].value_counts(ascending = False)
plt.figure(figsize = (10, 6))

homicides_age_group.plot(kind = 'bar')
plt.title('Homicides per age group')
plt.ylabel('Number of Homicides')
plt.xlabel('age group')

plt.show()
```
![image](https://github.com/user-attachments/assets/beebb029-94cd-4b9a-8dfd-4675fed911a5)  

9. Treemap showing mean age per state
```python
import plotly.express as px
df4 = df.groupby('state')['victim_age'].mean().sort_values().round(2)

data1 = {
    'Category': df4.index,
    'Values': df4.values,
    'Info': df4.values
}
data2 = pd.DataFrame(data1)
print(data2)

fig = px.treemap(data1, path = ['Category'], values = 'Values', title = 'Treemap')
fig.update_traces(hovertemplate = 'Category: %{label}<br>Values: %{value}')
fig.show()
```
![image](https://github.com/user-attachments/assets/cb9dc727-4cbe-43b7-b578-d4c61f73ae5e)  

## Findings
- California state had the highest number of homicides rate followed by Texas, Illinois
- Colorado state had the lowest number of homicides rate followed by minnesota and new mexico
- Chicago city had the highest number of homicides rate of over 5000 while had the lowest number of homicides rate
- Over the years number  of homicides has been rising rapidly
- July had the highest number of homicides rate followed by june and august
- Most of the homicides occured during weekend that is saturday and sunday
- Black men experienced the highest number of homicides
- Over 30000 of homicides happened to people aged between 20 and 40

## Conclusion
- Colarado, Minnesota, and new mexico are one of the safest places to live in
- As a black person who is a male chicago is one of the most dangerous places to live
- Most of the homicides occur during summer









