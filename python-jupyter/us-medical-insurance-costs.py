#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# 
# 
#     Figure out what the average age is for someone who has at least one child in this dataset.
# 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df = pd.read_csv('insurance.csv')


# In[2]:


df.head()


# In[3]:


print(df.info())
print(df.describe())


# In[26]:


genders_df = df.groupby("sex").agg([np.mean, np.std])
genders_df.head()


# #### Here we can see that we do not have Null data and every cell is populated with data

# This shows us the distribution of age by the count from this dataset

# In[5]:


genders = genders_df['charges']
genders.plot(kind = "barh", y = "mean", legend = False,
            title = "Average Cost")


# From here we can see that the average cost of insurance is higher for men

# In[19]:


grid = sns.FacetGrid(df, col = "smoker", hue = "smoker", col_wrap=5)
grid.map(sns.scatterplot, "bmi", "charges")


# #### This graph gives us a lot of insight about the cost of insurance based on bmi, and smoker status, as well as we can see the distribution between the bmi and smoker status
# 

# Now how about we try to find what would be the average cost of insurance for men with at least one child
# 

# In[7]:


gender = df['sex']
children = df['children']
cost = df['charges']
gender_dict = {'male':[], 'female':[]}

for i in range(len(children)):
    if children[i] != 0:
        gender_dict[gender[i]].append((cost[i], children[i]))
    else:
        continue
avrg_cost_men_with_children = 0
for cost, num_children in gender_dict['male']:
    avrg_cost_men_with_children += cost
avrg_cost_men_with_children = avrg_cost_men_with_children / len(gender_dict['male'])
print('Average cost of insurance for men that have at least one child is ${}'.format(round(avrg_cost_men_with_children, 2)))


# In[25]:


grid = sns.FacetGrid(df, col = "children", hue = "children", col_wrap=5)
grid.map(sns.scatterplot, "sex", "charges")


# In[8]:


regions = df['region']
print('Here we can see the different regions in this dataset:')
for region in regions.unique():
    print(region)


# In[27]:


sns.catplot(x='region', y='charges', 
            data = df,
            jitter = '0.25')
print('Charges by the region')


# Here we can observe charges based on the regions and we can see that the distribution of values is not even, let's make a further analysis of this observation

# In[14]:


sns.catplot(x='region', y='bmi', 
            data = df,
            jitter = '0.25')
print('BMI by the region')


# Here we can see a better data regardging distribution of charges in different regions based on sex

# In[11]:


sns.catplot(x="sex", y="charges", hue="region", kind="bar", data=df)


# Here we can see a better data regardging distribution of charges in different regions based on smoking status

# In[28]:


sns.catplot(x="smoker", y="charges", hue="region", kind="bar", data=df)


# In[ ]:




