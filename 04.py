import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')

print(df[['writing score']].tail(8))
