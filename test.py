import csv
import pandas as pd 

dataset = pd.read_csv('data/2020-21/leagues/testfile.csv')

#for index in range(2,len(dataset.columns)):
#ranks = dataset.rank(axis=0,method='dense', ascending=False).astype(int)
#teamIDarray = list(set(dataset['team_id']))
#print(teamIDarray)

# copyData = dataset

# Start in gameweek
for index in range(4,len(dataset.columns)-2):
	x = dataset[dataset['Max_in_GW'] == 0].iloc[:,index].idxmax()
	dataset.iat[x,-2] = dataset.columns[index]
	dataset.iat[x,-1] = dataset.iat[x,index]

print(dataset)