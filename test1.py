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
    utc_gps = np.array(f['GPS_1']['data'][::])
    utc_gps = remove_duplicates(utc_gps)

    for i in range(0, len(utc_gps)):
        print(i, ' ', utc_gps[i][1])