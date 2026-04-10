import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')

print(df[['gender', 'math score']].shape)

print(df[['gender', 'math score']].head(4))

print(df[['gender', 'math score']].tail(4))
