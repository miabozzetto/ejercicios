import pandas as pd
df=pd.read_csv('StudentsPerformance (2).csv')
print(df[['gender','math score']])
print(df.head(8))
print(df.tail(4))
print(df.dtypes)
print(df.shape)
print(df.count())
