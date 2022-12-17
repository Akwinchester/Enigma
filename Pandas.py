import pandas as pd

# First DataFrame
df1 = pd.DataFrame({'Time': [100, 200, 300, 400], 'Speed': [33,44,55,56]}) #Первый фрейм - время с GPS датчика

# Second DataFrame
df2 = pd.DataFrame({'Time': [100, 200, 300],
                    'Amper1': [10, 20, 30]}) #Второй фрейм - если есть совпадение +-300мс


# appending multiple DataFrame
df3_merged = pd.merge(df1, df2, how='left')
print(df3_merged)
print(df3_merged.interpolate())