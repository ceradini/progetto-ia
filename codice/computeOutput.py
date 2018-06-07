import pandas as pd # serve per leggere i file csv
import csv          # serve per scrivere su csv
import math         # serve per il NaN number

# dizionari con i dati dei dataset
reputazione={}
raccomandazione={}
casmin={}
newCasmin={}
newVincoliSoft={}
vincoliSoft={}
finale={}
readrep         = pd.read_csv('output/rep_bin.csv') # lettura del file csv contenente dati su reputazione
readrec=pd.read_csv('output/rec_bin.csv') # lettura del file csv contenente dati su raccomandazione
raccomandazioniFinaliDict={}

# preso il valore di raccomandazione e il punteggio di reputazione, applica il casmin per fondere i risultati in un'unica opinione binomiale
def casMin(punteggioA,punteggioB):
	if punteggioA['b']<=punteggioB['b']:
		# faccio lo swap
		temp=punteggioA
		punteggioA=punteggioB
		punteggioB=temp
	if punteggioB['u']>(punteggioA['b']-punteggioB['b']):
		punteggioB['u']=punteggioB['u']-(punteggioA['b']-punteggioB['b'])
		punteggioB['b']=punteggioA['b']
	else:
		punteggioB['b']=punteggioB['b']+punteggioB['u']
		punteggioB['u']=0.0
		punteggioA['b']=punteggioB['b']
	return punteggioA

# per ogni coppia utente/hotel del dataset di raccomandazione, prende il valore di reputazione per l'hotel e applica il casMin
def calcolaCasMin():
	for key,value in raccomandazione.items():
		str=key.split("/$/$/")
		hotel=str[1]
		casmin[key]=casMin(value,reputazione[hotel])

# preso il valore di raccomandazione e il punteggio di reputazione, applica i vincoli soft per fondere i risultati in un'unica opinione binomiale
def vincoliSoftAlg(punteggioA,punteggioB):
	rest={}
	rest['b']=punteggioA['b']+punteggioB['b']
	return rest

# per ogni coppia utente/hotel del dataset di raccomandazione, prende il valore di reputazione per l'hotel e applica i vincoli soft
def calcolaVincoliSoft():
	for key,value in raccomandazione.items():
		str=key.split("/$/$/")
		hotel=str[1]
		vincoliSoft[key]=vincoliSoftAlg(value,reputazione[hotel])

def raccomandazioniFinali():
	max=0
	for key,value in newCasmin.items():
		for k,v in value.items():
			for i,j in v.items():
				if j['b']>0.56:
					if key not in raccomandazioniFinaliDict.keys():
						raccomandazioniFinaliDict[key]={'listaHotel':[],'hotel':""}
					raccomandazioniFinaliDict[key]['listaHotel'].append(i)
	for key,value in newVincoliSoft.items():
		for k,v in value.items():
			max=-10000
			maxH=""
			for i,j in v.items():
				if max<j['b']:
					max=j['b']
					maxH=i
			if key not in raccomandazioniFinaliDict.keys():
				raccomandazioniFinaliDict[key]={'listaHotel':[],'hotel':""}
			raccomandazioniFinaliDict[key]['hotel']=maxH


# lettura dei dati dai dataset e scrittura nei dizionari
for index, row in readrep.iterrows():
    reputazione[row['hotel']]={'b':row['brep'],'d':row['drep'],'u':row['urep']}

for index, row in readrec.iterrows():
    raccomandazione[row['utente/$/$/hotel']]={'b':row['brec'],'d':row['drec'],'u':row['urec']}

calcolaCasMin()
calcolaVincoliSoft()

# scrittura di un dataset contenente i consigli dell'operatore casMin
with open('output/casmin.csv', 'w', encoding="utf-8") as csvfile:
    fieldnames = ['utente/$/$/hotel', 'b']
    writer     = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for key,value in casmin.items():
    	writer.writerow({'utente/$/$/hotel':key,'b':round(value['b'],2)})

# scrittura di un dataset contenente i consigli dati dai vincoli soft, viene raccomandato un hotel per utente
with open('output/vincoliSoft.csv', 'w', encoding="utf-8") as csvfile:
    fieldnames = ['utente/$/$/hotel', 'somma']
    writer     = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for key,value in vincoliSoft.items():
    	writer.writerow({'utente/$/$/hotel':key,'somma':round(value['b'],2)})

for key,value in casmin.items():
	k,v=key.split("/$/$/")
	if k not in newCasmin.keys():
		newCasmin[k]={'hotel':{}}
	newCasmin[k]['hotel'][v]=value

for key,value in vincoliSoft.items():
	k,v=key.split("/$/$/")
	if k not in newVincoliSoft.keys():
		newVincoliSoft[k]={'hotel':{}}
	newVincoliSoft[k]['hotel'][v]=value


raccomandazioniFinali()
print(raccomandazioniFinaliDict["A Traveler"])

