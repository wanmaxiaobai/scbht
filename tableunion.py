import pandas as pd
'''
不同类别是否包含特征值的数据个数分布
   1#  1*  10#  10*  11#  11*  12#  12*  ...  92*  93#  93*  94#  94*  t#  t*  id
1  22   0   19    3   20    2   20    2  ...   22    0   22    0   22  22   0   0
2  30   0   22    8   29    1   29    1  ...   30    0   30    0   30  30   0   1
3  24   0   24    0   24    0   24    0  ...   24    0   24    0   24  24   0   2
4  26   0   25    1   26    0   26    0  ...   26    0   26    0   26  26   0   3
5  26   0   26    0   26    0   26    0  ...   25    1   25    1   25  26   0   4
'''
def tableunion(tables,typenum):
    tables = tables
    index = tables.index
    columns = tables.columns

    newcolumns = []
    str1 = '#'
    str2 = '*'
    for i in columns:
        s1 = i + str1
        s2 = i + str2
        newcolumns.append(s1)
        newcolumns.append(s2)

    newindex = typenum
    tableunion = pd.DataFrame(int(0), index=newindex, columns=newcolumns)
    tableunion['id'] = [str(i) for i in range(len(tableunion.index))]

    for j in range(0, len(columns)):
        for i in range(0, len(index)):
            t = str(tables.loc[index[i], 't'])
            if tables.loc[index[i], columns[j]] > 0:
                tableunion.loc[tableunion.index==t, newcolumns[j * 2]] = tableunion.loc[tableunion.index==t, newcolumns[j * 2]] + 1
            else:
                tableunion.loc[tableunion.index==t, newcolumns[j * 2 + 1]] = tableunion.loc[tableunion.index==t, newcolumns[j * 2 + 1]] + 1
    # print("不同类别是否包含特征值的数据个数分布")
    # print(tableunion)
    return tableunion
