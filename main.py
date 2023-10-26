from datainpute import datainput
from KFold import kfold

if __name__ == '__main__':

    dataset = ['activity', 'aslbu','auslan2','context','epitope','gene','news','pioneer','question','reuters', 'robot', 'skating', 'temprestboost','unix','webkb' ]
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

    datasettest = ['activity', 'aslbu','auslan2','context','epitope','gene','pioneer', 'question', 'reuters', 'robot', 'skating', 'temprestboost', 'unix', 'webkb']
    datasettest = ['activity']
    lsaccurac = []
    for i in datasettest:
        accurac = kfold(i,5)
        lsaccurac.append(accurac)
        print(i,accurac)

    for i in range(0, len(datasettest)):
        print(datasettest[i], lsaccurac[i])





