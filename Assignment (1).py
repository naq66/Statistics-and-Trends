#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv('car_prices.csv')


# In[4]:


df


# In[5]:


df =df.dropna()


# In[6]:


df.reset_index(inplace = True)


# In[7]:


df = df.drop(['index'],axis = 1)


# In[8]:


df


# In[9]:


# Group by 'year' and count the number of sales in each year
sales_by_year = df.groupby('year').size()

# Plot histogram
plt.bar(sales_by_year.index, sales_by_year.values, color='skyblue')
plt.title('Number of Sales by Year')
plt.xlabel('Year')
plt.ylabel('Number of Sales')
plt.xticks(sales_by_year.index, rotation =45 )
plt.show()


# In[10]:


# Group years into decades
def group_years_into_decades(year):
    return f"{year // 10 * 10}s"

df['decade'] = df['year'].apply(group_years_into_decades)

# Filter data for automatic transmission
automatic_sales = df[df['transmission'] == 'automatic'].groupby('decade').size()

# Filter data for manual transmission
manual_sales = df[df['transmission'] == 'manual'].groupby('decade').size()

# Plot two lines for each transmission type
plt.plot(automatic_sales.index, automatic_sales.values, marker='o', label='Automatic')
plt.plot(manual_sales.index, manual_sales.values, marker='o', label='Manual')

plt.title('Number of Sales by Decade for Each Transmission Type')
plt.xlabel('Decade')
plt.ylabel('Number of Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend(title='Transmission')
plt.show()


# In[16]:


df_automatic= df[df.transmission=="automatic"]




# Plot violin plot
plt.figure(figsize=(5, 6))
sns.violinplot(x='transmission', y='sellingprice', data=df_automatic)
plt.title('Distribution of Selling Prices by Transmission Type')
plt.xlabel('Transmission Type')
plt.ylabel('Selling Price')
plt.show()


# In[ ]:




