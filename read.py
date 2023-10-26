import pandas as pd
class read:
    def __init__(self, filename):
        self.name = filename

    def readcsv(self):
        dataframe = pd.read_csv('dataset/{}_dataframe.csv'.format(self.name))
        return dataframe

    def readitem(self):
        file = open('dataset/{}_itemset.txt'.format(self.name), 'r')
        item = file.readline()
        file.close()
        return item.split(',')

    def readtypenum(self):
        file = open('dataset/{}_typenum.txt'.format(self.name), 'r')
        typenum = file.readline()
        file.close()
        return typenum.split(',')