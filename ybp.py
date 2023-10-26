import numpy as np
import pandas as pd
'''
根据fisher返回的p值列表，在验证集上生成对应的p值表
'''
def ybp(table, itemset, lslsp,typenum):
    lsybp = []
    table = table
    index = table.index
    columns = itemset
    typenum = typenum
    print(table)
    print(itemset)
    print(typenum)


    for i in lslsp:
        print(i[0])

    for rp in range(0, 2*len(itemset)):
        rps = []
        rpsp = []
        for i in lslsp:
            rps.append(i[0][rp])
            rpsp.append(i[1][rp])
        print(rps,rpsp)

        for i in index:
            print(table.loc[i])
            print(table.loc[i]['1'])
        #     for j in rps:
        #         print(j[:-1])
        #         print(j[-1])











    return 0

