import pandas as pd
import numpy as np
import datetime
import os

photo_directory = 'C:/Users/320100141/Desktop/Python Venv/VisionAI/Processed Photos'

df = pd.read_csv(r'C:\Users\320100141\Desktop\Python Venv\VisionAI\raw.csv', skiprows=[1])
df = df.drop(df.columns[0], axis=1)
df = df.T

rows = df.apply(lambda x: x.tolist(), axis=1)

cpt = sum([len(files) for r, d, files in os.walk(photo_directory)])

ar_temp = np.zeros((cpt,3))
ar = np.zeros((int(cpt/3),9))

i = 0
j = 0
k = 0

while i < len(rows[0]):
    i = i + 1
    if len(rows[0]) == i:
        break

    elif rows[0][i-1] != rows[0][i]:
        k = k + 1
        j = 0

    elif rows[0][i-1] == rows[0][i]:
        j = j + 1
        ar_temp[k][j-1] = rows[1][i-1]
        ar_temp[k][j] = rows[1][i]

ar = ar_temp.reshape(int(cpt/3),9)

current_date = datetime.datetime.now()
filename = 'Scratch results of '+str(current_date.day)+'-'+str(current_date.month)+'-'+str(current_date.year)

pd.DataFrame(ar).to_csv(str(filename + '.csv'))

print("Post-processing complete.")