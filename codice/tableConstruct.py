import pandas as pd # serve per leggere i file csv
import csv          # serve per scrivere su csv
import math         # serve per il NaN number

# dizionari necessari per il funzionamento del programma
reputazione  = {}
multinomiale = {}
binomiale    = {}
read         = pd.read_csv('hotel.csv') # lettura del file csv contenente dati su moltissimi hotel

W = 2 # costante necessaria ed è uguale a 2 perché indicato da slides

# funzione di sommatoria: esegue una sommatoria da init a end degli elementi sul dizionario passato
def summm(init, end, toSum):
	summ=0
	for i in range(init,end):
		summ=summ+toSum["x"+str(i)]
	return summ

# funzione di sommatoria 2: esegue una sommatoria da init a end degli elementi sul dizionario passato, questa sommatoria 
# è particolare, infatti è presa dalla equazione 4 del nostro paper
def summBin(init,end,bi):
	summ=0
	for i in range(init,end):
		summ=summ+bi["b"+str(i)]*((i)/(end-1))
	return summ

# calcola l'opinione multinomiale per tutti gli hotel del dataset prendendo in input i punteggi di reputazione degli stessi
def calcolaMultinomiale(chiave,multi,dizionario):
	somma=summm(0,10,multi)
	somma=W+somma
	for i in range(0,10):
		dizionario[chiave]["b"+str(i)]=round(multi["x"+str(i)]/(somma),2)
	dizionario[chiave]["u"]=round(W/somma,2)

# calcola l'opinione binomiale per tutti gli hotel del dataset prendendo in input le opinioni multinomiali degli stessi
def calcolaBinomiale(chiave,multi,dizionario):
	dizionario[chiave]["u"]=multi['u']
	for i in range(0,10):
		dizionario[chiave]["b"]=round(summBin(0,10,multi),2)
		dizionario[chiave]["d"]=round(1-dizionario[chiave]["b"]-dizionario[chiave]["u"],2)

#creazione dei dizionari per ospitare i punteggi di reputazione sul dataset
for index, row in read.iterrows():
    reputazione[row['name']]={'x0':0,'x1':0,'x2':0,'x3':0,'x4':0,'x5':0,'x6':0,'x7':0,'x8':0,'x9':0,'x10':0,'NaN':0}

# estrapolazione dei punteggi di reputazione dal dataset
for index, row in read.iterrows():
	if math.isnan(row['reviews.rating']):
		reputazione[row['name']]['NaN']+=1
	else:
		reputazione[row['name']]["x"+str(int(row['reviews.rating']))]+=1


# trasformazione dei punteggi di reputazione in opinioni multinomiali
for key,value in reputazione.items():
	multinomiale[key]={'b0':0,'b1':0,'b2':0,'b3':0,'b4':0,'b5':0,'b6':0,'b7':0,'b8':0,'b9':0,'b10':0,'u':0}

for key,value in reputazione.items():
	calcolaMultinomiale(key,value,multinomiale)

# trasformazione di opinioni multinomiali in binomiali
for key,value in multinomiale.items():
	binomiale[key]={'b':0,'d':0,'u':0}

for key,value in multinomiale.items():
	calcolaBinomiale(key,value,binomiale)

# salvataggio su csv dei risultati
with open('rep_bin.csv', 'w') as csvfile:
    fieldnames = ['hotel', 'b', 'd', 'u']
    writer     = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for key,value in binomiale.items():
    	writer.writerow({'hotel':key,'b':value['b'],'d':value['d'],'u':value['u']})

