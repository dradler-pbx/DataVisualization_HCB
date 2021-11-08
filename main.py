import pandas as pd
import numpy as np
import os

filepath = 'data'
parameterID = pd.read_excel('ParameterID.xlsx')


data = pd.DataFrame()
files = os.listdir(filepath)
firstrun = True

# check if files are of HCBLOKS device for data compression
hcb_files_flag = False
if files[0][0:7] == 'Log_HCB':
    hcb_files_flag = True


# read all files and append it to one single dataframe
for file in files:
    df = pd.read_csv(filepath+'\\'+file, sep=';', encoding='latin1')
    if file[0:6] == 'Logger':
        df = df.drop([0])
    if firstrun:
        data = df
        firstrun = False
    else:
        data = data.append(df)

# create new header with decoded filenames
new_header = []
for id in data.columns:
    if id in parameterID['ID(hex)'].values:
        id_clear = parameterID[parameterID['ID(hex)'] == id]['Custom name'].item()
    else:
        id_clear = id
    new_header.append(id_clear)
data.columns = new_header

# reduce data of HCBloks files (1 value per 10 entries)
if hcb_files_flag:
    data = data.groupby(np.arange(len(data))//10).mean()

data.to_csv('CombinedData.csv', index=False)
