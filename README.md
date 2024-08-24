# Homicides Data Analysis in Python
![image](https://github.com/user-attachments/assets/d094358f-4385-4b34-8525-1226818571c5)  

## Intoduction
<a href='Data Cleaning'>Data Cleaning </a>
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

## <a href='Data Cleaning'>Data Cleaning </a>
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
