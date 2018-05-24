# Introduzione

Raccomandazione

Reputazione

Unione dei due

# Soluzione di Josang e co.

# Una nostra alternativa

##Introduzione

Il nostro gruppo ha tuttavia pensato ad un'alternativa alla soluzione proposta da Josang ed il suo team per combinare i risultati ottenuti dai sistemi di reputazione e sistemi di raccomandazione, la nostra proposta è quella di utilizzare il formalismo dei vincoli soft per combinare le preferenze espresse dai due tipi di sistemi, quello di raccomandazione e quello di reputazione.

##Descrizione

I vincoli soft saranno modellati utilizzando un c-semiring formato nel seguente modo:

`<N, + = max, x = +, 0 = 0, 1 = 1>`

Quindi la combinazione dei valori sarà ottenuta attraverso l'operatore di somma mentre il criterio di ottimizzazione sarà il massimo dei valori combinati.

I vincoli saranno ottenuti prendendo come risultato i valori di reputazione ottenuti ed i valori di raccomandazione per le due (o più entità) da mettere in relazione. 
Quindi i valori di belief ottenuti dal sistema di reputazione vengono associati ad ogni vincolo. Potrebbe essere (come nel caso dell'esempio) che un'entità in un sistema non abbia un punteggio di reputazione perché non viene considerata dal sistema, ad esempio nel caso di utenti che votano degli hotel: il sistema potrebbe tracciare solo i voti che gli utenti danno agli hotel e non viceversa, in questo caso è bene che il valore di reputazione assegnato a questa entità sia uguale per tutto il dominio, quindi 1 a tutti gli utenti per esempio facendo si che diventi ininfluente ai fini del risultato. Considerando però che sarà possibile modificare questo valore in futuro nel momento in cui si possiedano informazioni quali la reputazione di un'entità che prima non ne aveva.
I valori di raccomandazione vengono utilizzati come valore di preferenza per le due entità.

## Esempio

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



Giunti a questo punto si utilizza l'operatore di ottimizzazione per ottenere il risultato ossia l'*operatore di massimo* (max) ed il risultato ottenuto è la combinazione *User 1 & Hotel 3*. Che di fatto rappresenta la migliore scelta per l'utente 1.

## Conclusioni

A differenza dell'algoritmo di CasMin individuato da Josang la nostra soluzione pre scegliere l'elemento di preferenza migliore non da priorità alle preferenze che hanno un voto "medio/alto" per entrambi i sistemi (quello di reputazione e quello di raccomandazione) ma bensi ottimizza il soddisfacimento in generale. 
Quindi in molti casi la soluzione proposta dallo studio di Josang e la nostra riportano i medesimi risultati ma potrebbero esserci casi in cui questo non è verificato. Suggeriamo di consultare la sezione riguardo alla nostra implementazione per avere ulteriori riscontri.

# La nostra implementazione

