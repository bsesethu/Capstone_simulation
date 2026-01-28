#import os    # to find the directory you're currently in
#print (os.getcwd())  #oooh sana, I just copied the file to the current directory

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Crime_data_A_new.csv')
print(df.head(5))

# print(df.columns) this shows it horizontally
for col in df.columns:
    print(col)

# Replace new line with space
#df.columns = df.columns.str.replace('\n', ' ', regex = True)

# Remove leading & trailing spaces
#df.columns = df.columns.str.strip()

# Replace spaces with underscores
df.columns = df.columns.str.replace('\n', ' ', regex=True).str.strip().str.replace(' ', '_')

#view these columns again
print(df.columns.tolist())

# Filtering for Mpumalanga
print('Mpumalanga' in df.columns)

# Keeping only columns I intend on using
df_mp = df[['CRIME_CATEGORY', 'Mpumalanga']].copy()

# Drop rows where MP has no data
df_mp.dropna(subset = ['Mpumalanga'], inplace = True)

# remove trailing/leading spaces 
df_mp['CRIME_CATEGORY'] = df_mp['CRIME_CATEGORY'].str.strip()

# Some Stats nyana

# Summary stats for the province
print(df_mp['Mpumalanga'].describe())

# Top 5 reported crimes
top5_crimes = df_mp.sort_values(by = 'Mpumalanga', ascending = False).head()  #Pieter would be proud kwaaaa
print(top5_crimes)

# Bar Chart to show Top 5 crimes in MP
plt.figure(figsize = (10,6))
sns.barplot(x = 'Mpumalanga', y = 'CRIME_CATEGORY', data =  top5_crimes)
plt.title('Top 5 Crimes in Mpumalanga')
plt.xlabel('Number of Cases')
plt.ylabel('Crime Category')
plt.tight_layout()
plt.show()

# Sort the top 5 crimes in descending order
top_crimes = df_mp.sort_values(by = 'Mpumalanga', ascending = False).head(5)

# Pie Chart
plt.figure(figsize = (7,7))
plt.pie(top_crimes['Mpumalanga'], labels = top_crimes['CRIME_CATEGORY'])
plt.title('Top 5 Crimes in the MP Province')
plt.axis('equal')
plt.show()

# Save the cleaned MP Dataset
df_mp.to_csv('cleaned_mpumalanga_crime.csv', index = False)


