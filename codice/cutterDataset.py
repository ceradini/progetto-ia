import pandas as pd # serve per leggere i file csv
import csv          # serve per scrivere su csv
import math         # serve per il NaN number


utenti        = {}
utenti_validi = []                              # memorizzo qui gli utenti che sono validi secondo i limiti imposti
read          = pd.read_csv('source/hotel.csv') # lettura del file csv contenente dati su moltissimi hotel
L             = 3                               # limite inferiore minimo di voti per tenere un utente nel dataset

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

# popolo l'array di utenti validi secondo i limiti imposti
for key,value in utenti.items():
	if value['numeroVoti'] >= L:
		utenti_validi.append(key)

# creo una copia del dataset tenendo solo gli utenti validi
with open('source/hotel_reduced.csv', 'w') as csvfile:
    fieldnames = ['address','categories','city','country','latitude','longitude','name','postalCode','province','reviews.date','reviews.dateAdded','reviews.doRecommend','reviews.id','reviews.rating','reviews.text','reviews.title','reviews.userCity','reviews.username','reviews.userProvince']
    writer     = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for index, row in read.iterrows():
    	if row['reviews.username'] in utenti_validi:
    		new_row = {
				'address':row['address'],
				'categories':row['categories'],
				'city':row['city'],
				'country':row['country'],
				'latitude':row['latitude'],
				'longitude':row['longitude'],
				'name':row['name'],
				'postalCode':row['postalCode'],
				'province':row['province'],
				'reviews.date':row['reviews.date'],
				'reviews.dateAdded':row['reviews.dateAdded'],
				'reviews.doRecommend':row['reviews.doRecommend'],
				'reviews.id':row['reviews.id'],
				'reviews.rating':row['reviews.rating'],
				'reviews.text':row['reviews.text'],
				'reviews.title':row['reviews.title'],
				'reviews.userCity':row['reviews.userCity'],
				'reviews.username':row['reviews.username'],
				'reviews.userProvince':row['reviews.userProvince']
    		}
    		writer.writerow(new_row)








