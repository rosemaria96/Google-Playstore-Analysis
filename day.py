
#--------------------Extraction-----------------------------

import zipfile
zip_path = r"C:\Users\ACER\Downloads\archive (2).zip"
extract_path = r"D:\Googleplay"

with zipfile.ZipFile(zip_path,'r') as zip_ref:
    zip_ref.extractall(extract_path)                    
print("Extracted")

#------------------------Data info--------------------------
import pandas as pd
df = pd.read_csv("D:\Googleplay\googleplaystore.csv")
print(df.head())
df.info()
print(df.describe())
print(df.describe(include='all'))
print(df.isnull().values.any())
print(df.isnull().sum())

#-----------------------Missing Value Visualization-----------------------
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(df.isnull(), cbar=False)
plt.show()

#------------------Datatype Conversions----------------
print(df['Category'].unique())
print(df['Installs'].head())
df['Reviews'] = pd.to_numeric(df['Reviews'], errors= 'coerce')
print(df['Reviews'].head())
df['Price'] = df['Price'].str.replace('$','', regex=False)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Installs'] = df['Installs'].str.replace('+','', regex=False)
df['Installs'] = df['Installs'].str.replace(',','', regex=False)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')
print(df['Last Updated'].unique())
df['Last Updated']=pd.to_datetime(df['Last Updated'], errors='coerce')
print(df['Size'].unique())
df['Size']=df['Size'].str.replace('K','000',regex=False)
df['Size']=df['Size'].str.replace('M','000000',regex=False)
df['Size']=df['Size'].replace('Varies with device',None)
df['Size']=pd.to_numeric(df['Size'], errors = 'coerce')
print(df['Android Ver'].unique())
df['Android Ver']=df['Android Ver'].str.replace('and up','',regex=False)
df['Android Ver']=df['Android Ver'].replace('Varies with device',None)
df['Android Ver']=df['Android Ver'].str.split('-').str[0]
df['Android Ver']=pd.to_numeric(df['Android Ver'], errors ='coerce')
df['Current Ver']=df['Current Ver'].replace('Varies with device', None)
print(df.dtypes)

#-----------verify---------
df.info()
print(df.isnull().sum())
df.describe()

#--------------Missing Value Handling-----------------------
df['Reviews'] = df['Reviews'].fillna(df['Reviews'].mean())
df['Rating'] = df['Rating'].fillna(df['Rating'].mean())
df['Installs'] = df['Installs'].fillna(df['Installs'].median())
df['Price'] = df['Price'].fillna(df['Price'].median())
df['Size'] = df['Size'].fillna(df['Size'].median())
df['Android Ver'] = df['Android Ver'].fillna(df['Android Ver'].median())
df['Last Updated'] = df['Last Updated'].fillna(df['Last Updated'].mode()[0])
df['Current Ver'] = df['Current Ver'].fillna(df['Current Ver'].mode()[0])
df['Content Rating'] = df['Content Rating'].fillna(df['Content Rating'].mode()[0])
df['Type'] = df['Type'].fillna(df['Type'].mode()[0])
print(df.isnull().sum())

#---------------Duplicate values Removal-----------------
print(df.duplicated().sum())
print(df[df.duplicated()])
df= df.drop_duplicates()
print(df.duplicated().sum())
print(df[df.duplicated(subset='App')])
df = df.sort_values('Reviews', ascending=False)
df = df.drop_duplicates(subset='App', keep='first')
print(df.duplicated(subset='App').sum())

#----------------Wrong Data Removal---------------
df = df[df['Category'] != '1.9']
print(df['Category'].unique())

#----------------EDA---------------------------
df[['Reviews','Installs']].corr()
sns.scatterplot(x='Reviews', y='Installs', data = df)
plt.show()

df.groupby('Category')['Rating'].mean().sort_values(ascending=False).plot(kind='bar')
plt.xticks(rotation=90)
plt.tight_layout()  
plt.show()

sns.countplot(x='Category', hue='Type', data=df)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

df['Type'].value_counts()
sns.countplot(x='Type', data=df)
plt.show()

df['Content Rating'].value_counts()
sns.countplot(y='Content Rating', data=df)
plt.show()

sns.histplot(df['Price'], bins=30)
plt.show()

sns.histplot(df['Reviews'], bins=50)
plt.show()

df.groupby('Category')['Installs'].sum().sort_values(ascending=False).plot(kind='bar')
plt.xticks(rotation = 90)
plt.tight_layout()
plt.show()

top10 = df.sort_values('Rating', ascending=False).head(10)
top10 = top10[top10['App'].str.contains(r'^[\x00-\x7F]+$', regex=True)]
sns.barplot(x='Rating', y='App', data=top10)
plt.title("Top 10 Highest Rated Apps")
plt.tight_layout()
plt.show()

df.groupby('Type')['Rating'].mean()
sns.barplot(x='Type', y='Rating', data=df)
plt.title("Average Rating: Free vs Paid Apps")
plt.xlabel("App Type")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()


#-------------------Saving Cleaned Dataset----------------------------
df.to_csv("D:\Googleplay\cleaned_google_playstore.csv", index=False)

#--------------------------Automatic Profiling----------------------
from ydata_profiling import ProfileReport
profile = ProfileReport(df, title="Cleaned Playstore Dataset Report", explorative=True)
profile.to_file("D:\Googleplay\cleaned_data_report.html")