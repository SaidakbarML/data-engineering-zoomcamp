import sys 
import pandas as pd 
print('argument ',sys.argv)
month = int( sys.argv[1])

df=pd.DataFrame({
    'day':[1,2],
    'num passengers':[3,4]
})
df['month'] = month
print(df.head())
print (f'hello world month {month}')

