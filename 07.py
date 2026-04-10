import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')

print(df[['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course', 'math score', 'reading score']])

print(df.head(7))

print(df.shape)

print(df.count())

print(df.tail(2))
