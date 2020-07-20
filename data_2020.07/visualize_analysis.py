%matplotlib inline
import pandas as pd
df = pd.read_csv('data/broadcast.csv', index_col = 0)
df.plot(kind = 'line') # default
df.plot(y = 'KBS')
df.plot(y = ['KBS', 'JTBC'])
df[['KBS', 'JTBC']].plot()
df['KBS'].plot()

df.loc[2017].plot(kind = 'pie')

df = pd.read_csv('data/sports.csv', index_col = 0)
df.plot(kind = 'bar')
df.plot(kind = 'barh')
df.plot(kind = 'bar', stacked = True)
df['Female'].plot(kind = 'bar')

df = pd.read_csv('data/body.csv', index_col = 0)
df.plot(kind = 'hist', y = 'Height', bins = 15)

