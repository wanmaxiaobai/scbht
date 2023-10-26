from scipy.stats import fisher_exact
import pandas as pd
def key_function(x):
    return x[1]
def fisher(tableunion):
    tableunion = tableunion
    columns = tableunion.columns
    index = tableunion.index
    lstableunion = []
    lslsp = []
    for j in index:
        lscolumns = []
        lsp = []
        tableunionj = tableunion[index == j]
        ntableunionj = tableunion.drop(index=j)
        ntableunionj = list(ntableunionj.sum(axis=0))
        ntableunionj = pd.DataFrame(ntableunionj)
        ntableunionj = ntableunionj.T
        ntableunionj.columns = columns
        dfs = [tableunionj, ntableunionj]
        result = pd.concat(dfs)
        #假设是某个类别的2*2表
        '''
            1# 1*  10# 10*  11# 11*  12# 12*  ...  92* 93#  93* 94#  94*   t# t*    id
            1   37  0   32   5   34   3   34   3  ...   37   0   37   0   37   37  0     0
            0  179  0  167  12  175   4  175   4  ...  178   1  178   1  178  179  0  1234
            
            [2 rows x 191 columns]
                1# 1*  10# 10*  11# 11*  12# 12*  ...  92* 93#  93* 94#  94*   t# t*    id
            2   45  0   35  10   42   3   42   3  ...   45   0   45   0   45   45  0     1
            0  171  0  164   7  167   4  167   4  ...  170   1  170   1  170  171  0  0234
            
            [2 rows x 191 columns]
                1# 1*  10# 10*  11# 11*  12# 12*  ...  92* 93#  93* 94#  94*   t# t*    id
            3   43  0   43   0   43   0   43   0  ...   43   0   43   0   43   43  0     2
            0  173  0  156  17  166   7  166   7  ...  172   1  172   1  172  173  0  0134
            
            [2 rows x 191 columns]
                1# 1*  10# 10*  11# 11*  12# 12*  ...  92* 93#  93* 94#  94*   t# t*    id
            4   44  0   42   2   43   1   43   1  ...   44   0   44   0   44   44  0     3
            0  172  0  157  15  166   6  166   6  ...  171   1  171   1  171  172  0  0124
            
            [2 rows x 191 columns]
                1# 1*  10# 10*  11# 11*  12# 12*  ...  92* 93#  93* 94#  94*   t# t*    id
            5   47  0   47   0   47   0   47   0  ...   46   1   46   1   46   47  0     4
            0  169  0  152  17  162   7  162   7  ...  169   0  169   0  169  169  0  0123
        '''

        # print(result)
        lstableunion.append(result)
        for i in range(0, len(columns)-3, 2):
            table = result[[columns[i], columns[i + 1]]]
            tabletwo = result[[columns[i + 1], columns[i]]]
            p1 = fisher_exact(table, alternative='greater')
            p2 = fisher_exact(tabletwo, alternative='greater')
            lsp.append(p1[1])
            lsp.append(p2[1])
            lscolumns.append(columns[i])
            lscolumns.append(columns[i+1])
            # lsp.append([columns[i][0:len(columns[i])-1], p1[1], p2[1], i])
        sorted_pairs = sorted(zip(lsp, lscolumns))
        sorted_list1, sorted_list2 = zip(*sorted_pairs)
        # lsp.sort(key=key_function)
        lslsp.append([sorted_list2, sorted_list1])
    # print(lslsp)
    '''
    p值列表
    ['1', [['1', 1.0, 1.0, 0], ['10', 0.8738066162708311, 0.33934119303203664, 2], ['11', 0.995488845144357, 0.07623851706036747, 4].......['93', 0.1796875, 1.0, 184], ['94', 0.1796875, 1.0, 186]]]
    '''
    return lstableunion, lslsp