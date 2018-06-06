import pandas as pd # serve per leggere i file csv
import csv          # serve per scrivere su csv
import math         # serve per il NaN number

# dizionari necessari per il funzionamento del programma
reputazione  = {}
multinomiale = {}
binomiale    = {}
utenti       = {}
read         = pd.read_csv('source/hotel.csv') # lettura del file csv contenente dati su moltissimi hotel

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

# funzione che ricava tutti gli utenti che hanno votato uno specifico hotel dato l'hotel e un utente, deve restituire un dizionario
def calcoloVicinato(utente,hotelVotato):
	vicinato=[]
	for key,value in utenti.items():
		if key != utente:
			if hotelVotato in utenti[key]['hotelVotati']:
				vicinato.append(key)
	return vicinato

# ritorna la dimensione di un vicinato passato
def vicinatoDim(vicinato):
	return len(vicinato)

# ritorna il punteggio medio dato dall'utente
def punteggioMedioUtente(utente):
	return utenti[utente]['media']

# Ritorna il punteggio dato da utente a hotel. Se sono presenti più voti dati da un utente allo stesso hotel, allora viene restituito quello medio
def punteggioUtenteHotel(utente,hotel):
	punteggio=0.0
	numeroVoti=0
	for index, row in read.iterrows():
		if utente==row['reviews.username']:
			if hotel==row['name']:
					if not(math.isnan(row['reviews.rating'])):
						punteggio+=row['reviews.rating']
						numeroVoti+=1
	return round(punteggio/numeroVoti)

# ritorna una lista con gli hotel votati sia da utente1 che da utente2
def hotelVotatiDaUtenti(utente1,utente2):
	hotel=[]
	lista1=utenti[utente1]['hotelVotati']
	lista2=utenti[utente2]['hotelVotati']
	for i in range(len(lista1)):
		if lista1[i] in lista2:
			hotel.append(lista1[i])
	return hotel

# cacola il numero di hotel votati in comune tra i due utente passati
def numeroHotelVotatiInComune(utente1,utente2):
	return len(hotelVotatiDaUtenti(utente1,utente2))

# calcola la somiglianza tra utente1 e utente2. N.B. Questo calcolo è molto complesso e richiede molto tempo
def somiglianza(utente1,utente2):
	hotel=hotelVotatiDaUtenti(utente1,utente2)
	# calcolo del numeratore della formula e degli operandi del denominatore
	numeratore=0.0
	operando1=0.0
	operando2=0.0
	for i in range(len(hotel)):
		numeratore+=((punteggioUtenteHotel(utente1,hotel[i])-punteggioMedioUtente(utente1))*(punteggioUtenteHotel(utente2,hotel[i])-punteggioMedioUtente(utente2)))
		operando1+=(punteggioUtenteHotel(utente1,hotel[i])-punteggioMedioUtente(utente1))**2
		operando2+=(punteggioUtenteHotel(utente2,hotel[i])-punteggioMedioUtente(utente2))**2
	# calcolo denominatore
	denominatore=0.0
	denominatore=operando1*operando2
	denominatore=math.sqrt(denominatore)
	if denominatore==0.0:
		return 0.0
	else:
		# calcolo della somiglianza
		return round(numeratore/denominatore,2)

# calcola la predizione dell'utente utente per l'hotel hotel
def predizione(utente,hotel):
	predizione=punteggioMedioUtente(utente)
	predizione/=10 # per normalizzare il voto che se fosse di media 10 allora viene 0.1 se no viene troppo alto e supera 1 già il punteggio
	print(predizione)
	vicinato=calcoloVicinato(utente,hotel)
	k=1/vicinatoDim(vicinato) # fattore di normalizzazione
	operando2=0.0
	for i in range(len(vicinato)):
		operando2+=((somiglianza(utente,vicinato[i]))*(punteggioUtenteHotel(vicinato[i],hotel)-punteggioMedioUtente(vicinato[i])))
	if operando2==0.0:
		return 0.0 # in questo caso significa che la somiglianza è zero e se gli utenti non si assomigliano non ha senso fare la raccomandazione fasandosi solo sul punteggio dato dall'utente
	else:
		predizione+=k*operando2
		return round(predizione,2)

# calcola l'opinione binomiale del valore di raccomandazione per l'utente u sull'hotel j
def binomialeUtenteHotel(utente,hotel):
	binomiale={'b':0.0,'d':0.0,'u':0.0}
	somma=0.0
	vicinato=calcoloVicinato(utente,hotel)
	for i in range(len(vicinato)):
		somma+=numeroHotelVotatiInComune(utente,vicinato[i])
	binomiale['u']=round(W/(W+somma),2)
	binomiale['b']=round(77.31-binomiale['u'],2) #predizione(utente,hotel)
	binomiale['d']=round(1-binomiale['b']-binomiale['u'],2)
	return binomiale

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

'''
# salvataggio su csv dei risultati
with open('output/rep_bin.csv', 'w') as csvfile:
    fieldnames = ['hotel', 'b', 'd', 'u']
    writer     = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for key,value in binomiale.items():
    	writer.writerow({'hotel':key,'b':value['b'],'d':value['d'],'u':value['u']})
'''
# calcolo del punteggio medio per utente
for index, row in read.iterrows():
    utenti[row['reviews.username']]={'punteggio':0, 'numeroVoti':0, 'media':0.0, 'hotelVotati':[]}

# estrapolazione dei punteggi di reputazione dal dataset
for index, row in read.iterrows():
	if not(math.isnan(row['reviews.rating'])):
		utenti[row['reviews.username']]['punteggio']+=row['reviews.rating']
		utenti[row['reviews.username']]['numeroVoti']+=1
		if row['name'] not in utenti[row['reviews.username']]['hotelVotati']:
			utenti[row['reviews.username']]['hotelVotati'].append(row['name']) # mi serve per i calcoli futuri, per scoprire i vari vicinati degli utenti
	
# calcolo del punteggio medio per ogni utente
for key,value in utenti.items():
	if value['numeroVoti']!=0:
		value['media']=round(value['punteggio']/value['numeroVoti'],2)
	else:
		value['media']=0.0

print(predizione("A Traveler","Hotel Russo Palace"))







