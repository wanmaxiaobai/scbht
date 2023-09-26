from datainpute import datainput
from KFold import kfold


if __name__ == '__main__':

    dataset = ['epitope','activity', 'aslbu', 'gene', 'pioneer', 'context', 'robot', 'auslan2', 'skating', 'unix', 'question',  'temprestboost']
    for i in dataset:
        dataframe, itemset = datainput('dataset/{}.txt'.format(i))
        dataframe.to_csv('dataset/{}_dataframe.csv'.format(i))

        typenum = dataframe['t'].values.tolist()
        typenum = sorted(list(set(typenum)))
        file = open('dataset/{}_typenum.txt'.format(i), 'w')
        file.write(','.join(typenum))

        file = open('dataset/{}_itemset.txt'.format(i),'w')
        file.write(','.join(itemset))
        file.close()

    datasettest = ['epitope','activity', 'aslbu', 'gene', 'pioneer', 'context']
    lsaccurac = []
    for i in datasettest:
        accurac = kfold(i,3)
        lsaccurac.append(accurac)
        print(i,accurac)

    for i in range(0, len(datasettest)):
        print(datasettest[i], lsaccurac[i])





