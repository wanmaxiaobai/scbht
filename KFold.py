import pandas as pd
from read import read
from tables import table, extendtable
from tableunion import tableunion
from fisher import fisher
from ybp import ybp
from textp import testp
from sklearn.model_selection import KFold, train_test_split

from prefix import pfspan
from randomsubsequence import randomsubsequence,generate_random_strings,n_generate_random_strings
from stringconcate import stringconcate

def kfold(filename,k):
    df = read(filename).readcsv()
    itemset = read(filename).readitem()
    typenum = read(filename).readtypenum()

    X = df['d']
    y = df['t']
    kf = KFold(n_splits=k, shuffle=True, random_state=52)
    i = 0
    lsac = []
    lstestac = []
    for fold, (train_index, test_index) in enumerate(kf.split(X)):
        i = i+1
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

        df_train = {
            'd':list(X_train),
            't':list(y_train)
        }
        df_yz = {
            'd':list(X_val),
            't':list(y_val)
        }
        df_test = {
            'd': list(X_test),
            't': list(y_test)
        }

        df_train = pd.DataFrame(df_train)
        df_test = pd.DataFrame(df_test)
        df_yz = pd.DataFrame(df_yz)

        # '''
        # 频繁子序列
        # '''
        # itemset = pfspan(df_train)
        # print('频繁子序列长度',len(itemset), itemset)
        # '''
        # 每条数据随机截取定长子序列
        # '''
        # itemset = randomsubsequence(df_train,2)
        # print(len(itemset),itemset)
        # '''
        # 随机生成子序列
        # '''
        number_of_zxl = 8
        itemsets = n_generate_random_strings(df_train, df_yz, typenum, number_of_zxl)
        # print('kfold',len(itemset),itemset)


        lslsip = []
        for itemset in itemsets:
            # print('随机提取子序列长度',len(itemset))
            tab = table(df_train, itemset)
            tabunion = tableunion(tab,typenum)
            p = fisher(tabunion)
            lsip = []
            for ip in p[1]:
                lsip.append(ip[0][0][:-1])
            lslsip = list(set(lslsip + lsip))
        print('最终合并的子序列长度', len(lslsip))

        itemset = lslsip
        itemset = stringconcate(lslsip,1,2)

        tab = table(df_train, itemset)
        itemset = tab.columns.tolist()[:-1]
        tabunion = tableunion(tab, typenum)

        p = fisher(tabunion)
        # print(p)
        tabyz = table(df_yz, itemset)
        # print(tabyz)
        tabtest = table(df_test,itemset)
        maxacr,maxr = ybp(tabyz, itemset, p[1], typenum)

        testacr = testp(tabtest, itemset, p[1], typenum, maxr)
        lstestac.append(testacr)

    ans = 0
    for i in lstestac:
        ans = ans+i

    return ans/len(lstestac)
