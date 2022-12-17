import h5py
import io
import pandas as pd
import numpy as np

result = np.array([])

def  create_time(d1):
    time = d1[0]//1000
    time = time * 1000 + 500
    return time

def create_row(d1, d2, d3,i):
    row = []
    time = create_time(d1[i])
    row.append(time-500)
    if  time-500 < d1[i][0] and time+500 > d1[i][0]:
        row.append(d1[i][1])
    else:
        row.append(d1[i-1][1])
    if abs(time - d2[i][0]) < 1000:
        row.append(d2[i][1])
    else:
        row.append(d2[i-1][1])
    if abs(time - d3[i][0]) < 1000:
        row.append(d3[i][1])
    else:
        row.append(d3[i-1][1])
    return row






with h5py.File('.\data_2022_10_16.hdf', 'r') as f:
    d1 = np.array(f['FrontCart.reducer.1.phase_1']['data'][:10:])

    d2 = np.array(f['FrontCart.reducer.1.phase_1']['data'][:10:])

    d3 = np.array(f['FrontCart.reducer.1.phase_1']['data'][:10:])
    print(1)

    for i in range(0,len(d1)):
        result = np.array([*result, create_row(d1, d2, d3, i)])
    print(result)
    print('первый фор')
    df = pd.DataFrame(result, columns=['Время', 'Ток1', 'Ток2', 'Ток3'])
    df.to_csv('До.csv', index=False)
    count = 0
    for i in range(1, len(result)):
        i = i - count
        if result[i-1][0] == result[i][0]:
            result[i - 1][1] = (result[i - 1][1] + result[i][1])/2
            result[i - 1][2] = (result[i - 1][2] + result[i][2]) / 2
            result[i - 1][3] = (result[i - 1][3] + result[i][3]) / 2
            result.pop(i)
            count +=1
    print('второй фор')


    df = pd.DataFrame(result, columns=['Время', 'Ток1', 'Ток2', 'Ток3'])
    df.to_csv('После.csv', index=False)

#
# df = pd.DataFrame({'Время': time, 'Ток1': toc1})
# df.to_csv('proba.csv')

# with open('./2022-10-20_13-30-30_401.bin', 'rb') as f:
#     x = f.read()
#     # x = b'\xc9MQc\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\xb6\x00\x00\x00\x00\x00\x00\x000.3.11\x00\x00D7290CD5A347/106/RUr2\x00\x00\x00\n\r\r\xa7\xdc\x97\xf5\x83\x01\x00\x00(\xd9\x97\xf5\x83\x01\x00\x00\x92Z'
#     print(x.decode('cp855'))


