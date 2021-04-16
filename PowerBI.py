import csv
import pandas as pd 

dataset = pd.read_csv('data/2020-21/leagues/testfile.csv')

#	JAFFA TROPHY
# Bepalen welke speler uit de trophy valt op basis van hoogste punten aantal min hits
# TO-DO: Wat te doen bij een gelijke stand
# TO-DO: Inbouwen dat de for loop stopt op het moment dat de trophy is afgerond	
for index in range(4,len(dataset.columns)-2):
	x = dataset[dataset['Max_in_GW'] == 0].iloc[:,index].idxmax()
	dataset.iat[x,-2] = dataset.columns[index]
	dataset.iat[x,-1] = dataset.iat[x,index]

#	AFFOE CUP
# Bepalen welke spelers uit de cup vallen op basis van laagste aantal punten min hits
# TO-DO: Wat te doen bij een gelijke stand
GW = 38 - len(dataset.index) 
for index in range(GW,len(dataset.columns)-2):
	x = dataset[dataset['Min_in_GW'] == 0].iloc[:,index].idxmin()
	dataset.iat[x,-2] = dataset.columns[index]
	dataset.iat[x,-1] = dataset.iat[x,index]

