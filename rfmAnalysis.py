# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno

import warnings
warnings.filterwarnings('ignore')

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

df_2010_2011 = pd.read_excel("RFM/online_retail_II.xlsx", sheet_name="Year 2010-2011")

# Let's copy dataframe to be able reach the original dataset afterwards
df = df_2010_2011.copy()

# Show the first 5 rows of the dataset
df.head()


# Show the last 5 rows of the dataset
df.tail()

# Shape of the dataset
df.shape

# See some basic information about the dataset
df.info()

# Check if there are any missing values
df.isnull().values.any()

# Missing values for each variable/column
df.isnull().sum()

# Number of unique values in column 'Description'? / How many different products do we have?
df["Description"].nunique()


# Show the products and order quantity
df["Description"].value_counts().head()


# The most ordered products (in descending order)
df.groupby("Description").agg({"Quantity":"sum"}).sort_values("Quantity", ascending = False).head()

# Show the first 5 rows of the dataset
df.head()


print("Total transactions: ", df.shape[0])
print("Total missing values: {} - which is {:.2f}% of our total data".format(df.isnull().sum().sum(), (df.isnull().sum().sum()*100)/df.shape[0]))
print("Total unique Countries: ", df.Country.nunique())
print("Total unique description: ", df.Description.nunique())


initial_countries=df.Country.unique()
initial_countries

# Checking for records having negative price
df.loc[df['Price'] < 0]



# Visualizing Missing values using missno library
msno.bar(df)
plt.show()
msno.heatmap(df)
plt.show()

# Drop all missing values
df.dropna(inplace=True)

# Verifying the null values
df.isnull().sum()

df.shape

# Grouping countries by Total quantity
df.groupby('Country')['Quantity'].sum().sort_values(ascending=False)

# Finding the duplicate transactions in the dataset
print("Duplicated Transactions")
df.duplicated().sum()

# Removing Duplicated Transactions
df.drop_duplicates(inplace = True)
print("Dataset shape after removing duplicates transactions")
df.shape

print("Total Products: ", len(df['StockCode'].unique()))
print("Total Transactions: ",len(df['Invoice'].unique()))
print('Total customers: ', len(df['Customer ID'].unique()))

# Initial Countries
initial_countries

# Types of Country
df.Country.unique()

df[df['Invoice'].apply(lambda x: int('C' in str(x)))==1]

# Checking transaction record for a customer
df.loc[df['Customer ID'] == 16321].sort_values(by = ['Price','Quantity','InvoiceDate'])

# Removing the cancelled transaction on df
cancelled_index=df[df['Invoice'].apply(lambda x: int('C' in str(x)))==1].index
df.drop(cancelled_index , inplace=True)


# Filtering the dataset by choosing positive values of Quantity and df
df = df[(df.Quantity>0) & (df.Price > 0)]

df.head()


# Saving the filtered data into new file
df.to_csv('RFM/filtered_data.csv')