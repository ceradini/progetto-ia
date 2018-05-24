# Introduzione

Raccomandazione

Reputazione

Unione dei due

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

In questa sezione introduremo, prima di tutto, la notazione e la formazione delle opinioni soggettive usate per fondere gusto e fiducia. Poi descriveremo un metodo per mappare dei punteggi multinomiali in opinioni binomiali. I punteggi multinomiali sono la forma di feedback restituita dai sistemi di reputazione e dai sistemi di raccomandazione.

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

### Opinioni derivate dai sistemi di reputazione

### Opinioni derivate dai sistemi di raccomandazione

## Combinazione dei valori di raccomandazione e reputazione

### Operatore CasMin per opinioni multinomiali

#### Esempio



### Operatore CasMin per opinioni binomiali

#### Esempio

## Conclusioni







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

