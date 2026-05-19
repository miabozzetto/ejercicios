import pandas as pd
df = pd.read_csv('users.csv')

print(df[['pais', 'edad']])

print(df.sort_values('edad'))

print(df[df['pais'] == 'Germany'].sort_values('edad', ascending=False).head(5))
