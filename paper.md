# Introduzione

## Sistemi di raccomandazione

Su Internet la quantità di informazioni è travolgente e continuamente in aumento, questo ha reso impossibile l'accesso tempestivo a elementi e informazioni di interesse su Internet. I sistemi di recupero delle informazioni (ad esempio i motori di ricerca) hanno parzialmente risolto il problema ma priorità e personalizzazione (mappare i contenuti disponibili per gli interessi e le preferenze dell'utente) di informazioni erano assenti.

Per tale motivo sono stati introdotti i sistemi di raccomandazione. I *Sistemi di Raccomandazione* sono sistemi di filtraggio di informazioni correlate alle preferenze dell'utente, l'interesse o al comportamento osservato su di esso rispetto alla grande quantità di informazioni. Questi sistemi hanno la capacità di prevedere se un determinato utente preferirebbe un articolo o meno in base al profilo dell'utente.

I sistemi di raccomandazione portano dei vantaggi sia agli utenti, mostrando informazioni di interesse, sia per i fornitori di servizi perché riducono i costi di transazione per la ricerca, selezione di articoli in ambiente di shopping online. Essi migliorano le entrate in quanto sono mezzi efficaci per vendere più prodotti.

Lo scopo dei sistemi di raccomandazione è principalmente di generare suggerimenti su risorse di cui un utente, a priori non ne è a conoscenza ma probabilmente potrebbe essere interessato a esse.

(Direi che tralasciamo come funzionano?)



## Sistemi di reputazione

I *Sistemi di Reputazione* sono un componente essenziale di varie piattaforme online, come ad esempio siti di e-commerce o sistemi di condivisione di file. Questi sistemi incoraggiano gli utenti a fornire un feedback su esperienze passate. Nascono perché, prima di essi, gli utenti che interagivano con nuovi siti web non avevano alcuna informazione.

Lo scopo dei sistemi di reputazione è quello di fornire consigli su risorse di cui l'utente è già a conoscenza e interessato. 

## Combinazione tra  sistemi di raccomandazione e sistemi di reputazione

Sposterei la sezione introduzione di Josang qui, ha più senso.

Nella sezione 2 riassumeremo una soluzione studiata ma con un difetto. Nella sezione 3 presenteremo una nostra soluzione utilizzano i vincoli soft.

# Soluzione di Josang e co.

## Introduzione

Come detto precedentemente i sistemi di reputazione e raccomandazione sono basati su principi differenti ma hanno entrambi lo stesso scopo: supportare l'utente fornendo delle informazioni per agevolare le sue decisioni. Brevemente, i compiti dei due sistemi sono i seguenti:

- sistemi di raccomandazione: suggeriscono all'utente risorse che non conosce ma alle quali può essere interessato. I punteggi di raccomandazione sono calcolati basandosi su informazioni fornite da altri utenti per oggetti simili;
- sistemi di reputazione: forniscono alla comunità informazioni riguardanti risorse che l'utente conosce già. I punteggi di reputazione indicano quanto un oggetto è piaciuto ad un utente.

Per fornire delle raccomandazioni più accurate è possibile integrare i due sistemi. L'integrazione risulta complessa a causa della diversità dei sistemi che hanno forme diverse di feedback. Anche i risultati hanno forme diverse:

- un voto da 1 a 5 per i sistemi di reputazione;
- una tupla (d1, ... , dk), dove di è una diversa caratteristica della risorsa d, per i sistemi di raccomandazione.

La soluzione del Professor Josang e dei suoi colleghi consiste nel fondere i punteggi di reputazione e di raccomandazione tramite un operatore chiamato CasMin (Cascading Minimum Common Belief Fusion). Il problema principale è che i punteggi di reputazione sono potenzialmente diversi dai punteggi di raccomandazione, ossia sono eterogenei e quindi impossibili da fondere senza prima essere manipolati. Per applicare l'operatore CasMin a tali punteggi bisogna renderli prima di tutto omogenei. Per rendere omogenei i punteggi di reputazione e i punteggi di raccomandazione, essi devono essere mappati in opinioni soggettive. Dopo essere stati mappati in opinioni soggettive, i punteggi possono essere combinati con l'operatore CasMin che restituirà un valore alto solo se entrambi i punteggi, di reputazione e di raccomandazione rispettivamente, saranno alti. Una risorsa verrà suggerita all'utente solo se è stata raccomandata con alta confidenza e se ha un alto punteggio di reputazione. La raccomandazione diviene più accurata rispetto ad il solo sistema di raccomandazione che può raccomandare oggetti con bassa reputazione. Infine i consigli distribuiti agli utenti avranno una qualità migliore.

## Opinioni soggettive

In questa sezione viene introdotta la notazione e la formazione delle opinioni soggettive usate per fondere gusto e fiducia. Successivamente viene descritto un metodo per mappare dei punteggi multinomiali in opinioni binomiali. I punteggi multinomiali sono la forma di feedback restituita dai sistemi di reputazione e dai sistemi di raccomandazione.

### Formazione e rappresentazione

Un'opinione soggettiva esprime la credenza (belief) degli stati di uno spazio degli stati chiamato "frame". Uno stato in un frame può essere considerato come una dichiarazione, quindi un frame contiene un insieme di dichiarazioni. Indichiamo con X = {x1, x2, ... , xk} un frame di cardinalità k, dove xi (1<=i<=k) rappresenta uno specifico stato. Un'opinione distribuisce la massa di credenze sul ridotto powerset del frame, indicato con R(X).

Un'opinione è una funzione composta che consiste in un vettore di belief **b**, un parametro di incertezza **u** e un vettore di base rate **a**, che prende valori nell'intervallo [0,1] e che soddisfa i seguenti requisiti di addittività:

- req 1
- req 2

L'opinione di un utente A sul frame X è denotata come omegaAx = (bX,uX,aX), dove **b**X è un vettore di belief sugli stati di R(X), uX è la massa di incertezza complementare, e aX è un vettore di base rate su X, tutti visti dal punto di vista del proprietario delle belief A.

### Tipologie di opinioni soggettive

Vengono presentate due diverse tipologie di opinioni soggettive:

- Opinioni multinomiali: il vettore di belief **b**X viene applicato solamente agli elementi Xi appartenenti a X, non in R(X);
- Opinioni binomiali: vengono applicate ai frame binari e hanno una rappresentazione speciale. Indichiamo con X = {x,xNeg} un frame binario. Un'opinione binomiale sulla verità dello stato x è la quadrupla ordinata omegaX=(b,d,u,a) dove:
  - b(belief): è la massa di credenze in supporto che x sia vero;
  - d(disbelief): è la massa di credenze in supporto che x sia falso;
  - u(incertezza): è l'incertezza sulla probabilità di x;
  - a(base rate): è la probabilità preventiva non informativa di x.

In caso di opinioni binomiali l'equazione 2 è espressa come... mettere formula...

### Conversione di opinioni multinomiali in opinioni binomiali

Le opinioni multinomiali sono una generalizzazione delle opinioni binomiali e in certi casi può essere necessario proiettare le opinioni multinomiali in opinioni binomiali. Per esempio, un sistema di reputazione dove i punteggi sono dati nella forma 1-5 stelle può rappresentare un punteggio di reputazione come un'opinione multinomiale su un frame con 5 stati, ognuno dei quali rappresenta uno specifico numero di stelle. In questo caso, un punteggio di reputazione rappresentato come un'opinione multinomiale può essere proiettato in un'opinione binomiale nel modo seguente. 

Indichiamo con X={x1,...,xk} un frame dove i k stati rappresentano un livello crescente di punteggio. Indichiamo con Y={y,yNeg} un frame frame binario dove y e yNeg indicano un'alta qualità e una bassa qualità di una risosrsa, rispettivamente. Assumiamo che un punteggio di reputazione o un valore di raccomandazione siano espressi tramite l'opinione multinomiale omegaX() sul frame X, e che un'opinione binomiale omegaY=() è richiesta sul frame binario Y. Allora la proiezione dall'opinione multinomiale omegaX su X nella opinione binomiale omegaY su Y è definita da: mettere sistema...

Il vantaggio di proiettare opinioni multinomiali in opinioni binomiali è la flessibilità di analizzare i punteggi di reputazione e i valori di raccomandazione indipendentemente dalla cardinalità del frame.

## Determinazione delle opinioni

In questa sezione vengono descritte le procedure per derivare opinioni soggettive dai punteggi di reputazione e dai valori di raccomandazione prodotti dai sistemi di reputazione e dai sistemi di raccomandazione rispettivamente.

### Opinioni derivate dai sistemi di reputazione

Un sistema di reputazione generalmente si applica a servizi o beni che possono essere valutati su uno o più aspetti. Nel caso in cui solamente un singolo aspetto può essere valutato, esso rappresenta tipicamente la qualità totale di uno specifico servizio o bene. Ogni aspetto può essere valutato con uno specifico livello di qualità, ad esempio da 1 a 5 stelle. È possibile che per un aspetto possano essere assegnati solo due possibili livelli di qualità, ad esempio "pollice in su" e "pollice in giù". In quest'ultimo caso i livelli indicano una buona qualità o una cattiva qualità rispettivamente.

Le opinioni per ogni aspetto possono essere derivate da tali valutazioni. Il frame per ogni aspetto è composto dall'insieme di livelli di punteggio discreti che possono essere assegnati all'aspetto, quindi nel caso in cui per un aspetto si possa assegnare una valutazione da 1 a 5 stelle, il frame corrispondente avrà 5 stati. Indichiamo con X il frame di cardinalità k, con r(xi) il numero di punteggi assegnati del tipo xi, e con omegaX =() un'opinione multinomiale su X. Più punteggi vengono raccolti e minore sarà l'incertezza. L'opinione omegaX può essere determinata dai punteggi r(xi) tramite la seguente equazione... Inserire equazione in LaTeX o come immagine...

Nell'equazione W = 2 è il peso precedente non informativo con valore di default imposto dal requisito di avere una funzione di densità di probabilità uniforme su frame binari.

Un punteggio è espresso come uno specifico livello corrispondente ad un singolo stato nel frame. Nel caso in cui dovessero esserci più di due livelli di punteggio, le opinioni derivate sono multinomiali. Dualmente, nel caso in cui solo due tipi di valutazione possono essere dati, il frame è binario e quindi le opinioni derivate sono binomiali. I punteggi di reputazione espressi come opinioni multinomiali possono essere mappati in opinioni binomiali assumendo che ogni livello di punteggio corrisponde ad un valore compreso nell'intervallo [0,1].

### Opinioni derivate dai sistemi di raccomandazione

Nel nostro progetto i valori di raccomandazione sono generati da un metodo CF (Collaborative filtering) basato sull'utente. Il compito dei metodi CF è di predirre la preferenza di una data risorsa per un utente attivo, basandosi sulla storia dell'utente stesso e degli altri partecipanti della comunità. Vengono introdotti i simboli s,v per gli utenti e i,j per gli oggetti. Indichiamo con Rv,i il punteggio dato da un utente v all'oggetto i, e con Iv l'insieme degli oggetti che l'utente v ha precedentemente votato. Il punteggio medio dell'utente v è dato dalla seguente formula...

Indichiamo con Ns,j il vicinato di un utente attivo s vincolato dall'aver votato l'oggetto j. Quindi Ns,j è l'insieme di utenti che hanno votato gli stessi (o alcuni) oggetti che anche s ha votato e che hanno votato anche lo specifico oggetto j. Generalmente, solo i migliori K utenti più simili a s vengono selezionati per far parte del vicinato. La predizione Ps,j per l'utente s sull'oggetto j è data dalla seguente formula...

Dove k è un fattore di normalizzazione e w(s,v) rappresenta la somiglianza tra gli utenti s e v. Ci sono diversi metodi per calcolare la somiglianza tra gli utenti ma il più comune è il coefficiente di correlazione di Pearson:

dove Is,v rappresenta l'insieme degli oggetti che entrambi gli utenti s e v hanno votato, e w(s,v) è localizzato nell'intervallo [-1,1]. Un problema per il calcolo della somiglianza è che nel caso in cui non ci sono o solamente pochi oggetti sono stati votati in comune, la somiglianza calcolata non è affidabile introducendo incertezza rispetto al valore previsto. Questo problema è detto cold start. Però, quando le predizioni sono rappresentate in termini di opinioni soggettive, il grado di incertezza può essere esplicitamente espresso. Qui sotto viene descritto un metodo per ricavare opinioni binomiali dalle predizioni fatte da un metodo CF.

La derivazione si basa su due assunzioni intuitive:

- L'incertezza della predizione derivata è una funzione decrescente del numero di punteggi dati dagli utenti simili in Ns,j. Più utenti ci saranno nel vicinato e più affidabile sarà la predizione risultante;
- Vale l'equazione...

Quindi emerge il seguente insieme di equazioni...

dove W = 2 è il precedente peso non informativo. Come detto precedentemente Ns,j è il vicinato dell'utente s vincolato dall'aver votato l'oggetto j, e Is,v è l'insieme di oggetti che entrambi gli utenti s e v hanno votato.

Sebbene l'equazione è stata ottenuta da un metodo CF basato sull'utente, essa può essere facilmente adattata ai metodi CF basati sull'oggetto: ...

dove Ns,j è il vicinato dell'oggetto j, ossia l'insieme di oggetti che sono stati votati dagli utenti che hanno votato anche l'oggetto j e dove tutti (o alcuni) sono stati votati dall'utente s. Mentre Ui,j è l'insieme degli utenti che hanno votato entrambi gli oggetti i e j. Come prima, solo i migliori K oggetti saranno selezionati come vicinato per le predizioni di punteggio.

## Combinazione dei valori di raccomandazione e reputazione

Dopo aver ottenuto le opinioni soggettive dai sistemi di reputazione e dai sistemi di raccomandazione, esse possono essere combinate. Il gruppo utilizza l'operatore CasMin introdotto da Josang e i suoi colleghi. Questo operatore ha la capacità di combinare i livelli di punteggio dei due diversi sistemi, se questi sono espressi come opinioni soggettive. In questa sezione vengono presentati i principi e la logica dell'algoritmo CasMin e due versioni dello stesso:

- Una versione proposta da Josang che richiede che i punteggi siano espressi come opinioni multinomiali;
- Una versione, da noi rivista, basata sulla versione di Josang, che richiede che i punteggi siano espressi come opinioni binomiali.

Infine viene presentato un esempio di utilizzo dell'operatore CasMin, nella realtà di TripAdvisor, con un dataset puramente inventato.

### Caratteristiche dell'operatore CasMin

L'operatore CasMin è applicabile quando gli stati nel frame rappresentano livelli ordinati di punteggio. Quando si combinano le masse di credenze del più alto livello sul frame, la migliore massa di credenza tra i due argomenti è ridotta per essere matchata con la massa di credenza del secondo argomento. Questo permette di distribuire omogeneamente le masse di credenza su tale stato. La porzione di massa di credenza che è stata precedentemente rimossa dal migliore dei due argomenti viene sommata alla massa di credenza del livello subito inferiore nel frame. L'algoritmo procede in questo modo fino ad arrivare al livello minimo del frame. Infine la massa di credenza degli ultimi argomenti può essere matchata con la massa di incertezza dell'altro argomento. In questo modo l'incertezza viene ridotta, mentre la massa di credenza del livello più basso viene incrementata.

Questo operatore gode della proprietà conservativa. Questa proprietà è utile a fare in modo che un oggetto venga raccomandato solo se ha un alto valore di raccomandazione e un alto punteggio di reputazione. CasMin fornisce un modello di combinazione conservativo poiché prende il più piccolo punteggio di reputazione e valore di raccomandazione a ogni livello, partendo dal livello più alto, e ad ogni livello fa scendere i valori in eccesso nei livelli inferiori. Quindi un alto valore di CasMin può essere ottenuto solamente se entrambi i sistemi producono punteggi alti. In questo modo, il consiglio prodotto dalla combinazione risultante di CasMin sarà più conservativo rispetto a quello prodotto dai due sistemi isolati.

### Operatore CasMin con opinioni multinomiali

Indichiamo con X={x~1~ ,...,x~k~} un frame ordinato di cardinalità k, dove xk è il livello di punteggio più alto ottenuto da un sistema di raccomandazione o reputazione. Assumiamo che ci siano due opinioni omegaAx e omegaBx sul frame X dove A e B indicano due diversi proprietari di credenze, ossia due argomenti. Le due opinioni possono essere matematicamente combinate usando l'operatore CasMin denotato dalla seguente espressione...

La soluzione proposta da Josang richiede opinioni multinomiali. Prima di tutto agisce sulla credenza del livello più alto xk e per finire agisce sulla credenza del livello più basso x1. Ad ogni livello esegue le operazioni descritte nella sezione precedente. La linea 2 assicura che la credenza dell'argomento A sia sempre migliore della credenza dell'argomento B, facendo un'operazione di swap se necessario. Al termine del ciclo la nuova opinione dell'utente A rappresenta il risultato combinato che verrà restituito.

#### Pseudocodice

```
FOR i = k to 2 DO {
    IF bAx(xi)<=bBx(xi) THEN {Swap(omegaAx,omegaBx);}
    IF uBx>(bAx(xi) - bBx(xi)) THEN {
        uBx=uBx - (bAx(xi) - bBx(xi));
        bBx(xi) = bAx(xi);
        bcascade=0;
    } ELSE {
        bBx(xi)=bBx(xi) + uBx;
        uBx=0;
        bcascade=bAx(xi) - bBx(xi);
        bAx(xi)=bBx(xi);
    }
    bAx(xi-1)=bAx(xi-1) + bcascade;
}
CasMin=omegaAx;
```

#### Esempio

| Hotel   | Rep. Ratings                                                 | Multinomial Rep. Score                                       | Binomial Rep. Score                  | Rec. Value                        | CasMin Advice                        |
| ------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------ | --------------------------------- | ------------------------------------ |
| Hotel 1 | r(x5) = 50<br />r(x4) = 10<br />r(x3) = 10<br />r(x2) = 0<br />r(x1) = 5 | bX5 = 0.65<br />bX4 = 0.13<br />bX3 = 0.13<br />bX2 = 0.00<br />bX1 = 0.06<br />uX = 0.03 | b = 0.81<br />d = 0.16<br />u = 0.03 | b = 0.1<br />d = 0.7<br />u = 0.2 | b = 0.30<br />d = 0.70<br />u = 0.00 |
| Hotel 2 | r(x5) = 5<br />r(x4) = 0<br />r(x3) = 10<br />r(x2) = 10<br />r(x1) = 50 | bX5 = 0.06<br />bX4 = 0.00<br />bX3 = 0.13<br />bX2 = 0.13<br />bX1 = 0.65<br />uX = 0.03 | b = 0.16<br />d = 0.81<br />u = 0.03 | b = 0.7<br />d = 0.1<br />u = 0.2 | b = 0.19<br />d = 0.61<br />u = 0.20 |
| Hotel 3 | r(x5) = 50<br />r(x4) = 10<br />r(x3) = 10<br />r(x2) = 0<br />r(x1) = 5 | bX5 = 0.65<br />bX4 = 0.13<br />bX3 = 0.13<br />bX2 = 0.00<br />bX1 = 0.06<br />uX = 0.03 | b = 0.81<br />d = 0.16<br />u = 0.03 | b = 0.7<br />d = 0.1<br />u = 0.2 | b = 0.81<br />d = 0.19<br />u = 0.00 |



Nell'esempio illustrato si considera il caso di dover fornire consigli sugli hotel di un sito web. Si assume di avere un sistema di raccomandazione che tracci le preferenze degli utenti, e un sistema di reputazione che permetta agli utenti di valutare gli hotel. Con il metodo descritto in sezione §... il sistema di reputazione può produrre punteggi espressi come opinioni multinomiali. Con il metodo descritto in sezione §... le opinioni multinomiali possono essere trasformate in opinioni binomiali. I valori di raccomandazione per ogni hotel e ogni utente sono espressi come opinioni binomiali usando le equazioni descritte in sezione §... Il sistema di raccomandazione identifica una lista di hotel basandosi sul punteggio dato dall'utente e da altri viaggiatori. Esso può prevedere che all'utente piacerà un hotel perché altri utenti con gusti simili sono stati soddisfatti dell'hotel. Invece, il sistema di reputazione produce punteggi disponibili a tutta la comunità per ogni hotel. L'operatore CasMin produce risultati conservativi in modo che un hotel debba avere simultaneamente alti valori di raccomandazione e alti punteggi di reputazione. Nella tabella è mostrata la combinazione di due opinioni multinomiali, una per il sistema di raccomandazione e una per il sistema di reputazione, utilizzando l'algoritmo sopra descritto. Vengono illustrati i risultati di analisi di tre hotel differenti sul sito web. Nei casi dell'hotel 1 e l'hotel 2 dove i valori di raccomandazione e i punteggi di reputazione sono in conflitto, il consiglio restituito dal CasMin ha un belief basso. L'unico risultato buono è per l'hotel 3 dove entrambi i sistemi hanno prodotto punteggi positivi e la combinazione ha prodotto un buon valore della belief del CasMin.

### Operatore CasMin con opinioni binomiali

Il gruppo presenta una versione rivista rispetto a quella di Josang. La versione proposta richiede opinioni binomiali. Prima di utilizzare CasMin bisogna ottenere le opinioni multinomiali a partire dai punteggi di reputazione (riferimento a equazione). Queste devono essere poi mappate in opinioni binomiali (riferimento equazione). Successivamente si possono derivare le opinioni binomiali dai sistemi di raccomandazione che, nel caso proposto, utilizzano un metodo Collaborative Filtering basato sull'utente (riferimento equazione). Dopo aver ottenuto le due opinioni binomiali si può utilizzare l'algoritmo di seguito proposto per combinare i risultati. L'algoritmo restituisce solamente il vettore di belief **b** del risultato combinato. Infatti è il vettore di belief il dato interessante che determina la qualità della raccomandazione finale. Un vettore di belief alto nel CasMin indica una buona raccomandazione (raccomandazione e reputazione entrambi alti), mentre un valore basso indica una cattiva raccomandazione, ossia l'oggetto non verrà consigliato all'utente.



#### Pseudocodice

```
IF bAx(xi)<=bBx(xi) THEN {Swap(omegaAx,omegaBx);}
IF uBx>(bAx(xi) - bBx(xi)) THEN {
     uBx=uBx - (b^A^~x~(xi) - bBx(xi));
     bBx(xi) = bAx(xi);
} ELSE {
    bBx(xi)=bBx(xi) + uBx;
    uBx=0;
    bAx(xi)=bBx(xi);
}
CasMin=omegaAx;
```

#### Esempio

| Hotel   | Binomial Rep. Score                  | Binomial Rec. Value                | CasMin Advice |
| ------- | ------------------------------------ | ---------------------------------- | ------------- |
| Hotel 1 | b = 0.81<br />d = 0.16<br />u = 0.03 | b = 0.1<br />d = 0.16<br />u = 0.2 | b = 0.3       |
| Hotel 2 | b = 0.16<br />d = 0.81<br />u = 0.03 | b = 0.7<br />d = 0.1<br />u = 0.2  | b = 0.19      |
| Hotel 3 | b = 0.81<br />d = 0.16<br />u = 0.03 | b = 0.7<br />d = 0.1<br />u = 0.2  | b = 0.81      |



Applicando l'algoritmo sopra riportato alle due opinioni binomiali riportate in tabella di ottengono i valori di credenza in ultima colonna. Si può notare che l'hotel che verrà consigliato dal sistema è il terzo. Infatti il valore ottenuto dal CasMin è 0.81 che significa che entrambi i sistemi, di reputazione e raccomandazione, hanno restituito buoni punteggi per l'hotel 3. Nel caso dell'hotel 1 si può vedere come, nonostante ci sia un buon punteggio di reputazione (0.81), l'operatore CasMin restituisca un risultato basso (0.3). Questo perché il valore restituito dal sistema di raccomandazione per l'hotel 1 è basso (0.1). Per concludere, nel caso dell'hotel 2 si può vedere come, nonostante ci sia un buon valore di raccomandazione (0.7), l'operatore CasMin restituisca un risultato basso (0.19). Questo perché il punteggio restituito dal sistema di reputazione per l'hotel 2 è basso (0.16).

## Conclusioni

Da quando i sistemi di raccomandazione e reputazione sono a supporto delle decisioni si è pensato che la combinazione degli stessi potesse produrre risultati migliori rispetto ai sistemi isolati. Però si è compreso che combinare i due sistemi è complesso. Infatti si è dovuti ricorrere alla teoria della logica soggettiva per rendere omogenei i due risultati. Con questo breve articolo, il gruppo ha riproposto l'algortimo di Josang e ha proposto una nuova versione dell'algortimo che funziona con le opinioni binomiali. Il gruppo ha dovuto creare un nuovo algoritmo perché è risultato difficile ricavare opinioni multinomiali dai sistemi di raccomandazioni per cui risulta difficile applicare l'algoritmo di Josang nella realtà. Il gruppo ritiene che la soluzione proposta sia migliore per un utilizzo con dati reali e cercherà di provare questa affermazione implementando l'algoritmo in Python e testandolo con dataset reali trovati nel web.

# Una nostra alternativa

##Introduzione

Il nostro gruppo ha tuttavia pensato ad un'alternativa alla soluzione proposta da Josang ed il suo team per combinare i risultati ottenuti dai sistemi di reputazione e sistemi di raccomandazione, la nostra proposta è quella di utilizzare il formalismo dei vincoli soft per combinare le preferenze espresse dai due tipi di sistemi, quello di raccomandazione e quello di reputazione.

##Descrizione

I vincoli soft saranno modellati utilizzando un c-semiring formato nel seguente modo:

`<N, + = max, x = +, 0 = 0, 1 = 1>`

Quindi la combinazione dei valori sarà ottenuta attraverso l'operatore di sommo, il criterio di ottimizzazione sarà il massimo dei valori combinati, il minimo livello di preferenza sarà rappresentato da uno zero mentre il massimo da un uno.

I vincoli saranno ottenuti mettendo in relazione le entità facenti parte del sistema e collegandole tra loro utilizzando i risultati dai due sistemi (reputazione e raccomandazione) nel seguente modo:

1. I **valori di belief ottenuti dal sistema di reputazione** vengono associati ad ogni vincolo. 

   Potrebbe essere (come nel caso dell'esempio) che un'entità in un sistema non abbia un punteggio di reputazione perché non viene considerata dal sistema (ad esempio nel caso di utenti che votano degli hotel: il sistema potrebbe tracciare solo i voti che gli utenti danno agli hotel e non viceversa) ed in questo caso il valore di reputazione assegnato a questa entità deve essere uguale per tutto il dominio (nel nostro caso 1). E' bene considerare che sarà possibile modificare questo valore in futuro nel momento in cui si riesca ad ottenere punteggi di reputazione anche per quelle entità che prima non venivano valutate.

2. I **valori di belief ottenuti dal sistema di raccomandazione** vengono utilizzati invece come valore di preferenza per le due entità.

## Sviluppo

Una volta costruiti i vincoli tra le entità utilizzando i valori di belief dei sistemi di raccomandazione e reputazione sarà possibile capire quale è l'associazione migliore che massimizza la preferenza tra le entità convolte.

Per ottenere il risultato su n vincoli, basterà combinare le preferenze tra le n entità attraverso l'operatore somma, la preferenza migliore sarà quella massima. 

### Esempio

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
Quindi in molti casi la soluzione proposta dallo studio di Josang e la nostra riportano i medesimi risultati ma potrebbero esserci casi in cui questo non è verificato. Consultare la sezione riguardo alla nostra implementazione per avere i risconti ed i risultati di questa analisi.

# La nostra implementazione



# Bibliografia

https://www.sciencedirect.com/science/article/pii/S1110866515000341

https://link.springer.com/article/10.1007/s12599-017-0493-1