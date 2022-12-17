import h5py
import io
import pandas as pd
import numpy as np
from functions import remove_duplicates
def update_result(result, new_list):
    result = np.array([*result, new_list])
    return result

result = np.array([])
with h5py.File('data_2022_10_16.hdf', 'r') as f:
    print(list(f['GPS_1']['columns']))
    utc = np.array(f['GPS_1']['data'][::])
    utc = remove_duplicates(utc)
    utc_gps = []
    for i in range(0, len(utc)):
        utc_gps.append(utc[i][1])

df = pd.DataFrame({'Время': utc_gps})
df.to_csv('time.csv', index=False)
print('ok')