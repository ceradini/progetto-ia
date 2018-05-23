# Introduzione

## Sistemi di raccomandazione

Su Internet la quantità di informazioni è travolgente e continuamente in aumento, questo ha reso impossibile l'accesso tempestivo a elementi e informazioni di interesse su Internet. I sistemi di recupero delle informazioni (ad esempio i motori di ricerca) hanno parzialmente risolto il problema ma priorità e personalizzazione (mappare i contenuti disponibili per gli interessi e le preferenze dell'utente) di informazioni erano assenti.

Per tale motivo sono stati introdotti i sistemi di raccomendazione. I *Sistemi di Raccomandazione* sono sistemi di filtraggio di informazioni correlate alle preferenze dell'utente, l'interesse o al comportamento osservato su di esso rispetto alla grande quantità di informazioni. Questi sistemi hanno la capacità di prevedere se un determinato utente preferirebbe un articolo o meno in base al profilo dell'utente.

I sistemi di raccomandazione portano dei vantaggi sia agli utenti, mostrando informazioni di interesse, sia per i fornitori di servizi perché riducono i costi di transazione per la ricerca, selezione di articoli in ambiente di shopping online. Essi migliorano le entrate in quanto sono mezzi efficaci per vendere più prodotti.

(Direi che tralasciamo come funzionano?)



## Sistemi di reputazione

I *Sistemi di Reputazione* generano punteggi basati su feedback o valutazioni di membri di una community.

## Combinazione tra  sistemi di raccomandazione e sistemi di reputazione

I sistemi di raccomandazione e i sistemi di reputazione sono simili in quanto entrambi raccolgono dati

# Soluzione di Josang e co.

# Una nostra alternativa

Il nostro gruppo ha tuttavia pensato ad un'alternativa alla soluzione proposta da Josang ed il suo team per combinare i risultati ottenuti dai sistemi di reputazione e sistemi di raccomandazione.

La nostra proposta è quella di utilizzare il formalismo dei vincoli soft per combinare le preferenze espresse dai due tipi di sistemi, quello di raccomandazione e quello di reputazione. I vincoli soft saranno modellati utilizzando un c-semiring formato nel seguente modo:

`<N, + = max, x = +, 0 = 0, 1 = 1>`

Quindi la combinazione dei valori sarà ottenuta attraverso l'operatore di somma mentre il criterio di ottimizzazione sarà il massimo dei valori combinati.

I vincoli saranno ottenuti prendendo come risultato i valori di reputazione ottenuti ed i valori di raccomandazione per le due (o più entità) da mettere in relazione. 
Quindi i valori di belief ottenuti dal sistema di reputazione vengono associati ad ogni vincolo. Potrebbe essere (come nel caso dell'esempio) che un'entità in un sistema non abbia un punteggio di reputazione perché non viene considerata dal sistema, ad esempio nel caso di utenti che votano degli hotel: il sistema potrebbe tracciare solo i voti che gli utenti danno agli hotel e non viceversa, in questo caso è bene che il valore di reputazione assegnato a questa entità sia uguale per tutto il dominio, quindi 1 a tutti gli utenti per esempio facendo si che diventi ininfluente ai fini del risultato. Considerando però che sarà possibile modificare questo valore in futuro nel momento in cui si possiedano informazioni quali la reputazione di un'entità che prima non ne aveva.
I valori di raccomandazione vengono utilizzati come valore di preferenza per le due entità.

Si fornisce quì di seguito un esempio utilizzando gli stessi valori contenuti negli esempio precedente sull'implementazione dell'algoritmo di CasMin ma in questo caso a noi interessa solo il valore di *belief* ottenuto dai sistemi di reputazione (rep) e raccomandazione (rec).
I valori di raccomandazione sono riferiti all'utente *User 1* su cui poi si baserà l'esempio per capire secondo l'applicazione dei vincoli soft quale sarebbe l'hotel per lui consigliato.

| Hotel   | Binomial Rep. Score | Binomial Rec. Score |
| ------- | ------------------- | ------------------- |
| Hotel 1 | b = 0.81            | b = 0.1             |
| Hotel 2 | b = 0.16            | b = 0.7             |
| Hotel 3 | b = 0.81            | b = 0.7             |

Che rappresentati graficamente come vincoli diventa:

![User and Hotel rapresentation with CSP](/Users/matteo.ceradini/Google Drive/Università/Intelligenza Artificiale/Progetto/Git/images/ProgettoIA - rec and rac with csp.png)

Quindi effettuando la combinazione dei valori i risultati sono:

$(User1 , Hotel 1) = 1 + 0.1 + 0.81 = 1.91$

$(User 1, Hotel 2) = 1 + 0.7 + 0.16 = 1.86$

$(User 1, Hotel 3) = 1 + 0.7 + 0.81 = 2.51$



# La nostra implementazione



# Bibliografia

https://www.sciencedirect.com/science/article/pii/S1110866515000341