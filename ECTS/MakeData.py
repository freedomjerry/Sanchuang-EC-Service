import pandas as pd
import numpy as np

np.set_printoptions(threshold=np.inf)
data = np.random.randint(0, 10, 10000)
# print(data)
label = np.empty((9900, 1), int)
result = np.empty((9900, 1), int)
content = np.empty((9900, 30), int)
for i in range(9900):
    data1 = np.empty(30)
    data1 = data[i: i+30]
    # print(type(data1[0]))
    data2 = np.empty(7)
    data2 = data[i+30: i+37]
    # print(data2, data2.shape)
    month = data1.mean()
    nextweek = data2.mean()
    if month >= nextweek:
        if month >= nextweek * 1.5:
            label[i] = [1]
        else:
            label[i] = [0]
    else:
        if nextweek >= month * 1.5:
            label[i] = [1]
        else:
            label[i] = [0]

    content[i] = data1
    # print(type(content[0][0]))
result = np.hstack((label, content)).astype(int)
res = pd.DataFrame(result)
res.to_csv('sell.txt', index=False, sep=',')
