import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')

print(df[['math score', 'reading score']])

x = df['math score']
y = df['reading score']

plt.plot(x,y)
plt.show()
