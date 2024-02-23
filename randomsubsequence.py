import random
import math
from tables import table
from tableunion import tableunion
from fisher import fisher
def randomsubsequence(datatrain,zxln):
    n = zxln
    data = datatrain
    data = data['d'].values.tolist()
    ls = []
    kn = 0
    for i in data:
        sl = i.split()
        if(len(sl)<n):
            continue
        start_index = random.randint(0, len(sl)-n)
        random_subsequence = sl[start_index: start_index + n]
        s = ' '.join(random_subsequence)
        # print(s)
        ls.append(s)
    return list(set(ls))


def generate_random_strings(df_train, df_yz, typenum):
    data = df_train
    data = data['d'].values.tolist()
    datalen = len(data)
    k = round(math.sqrt(len(data)))*4

    random_elements = random.sample(data, k)
    ls = []
    for i in random_elements:
        sl = i.split()
        lenstr = round(math.sqrt(len(sl)))
        substring_length = random.randint(1, lenstr)
        # 随机选择截取的起始位置
        start_index = random.randint(0, len(sl) - substring_length+1)
        result = sl[start_index: start_index + substring_length]
        s = ' '.join(result)
        # print(s)
        ls.append(s)

    itemset = list(set(ls))
    tabyz = table(df_yz, itemset)
    tableunionyz = tableunion(tabyz, typenum)
    p = fisher(tableunionyz)

    lss = []
    for i,j in p[1]:
        for k in range(0, round(math.sqrt(len(i)))):
            lss.append(i[k][:-1])

    # print('提取出', list(set(lss)))
    return list(set(lss))


def n_generate_random_strings(df_train, df_yz, typenum, n):
    lsitemset = []
    for i in range(0, n):
        itemset = generate_random_strings(df_train, df_yz, typenum)
        lsitemset.extend(itemset)

    return list(set(lsitemset))
