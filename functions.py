import h5py
import io
import pandas as pd
import numpy as np

def update_result(result, new_list):
    result = np.array([*result, new_list])
    return result


def remove_duplicates(array):
    u, idx = np.unique(array, axis=0, return_index=True)
    array = u[idx.argsort()]
    return array