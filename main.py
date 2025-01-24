import pandas as pd

df = pd.read_csv('master.csv',header=0)

df.iloc[-1,0] = 'acbc0144'
# print(df.iloc[-1,0])
print(df)

df.to_csv('master.csv',index=False)