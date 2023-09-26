import pandas as pd

def datainput(filepath):
    file = open(filepath)
    data  = []
    db = []
    data_label = []
    itemset = []
    for i in file:
        temp = i.replace("\n", "").split("\t")
        data.append(temp[1])
        seq_db = temp[1].split(" ")
        db.append(seq_db)
        data_label.append(str(temp[0]))
    # unique itemset
    itemset = set([item for sublist in db for item in sublist])
    itemset = list(itemset)
    int_itemset = [str(x) for x in itemset]
    int_itemset.sort()
    itemset = [str(x) for x in int_itemset]

    dataframe = {
        'd': data,
        't':data_label
    }
    dataframe = pd.DataFrame(dataframe)
    dataframe = dataframe.drop_duplicates(subset=['d'], keep=False)

    return dataframe,itemset


