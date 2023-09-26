import pandas as pd
from tables import table
from tableunion import tableunion
from fisher import fisher
from train import train
from ybp import ybp
from rop import rop
from read import read
from testp import testp
from sklearn.model_selection import KFold, train_test_split

def kfold(filename,k):
    df = read(filename).readcsv()
    itemset = read(filename).readitem()
    typenum = read(filename).readtypenum()
    X = df['d']
    y = df['t']
    kf = KFold(n_splits=k, shuffle=True, random_state=42)
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
        tab = table(df_train, itemset)
        tabunion = tableunion(tab,typenum)
        p = fisher(tabunion)
        # train(p[1],i)
        tabyz = table(df_yz, itemset)
        tabtest = table(df_test,itemset)
        lscolumnsybp = ybp(tabyz,itemset,p[1],typenum)
        # print(lscolumnsybp)

        ac = rop(tabyz,lscolumnsybp)
        #每次检验验证机在不同特征值的额准确率
        maxval = max(ac)
        maxindex = ac.index(maxval)
        # print(ac,maxindex)

        lscolumnstestp = testp(tabtest,itemset,p[1],typenum)[maxindex]
        # print(lscolumnstestp)

        k = 0
        ltestaccurac = []
        for i in  range(0,len(lscolumnstestp)):
            if str(lscolumnstestp[i]) == str(tabtest['t'].values[i]):
                k = k+1
        testac = k/len(lscolumnstestp)

        lstestac.append(testac)
    # print(lstestac)

    ans = 0
    for i in lstestac:
        ans = ans+i

    return ans/len(lstestac)
