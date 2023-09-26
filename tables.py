import pandas as pd
import numpy as np
'''
['1', '2', '3', '4', '5']
是否包特征值表
                                                        1    10  ...   94  t
d                                                                ...        
11 15 19 20 17 3 5 55 31 35 56 53 32 36 29 33 4...   14.0   0.0  ...  0.0  2
11 15 19 20 3 5 17 55 56 53 12 16 9 10 13 14 11...   24.0   2.0  ...  0.0  4
11 15 19 3 5 20 17 49 31 32 29 50 51 55 56 53 5...   24.0   1.0  ...  0.0  1
19 3 75 76 4 5 6 20 1 2 7 8 17 3 5 51 55 56 53 ...   28.0   3.0  ...  0.0  4
11 15 19 3 49 5 20 17 50 51 55 56 53 52 49 50 5...   16.0   1.0  ...  0.0  2
...                                                   ...   ...  ...  ... ..
11 15 19 71 72 49 3 20 5 17 50 51 55 31 35 56 5...   43.0   4.0  ...  0.0  3
11 15 19 3 5 20 17 31 49 50 32 51 43 52 44 49 4...   20.0   1.0  ...  0.0  4
11 15 19 3 5 20 17 55 56 53 54 55 56 49 53 23 2...   20.0   1.0  ...  0.0  1
11 15 19 20 3 17 5 55 31 35 56 53 36 32 29 12 1...  106.0  12.0  ...  0.0  3
11 15 19 3 5 20 17 49 43 47 44 48 4 6 1 7 12 16...   21.0   2.0  ...  0.0  4
'''
def table(data,itemset):
    data = data
    index = data.loc[:, 'd']
    columns = itemset

    lencolumns = len(columns)
    lenindex = len(index)

    tables = pd.DataFrame(np.zeros(lencolumns * lenindex).reshape(lenindex, lencolumns),index =index,columns =columns,)
    tables.columns = columns
    tables.index = index

    # 原滑动窗口计算字串的数量
    for i in range(0, len(index)):
        for j in range(0, len(columns)):
            for k in range(0, len(index[i]) - len(columns[j])):
                if columns[j] == index[i][k:k + len(columns[j])]:
                    tables.loc[index[i], columns[j]] = tables.loc[index[i], columns[j]] + 1
    tables['t'] = data.loc[:, 't'].values.tolist()
    # print("是否包特征值表")
    # print(tables)
    return tables