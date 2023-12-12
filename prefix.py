from typing import List
from prefixspan import PrefixSpan
from read import read
import pandas as pd
import numpy as np
def pfspan(datatrain):

    data = datatrain

    grouped = data.groupby('t')
    # 将每个分组转化为单独的DataFrame
    result = [group for _, group in grouped]
    # 输出划分后的多个小DataFrame
    lspfspan = []
    for df_group in result:
        ls = []
        for i in df_group['d']:
            ls.append(i.split())
        lspfspan.append(ls)

    ls = []
    for i in lspfspan:
        ps = PrefixSpan(i)

        n = ps.topk(32)
        ls.append(n)

    lscolumns: list[str] = []
    for i in ls:
        for j in i:
            lscolumns.append(" ".join(j[1]))

    print((set(lscolumns)))
    return list(set(lscolumns))