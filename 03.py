import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')

print(df[['gender', 'race/ethnicity', 'parental level of education']].head(10))
