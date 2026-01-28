import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from xlwings import view

file = pd.read_excel('Crime_data_A_newCSV')

df = pd.read_csv('Crime_data_A_newCSV')
print(df.head(15))


df_condensed = df.loc[0:10] #select rows 0 through to 8.

df 

