import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')

print(df['math score'])

print(df.sort_values('math score'))

print(df.sort_values('math score', ascending=False))
