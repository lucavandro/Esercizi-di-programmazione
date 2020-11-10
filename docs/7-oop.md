## g1. Quadrato
Creare una classe chiamata *Quadrato*. La classe è costituta da un membro privato chiamato lato e da 3 metodi publici:
1. perimetro() che calcola il perimetro
2. area() che calcola l'area
3. diagonale() che calcola la diagonale()
4. stampaValori() che stampa nell'ordine: il valore del lato, del perimetro, dell'area e della diagonale

##### ESEMPIO C++ 
```
> Quadrato q(5)
> q.stampaValori()
Lato: 5
Perimetro: 20
Area: 25
Diagonale: 7.071
```


## g2. Cerchio
Creare una classe chiamata *Cerchio*. La classe è costituta da un membro privato chiamato raggio e da 3 metodi pubblici:
1. circonferenza() che calcola il circonferenza
2. area() che calcola l'area
3. diametro() che calcola la diametro()
4. stampaValori() che stampa nell'ordine: il valore del raggio, della circonferenza, dell'area e del diametro

##### ESEMPIO C++ 
```
> Cerchio c(5)
> c.stampaValori()
Raggio: 5
Circonferenza: 31.4
Area: 78.5
Diametro: 10
```

## g3. Conto corrente
Una banca deve creare una piattaforma online per gestire i conti correnti di ciascun cliente.
Un conto corrente deve tenere traccia del *saldo* ovvero di quanti soldi ci sono sul conto. Quando viene creato il conto corrente, il saldo è 0.
Inoltre deve essere possibile effettuare dei prelievi e dei versamenti sul conto, oltre a poter visionare
il saldo corrente.


##### ESEMPIO C++ 
```
> Conto c;
> c.versa(200)
> c.preleva(150)
> c.stampaSaldo()
Il tuo saldo è di 50 euro
```


## g4. Dado
I dadi non sempre hanno 6 facce. Vogliamo costruire un classe chiamata Dado, che crea oggetti di tipo dado e in cui il numero di facce sia deciso al momento della creazione e deve essere maggiore di 4 (numero minimo di facce per un oggetto tridimensionale). Ogni oggetto di tipo dado dovrà avere:
- un getter per accedere al numero di lati (che non può essere cambiato dopo la creazione)
- metodo lancia() che genera un numero casuale compreso tra 1 e n, dove n è il numero di facce


##### ESEMPIO C++ 
```
> Dado d1(4), d2(6);
> d1.getLati()
4
> d2.getLati()
6
> d1.lancia()
3
> d2.lancia()
6
```

## g5. Equazioni
Vogliamo creare una classe Equazione2 che modelli un equazione di secondo grado del tipo ax<sup>2</sup> + bx + c = 0.
Ogni oggetto della classe deve essere inizializzato fornendo i 3 parametri a, b, c che possono essere:
- passati direttamente al costruttore nel main
- richiesti all'utente tramite linea di comando
La classe deve essere provvista dei seguenti metodi:
- setter e getter per a,b,c
- metodo delta() che calcola il delta = b<sup>2</sup>-4ac
- i metodi x1() e x2() che ritornao le rispettive soluzioni se esistono, altrimenti generaro un errore
- stampa() un metodo che stampa l'equazione (vedere esempio)
- stampaSoluzioni() che stampa le soluzioni (vedere esempio)


##### ESEMPIO C++ 
```
> Equaizone eq(1, -2, -3);
> eq.delta()
16
> eq.x1()
-1
> eq.x2()
3
> eq.stampaSoluzioni()
x1 = -1, x2 = 3
> eq.stampa()
x^2 - 2x - 3 = 0
```

## g6. Assitente testuali
Gli assistenti vocali come Alexa, Siri, GoogleAssistant sono sempre più diffusi. Vogliamo costruirne una versione più
semplice, basata sulla programmazione ad oggetti, che riceva comandi testuali e fornisca risposta testuali.
Il nostro assistente, non saprà come rispondere ai nostri comandi, ma sarà in grado di imparare attraverso il nostro insegnamento.
Il nostro assitente è in grado di memorizzare al massimo 100 comandi.
La classe sarà dotata dei seguenti metodi pubblici:
- impara(string comando, string risposta) che consente al nostro assistente di apprendere un nuovo comando
- impara() overloading del metodo precedente, dove comando e riposta sono inseriti da tastiera
- rispondi(string comando) che riceve un comando e fornisce la risposta associata.
- rispondi() oveloading del metodo precedente, dove il comando viene inserito da linea di comando
Se l'assistente non conosce la risposta, stampa una risposta di default "Mi dispiace, non so rispondere a questa domanda"
La classe non è provvista di proprietà pubbliche
##### ESEMPIO C++ 
```
> Assistente alexa;
> alexa.impara("Chi ha scoperto l'America?", "Cristoforo Colombo")
> alexa.impara("Quanti sono i nani di Biancaneve?", "7")
> alexa.impara("Quanto pesi?", "Fatti i fatti tuoi")
> alexa.impara()
Inserisci un comando: 
 Di che colore era il cavallo bianco di Napoleone?
Inserisci una risposta:
 Bianco
> alexa.rispondi("Quanto pesi?")
Fatti i fatti tuoi
> alex.rispondi("Quanti soldi hai sul conto in banca?")
Mi dispiace, non so rispondere a questa domanda
```