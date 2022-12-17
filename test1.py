import h5py
import io
import pandas as pd
import numpy as np

def update_result(result, new_list):
    result = np.array([*result, new_list])
    return result

result = np.array([])
with h5py.File('.\data_2022_10_16.hdf', 'r') as f:
    print(list(f['GPS_1']['columns']))
    utc_gps = np.array(f['GPS_1']['data'][:200:])
    u, idx = np.unique(utc_gps, axis=0, return_index=True)
    utc_gps = u[idx.argsort()]
    for i in range(0, len(utc_gps)):
        print(i, ' ', utc_gps[i][0], ' ', utc_gps[i][1])