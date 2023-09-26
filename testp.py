import numpy as np
import pandas as pd
'''
根据验证集找到的特征值分类计算分类准确率
'''
def testp(table, itemset, lslsp,typenum):
    lsybp = []
    table = table
    index = table.index
    columns = itemset
    typenum = typenum
    for n in range(0, len(typenum)):
        tables = np.array(table)
        for j in range(0, len(columns)):
            for i in range(0, len(index)):
                if tables[i][j] > 0:
                    tables[i][j]= lslsp[2*n+1][j][1]
                else:
                    tables[i][j] = lslsp[2*n+1][j][2]
        t = tables
        # print(t)
        lsybp.append(t)
    # print(lsybp)


    mintype = ''
    lscolumnsybp = []
    for j in range(0,len(columns)):
        lstypenump = []
        for i in range(0,len(index)):
            min = 1
            for n in range(0, len(typenum)):
                if lsybp[n][i][j] <= min:
                    min = lsybp[n][i][j]
                    mintype = typenum[n]
            lstypenump.append((mintype))
        lscolumnsybp.append(lstypenump)
        # print(lstypenump)
    # print(lscolumnsybp)

    return lscolumnsybp

