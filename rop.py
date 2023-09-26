'''
在验证集上找到第r个特征值分类效果最好用来下一步在测试集上使用
'''
def rop(table,lscolumnsybp):
    table = table
    lscolumnsybp = lscolumnsybp
    testtype = table['t'].values
    testtype = list(testtype)
    laccurac = []
    for i in lscolumnsybp:
        k = 0
        for j in range(0,len(i)):
            if str(i[j]) == str(testtype[j]):
                k = k+1
            # print(k)
        laccurac.append(k/len(i))
    # laccurac = laccurac.sort(reverse=True)
    # print(sorted(laccurac,reverse=True))
    # print(laccurac)
    return laccurac