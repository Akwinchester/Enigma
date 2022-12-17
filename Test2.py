import h5py
import numpy as np

with h5py.File('.\data_2022_10_16.hdf', 'r') as f:
    gps = np.array(f['GPS_1']['data'][::])
    print(f.keys())
