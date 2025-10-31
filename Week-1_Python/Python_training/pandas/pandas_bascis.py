import nt

import pandas as pd


data=[1,2,3,4,5,6]
print(data)
series = pd.Series(data)
print(series)


data={
    'Name':['Omkar','fefe','dsad','sdsac'],
    'Age':[22,34,24,22],
    'City':['Hyd','Hyd','asda','SDsa']
}
df=pd.DataFrame(data)
print(df)

print('desc  \n',df.describe())

print(df['Name'])
print(df[['Name','City']])

print(df[df['Age']>30])
