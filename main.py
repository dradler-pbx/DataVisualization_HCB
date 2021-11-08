import pandas as pd
import os

filepath = 'data\HCB'
parameterID = pd.read_excel('ParameterID.xlsx')


data = pd.DataFrame()
files = os.listdir(filepath)

for file in files:
    df = pd.read_csv(filepath+'\\'+file, sep=';')
    data.merge(df, on='title')

new_header = []
for id in data.columns:
    id_clear = parameterID[parameterID['ID(hex)']==id]['Custom name']
    new_header.append(id_clear)

data.columns = new_header