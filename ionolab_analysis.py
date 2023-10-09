from datetime import datetime, timedelta
from functools import reduce

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import xlrd
import os


tarama = os.scandir()
new_df = pd.DataFrame()

for belge in tarama:
    try:
        dataList = list()
        belge = belge.name
        abcDF = pd.read_excel(belge, skiprows=1)
        for i in range(len(abcDF)):
            dataList.append(abcDF.iloc[i][2])

        
        
        new_df[abcDF.iloc[0][1].strftime('%Y-%m-%d')] = dataList
        
    except:
        continue

def sortDF(new_df):
    sorted_new_df = sorted(new_df.columns)
    # df = df[sorted_columns]
    new_df = new_df[sorted_new_df]
    return new_df
def control(x,y):
    a = datetime.strptime(y,'%Y-%m-%d') - datetime.strptime(x,'%Y-%m-%d')
    
    if a == timedelta(days=1): return True
    
    else: return (datetime.strptime(x,'%Y-%m-%d') + timedelta(days=1))


new_df = sortDF(new_df)

for i in range(len(new_df.columns)-1):
    #print(new_df.columns[i],new_df.columns[i+1])
    if control(new_df.columns[i],new_df.columns[i+1]) != True:
        print(control(new_df.columns[i],new_df.columns[i+1]).strftime('%Y-%m-%d'))
        new_df[datetime.strftime(control(new_df.columns[i],new_df.columns[i+1]),'%Y-%m-%d')] = 0
        new_df = sortDF(new_df)

ax = sns.heatmap(new_df, cmap="rainbow")
ax_fig = ax.get_figure()
ax_fig.savefig("output.png")