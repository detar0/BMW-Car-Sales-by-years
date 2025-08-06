# -*- coding: utf-8 -*-
"""Untitled7.ipynb

import pandas as pd
import matplotlib.pyplot as plt

df =  pd.read_csv("/BMW_Car_Sales_Classification.csv")
print(df.head(10))
# Checking for unique values
print(df["Model"].unique())
data = df["Price_USD"]
# Checking for NaN and others
print(df.isnull().sum())
# Converting to numeric
cleared=pd.to_numeric(data,errors="coerce")
print(cleared)


# Filtering data by years
st_yr=2014
nd_yr=2024
data_2014 = df[df["Year"] == st_yr]
data_2024 = df[df["Year"] == nd_yr]
data_2014["Price_USD"] = pd.to_numeric(data_2014["Price_USD"], errors="coerce")
data_2024["Price_USD"] = pd.to_numeric(data_2024["Price_USD"], errors="coerce")

#Sorting by largest models
top_8_2014 = data_2014.nlargest(12, "Price_USD")["Model"].tolist()
top_8_2024 = data_2024.nlargest(8, "Price_USD")["Model"].tolist()
data_2014["Model_Filtered"]=data_2014["Model"].apply(lambda x:x if x in top_8_2014 else "Others")
data_2024["Model_Filtered"]=data_2024["Model"].apply(lambda x:x if x in top_8_2024 else "Others")
result_2014 = data_2014.groupby("Model_Filtered")["Price_USD"].sum().reset_index()
result_2024 = data_2024.groupby("Model_Filtered")["Price_USD"].sum().reset_index()

fig,(ax1,ax2) = plt.subplots(1,2, figsize=(10,8))
#Creating the charts
ax1.pie(result_2014["Price_USD"], labels=result_2014["Model_Filtered"], autopct = "%1.1f%%")
ax1.set_title("BMW largest sold models in 2014")

ax2.pie(result_2024["Price_USD"], labels=result_2024["Model_Filtered"],  autopct = "%1.1f%%")
ax2.set_title("BMW largest sold models in 2024")

plt.tight_layout()
plt.show()
