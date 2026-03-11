## c1. Contiamo!
Scrivi un programma che stampi i numeri da 1 a 100.

##### ESEMPIO
```
1
2
3
...
99
100
```

<!-- ##### [Soluzioni](soluzioni/c/c1.md) -->


## c2. Contiamo al contrario!
Scrivi un programma che stampi i numeri da 100 a 1

##### ESEMPIO 1
```
100
99
98
...
2
1
```

<!-- ##### [Soluzioni](soluzioni/c/c2.md) -->


## c3. Contiamo! 2
Scrivi un programma che stampi i numeri da 1 ad un numero **n** inserito dall'utente.

##### Attenzione!
Assicurati che l'utente inserisca un numero maggiore di 1 o il tuo programma potrebbe comportarsi in modo *"inaspettato"*

##### ESEMPIO 1
```
Inserisci un numero: 15

1
2
3
...
14
15
```
##### ESEMPIO 2
```
Inserisci un numero: -5
Errore: Devi inserire un numero maggiore di 1
Inserisci un numero: 33

1
2
3
...
32
33
```

<!-- ##### [Soluzioni](soluzioni/c/c3.md) -->


## c4. Contiamo! 3
Scrivi un programma che stampi tutti i numeri compresi tra due valori a e b inseriti dall'utente.
Se a < b i numeri vanno stampati in ordine crescente.
Se a > b i numeri vanno stampati in ordine descerscente.

Guarda con attenzione gli esempi per capire il comportamento richiesto dal programma

##### ESEMPIO 1
```
Inserisci il valore di a: 4
Inserisci il valore di b: 15

4
5
6
...
14
15
```
##### ESEMPIO 2
```
Inserisci il valore di a: 15
Inserisci il valore di b: 4

15
14
13
...
5
4
```

<!-- ##### [Soluzioni](soluzioni/c/c4.md) -->


## c5. I numeri di Fibonacci
I numeri di Fibonacci sono una successione di numeri individuata nel XIII secolo dal matematico italiano Leonardo Fibonacci. Questa serie è molto famosa e si vasa sulla seguente regola:

> ogni numero della serie è la somma dei due numeri precedenti. 

Cerchiamo di capire come funziona partendo da due numeri : 0 e 1 che sono i primi due numeri della serie.

| ultimi due numeri | numero generato | la serie diventa |
|-------------------|-----------------|------------------|
| 0,1               | 1               | 0,1,1            |
| 1,1               | 2               | 0,1,1,2          |
| 1,2               | 3               | 0,1,1,2,3        |
| 2,3               | 5               | 0,1,1,2,3,5      |
| 3,5               | 8               | 0,1,1,2,3,5,8    |
| 5,8               | 13              | 0,1,1,2,3,5,8,13 |

Scrivi un programma che stampi i primi 20 numeri della successione di Fibonacci.

##### Attenzione!
Guarda l'esempio e assicurati di avere ottenuto gli stessi numeri come risultato!

##### ESEMPIO 1
```
0
1
1
2
3
5
8
13
...
2584
4181
6765
```

<!-- ##### [Soluzioni](soluzioni/c/c5.md) -->


## c6. C'è posta per te
Giulia ed Emilia consegnano la posta a via Roma dove ci sono 10 edifici: Giulia consegna la posta sul lato sinistro della strada dove ci sono i numeri civici pari, Emilia sul lato destro dove i numeri civici sono dispari.
Emilia sostiene di lavorare molto di più di Giulia sostenendo che le lettere consegnate dal suo lato sono di più rispetto a quelle del lato di Giulia.
Giulia non è d'accordo e propone ad Emilia di scrivere un programma che le aiuti una volta per tutte a porre fine a questa questione.

Scrivi un programma che chieda all'utente per ciascun numero civico quante lettere vengono consegnate. Alla fine il programma stamperà chi tra Emilia e Giulia ha consegnato più lettere.

##### ESEMPIO 1
```
Inserisci le lettere consegnate al civico n.1 : 10
Inserisci le lettere consegnate al civico n.2 : 4
Inserisci le lettere consegnate al civico n.3 : 5
Inserisci le lettere consegnate al civico n.4 : 1
Inserisci le lettere consegnate al civico n.5 : 2
Inserisci le lettere consegnate al civico n.6 : 6
Inserisci le lettere consegnate al civico n.7 : 1
Inserisci le lettere consegnate al civico n.8 : 0
Inserisci le lettere consegnate al civico n.9 : 3
Inserisci le lettere consegnate al civico n.10 : 11

Giulia ha consegnato 22 lettere
Emilia ha consegnato 21 lettere

Giulia lavora più di Emilia
```
##### ESEMPIO 2
```
Inserisci le lettere consegnate al civico n.1 : 12
Inserisci le lettere consegnate al civico n.2 : 4
Inserisci le lettere consegnate al civico n.3 : 3
Inserisci le lettere consegnate al civico n.4 : 1
Inserisci le lettere consegnate al civico n.5 : 4
Inserisci le lettere consegnate al civico n.6 : 6
Inserisci le lettere consegnate al civico n.7 : 1
Inserisci le lettere consegnate al civico n.8 : 0
Inserisci le lettere consegnate al civico n.9 : 3
Inserisci le lettere consegnate al civico n.10 : 11

Giulia ha consegnato 22 lettere
Emilia ha consegnato 23 lettere

Emilia lavora più di Giulia
```
##### ESEMPIO 3
```
Inserisci le lettere consegnate al civico n.1 : 12
Inserisci le lettere consegnate al civico n.2 : 4
Inserisci le lettere consegnate al civico n.3 : 3
Inserisci le lettere consegnate al civico n.4 : 1
Inserisci le lettere consegnate al civico n.5 : 4
Inserisci le lettere consegnate al civico n.6 : 6
Inserisci le lettere consegnate al civico n.7 : 1
Inserisci le lettere consegnate al civico n.8 : 0
Inserisci le lettere consegnate al civico n.9 : 2
Inserisci le lettere consegnate al civico n.10 : 11

Giulia ha consegnato 22 lettere
Emilia ha consegnato 22 lettere

Emilia e Giulia lavorano allo stesso modo.
```

<!-- ##### [Soluzioni](soluzioni/c/c6.md) -->


## c7. Consegne a domicilio
Luca consegna pasti a domicilio con la sua bici. Spesso i clienti gli lasciano una mancia e lui ha deciso di creare un programma per tenere un piccolo bilancio dei soldi guadagnati con le mance.
Scrivere un programma che legga i valori delle mance guadagnate da Luca fino a quando non viene inserito un valore minore di 0. 
A quel punto il programma stampa:

- il numero di consegne effettuate
- il totale delle mance ricevute
- il valore medio di una mancia (tenendo conto solo dei clienti che lasciano la mancia)
- Il numero di consegne effettuate
- la percentuale di clienti che ha lasciato una mancia

##### ESEMPIO 
```
Inserisci il valore della mancia: 5
Inserisci il valore della mancia: 0
Inserisci il valore della mancia: 2
Inserisci il valore della mancia: 2
Inserisci il valore della mancia: -1

Hai effettuato 4 consegne
Hai guadagnato 10 Euro di mancia
Il valore medio di una mancia è di 3 euro
Il 75% dei clienti ha lasciato una mancia
```

<!-- ##### [Soluzioni](soluzioni/c/c7.md) -->


## c8. Il fattoriale
Il fattoriale di un numero è uguale al prodotto di un numero naturale per tutti i suoi predecessori. L'unica eccezione è il fattoriale di 0 che è pari a 1.
**Che cosa signfica?** 
Indichiamo il fattoriale di un numero con il simbolo "!" ad esempio il fattoriale di 6 si indica con 6!:

| n! | Calcolo         | Risulato |
|----|-----------------|----------|
| 0! | Per convenzione | 1        |
| 1! | 1               | 1        |
| 2! | 2·1             | 2        |
| 3! | 3·2·1           | 6        |
| 4! | 4·3·2·1         | 24       |
| 5! | 5·4·3·2·1       | 120      |

Scrivi un programma che letto un numero in ingresso calcoli il suo fattoriale.

**Attenzione**: puoi calcolare il fattoriale solo se il numero è positivo! Se l'utente inserisce un numero negativo devi stampare un messaggio di errore.

##### ESEMPIO 1
```
Inserisci un numero: 5

5! = 120
```

##### ESEMPIO 2
```
Inserisci un numero: -3

Errore: è possibile calcolare il fattoriale solo di un numero maggiore o uguale a zero
```
##### ESEMPIO 3
```
Inserisci un numero: 0

0! = 1
```

<!-- ##### [Soluzioni](soluzioni/c/c8.md) -->


## c9. Indovina il numero
Un programma genera un numero casuale tra 1 e 100, ma senza mostrarlo a video: sarà l'utente a doverlo indovinare! Il gioco prosegue fino a quando l'utente non indovina il numero.
Ad ogni tentativo il computer mostra un aiuto:

- stampa "Più grande" se il numero da indovinare è maggiore dell'ultimo numero inserito
- stampa "Più piccolo" se il numero da indivinare è minore dell'ultimo numero inserito.

Una volta indovinato il numero il programma stampa il messaggio "HAI VINTO!" e mostra il numero di tentativi effettuati.

##### ESEMPIO 1
```
Indovina il numero: 16
Più grande!
Indovina il numero: 50
Più piccolo!
Indovina il numero: 25
Più grande!
Indovina il numero: 26

HAI VINTO!
Hai effettuato 4 tentativi
```

<!-- ##### [Soluzioni](soluzioni/c/c9.md) -->


## c10. Indovina il numero 2
Un programma genera un numero casuale tra 1 e 100, ma senza mostrarlo a video: sarà l'utente a doverlo indovinare! L'utente ha a disposizione 3 tentativi.
Ad ogni tentativo errato il computer mostra un aiuto:

- stampa "Fuochino" se il valore assoulto della differenza tra il numero da indovinare e l'ultimo numero inserito è minore o uguale di 5
- stampa "Acqua" se il valore assoulto della differenza tra il numero da indovinare e l'ultimo numero inserito è maggiore di 5

Se l'utente indovina il numero entro 3 tentativi,il programma stampa la scritta "HAI VINTO" e termina: se l'utente indovina al primo tentativo, il tentativo 2 e 3 non devono essere richiesto, così come se l'utente indovina al secondo tentativo il tentativo 3 non viene richiesto all'utente.
Se l'utente non indovina il numero entro 3 tentativi, il programma stampa "HAI PERSO" e mostra all'utente il numero da indovinare

##### ESEMPIO 1
```
Tentativo 1: 16
Acqua
Tentativo 2: 25
Fuochino
Tentativo 3: 26

HAI VINTO!
```
##### ESEMPIO 2
```
Tentativo 1: 25
Fuochino
Tentativo 2: 26

HAI VINTO!
```
##### ESEMPIO 3
```
Tentativo 1: 16
Acqua
Tentativo 2: 25
Fuochino
Tentativo 3: 28
Fuochino

HAI PERSO! Il numero giusto era 26
```

<!-- ##### [Soluzioni](soluzioni/c/c10.md) -->



## c11. Il bancomat
Un bancomat ha una pulsantiera con 4 bottoni:

1. Per effettuare un prelievo
2. Per effettuare un versamento
3. Per stampare il saldo
4. Per terminare l'operazione

Una volta terminata un'operazione, l'utente può scegliere di effettuarne un'altra, tranne quando viene premuto il bottone 4: in quel caso il programma del bancomat stampa un messaggio con scritto "Arrivederci" e termina.

Scrivere un programma che rispetti i seguenti requisiti:

- Stampi all'utente un menu con l'elenco delle operazioni;
- Consenta all'utente di compiere un'operazione;
- Se l'operazione è un prelievo o un versamento viene chiesto quanto denaro prelevare e versare, aggiornando il saldo di conseguenza;
- Se la scelta dell'utente non rientra tra quelle possibili viene stampato un messaggio di errore.

Assumiamo, per semplicità che il saldo iniziale sia uguale a 0

##### ESEMPIO 1
```
Benvenuto! 
Seleziona:
1 - Per effettuare un prelievo
2 - Per effettuare un versamento
3 - Per stampare il saldo
4 - Per terminare l'operazione
Inserisci la tua scelta: 2
Inserisci il denaro da versare: 200
VERSAMENTO EFFETTUATO
Inserisci la tua scelta: 1
Inserisci il denaro da prelevare: 50
PRELIEVO EFFETTUATO
Inserisci la tua scelta: 3
Il tuo saldo è pari a 150 Euro
Inserisci la tua scelta: 4
ARRIVEDERCI!
```

##### ESEMPIO 2
```
Benvenuto! 
Seleziona:
1 - Per effettuare un prelievo
2 - Per effettuare un versamento
3 - Per stampare il saldo
4 - Per terminare l'operazione
Inserisci la tua scelta: 5
Errore: scelta non valida.
Inserisci la tua scelta: 3
Il tuo saldo è pari a 0 Euro
Inserisci la tua scelta: 4
ARRIVEDERCI!
```

<!-- ##### [Soluzioni](soluzioni/c/c11.md) -->


## c12. Il distributore di caffè
In un distributore automatico, un caffè costa 50 cent. Il distributore accetta solo monete da 5, 10 e 20 cent.
Scrivere un programma che legga le monete inserite da un cliente e che rispetti i seguenti requisiti:

- accetti solo monete da 5, 10 e 20: se viene inserito un taglio diverso, il distributore stampa un messaggio di errore e chiede di inserire una nuova moneta.
- una volta che la somma delle monete inserite supera i 50 centesimi il programma smette di chiedere di inserire monete.
- se la somma delle monete inserite supera i 50 centesimi viene stampato l'importo dell'eventuale resto.

##### ESEMPIO 1
```
Inserisci una moneta: 5
Inserisci una moneta: 20
Inserisci una moneta: 5
Inserisci una moneta: 20

Caffè erogato
Resto 0 cent.
```
##### ESEMPIO 2
```
Inserisci una moneta: 20
Inserisci una moneta: 20
Inserisci una moneta: 20

Caffè erogato
Resto 10 cent.
```
##### ESEMPIO 3
```
Inserisci una moneta: 20
Inserisci una moneta: 50
Errore: Puoi inserire solo monete da 5, 10 e 20 centeisimi
Inserisci una moneta: 20
Inserisci una moneta: 10

Caffè erogato



<!-- ##### [Soluzioni](soluzioni/c/c13.md) -->

## c14. Somma delle cifre
Scrivi un programma che legga un numero intero positivo e ne calcoli la somma delle cifre . Il programma deve gestire anche il caso in cui l'utente inserisca 0.

##### ESEMPIO 1
```
Inserisci un numero: 12345

La somma delle cifre è 15
```
##### ESEMPIO 2
```
Inserisci un numero: 0

La somma delle cifre è 0
```


## c15. Tabellina
Scrivi un programma che chieda all'utente un numero intero **n** e stampi la tabellina di **n** (i primi 10 multipli).

##### ESEMPIO 1
```
Inserisci un numero: 7

7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70
```


## c16. Vendite
Andrea registra le vendite giornaliere del suo negozio. Scrivi un programma che legga l'ammontare delle vendite giorno per giorno fino a quando non viene inserito un valore negativo. Alla fine stampare:

- il numero di giorni registrati
- il totale delle vendite
- la media giornaliera delle vendite

##### ESEMPIO
```
Inserisci vendite del giorno: 120
Inserisci vendite del giorno: 200
Inserisci vendite del giorno: 0
Inserisci vendite del giorno: 150
Inserisci vendite del giorno: -1

Giorni registrati: 4
Vendite totali: 470
Media giornaliera: 117.5
```


## c17. Numeri perfetti
Un numero perfetto è uguale alla somma dei suoi divisori propri (escluso se stesso). Scrivi un programma che legga un numero **n** e stampi tutti i numeri perfetti minori o uguali a **n** .

##### ESEMPIO
```
Inserisci un numero: 30

6 è un numero perfetto
28 è un numero perfetto
```


## c18. Primo successivo
Scrivi un programma che legga un numero intero **n** e trovi il primo numero primo maggiore di **n** utilizzando un ciclo **while**.

##### ESEMPIO
```
Inserisci un numero: 14

Il primo numero primo maggiore di 14 è 17
```


## c19. Serie geometrica
Scrivi un programma che chieda all'utente i valori iniziale **a**, ragione **r** e numero di termini **k**, e stampi i primi **k** termini di una progressione geometrica usando un ciclo **for**.

##### ESEMPIO
```
Valore iniziale (a): 3
Ragione (r): 2
Numero di termini: 5

3
6
12
24
48
```


## c20. Controllo PIN
Scrivi un programma che chieda all'utente di inserire un PIN (4 cifre) e consenta al massimo 3 tentativi. Se il PIN inserito è corretto il programma stampa "Accesso consentito" e termina; se dopo 3 tentativi non viene inserito il PIN giusto il programma stampa "Accesso negato".

##### ESEMPIO 1
```
Inserisci il PIN: 1234
PIN corretto
Accesso consentito
```
##### ESEMPIO 2
```
Inserisci il PIN: 0000
PIN errato
Inserisci il PIN: 1111
PIN errato
Inserisci il PIN: 2222
PIN errato
Accesso negato
```


## c21. Massimo comune divisore
Scrivi un programma che legga due numeri interi positivi e calcoli il loro massimo comune divisore (MCD) utilizzando l'algoritmo di Euclide.

##### ESEMPIO
```
Inserisci il primo numero: 28
Inserisci il secondo numero: 20

Il MCD è 4
```


## c22. Media di una sequenza
Scrivi un programma che chieda all'utente quanti numeri intende inserire (**n**) e poi legga **n** numeri impiegando un ciclo **for**. Alla fine stampare la media.

##### ESEMPIO
```
Quanti numeri vuoi inserire? 4
Inserisci un numero: 5
Inserisci un numero: 10
Inserisci un numero: 7
Inserisci un numero: 8

La media è 7.5
```


## c23. Deposito con interesse
Mario versa una certa cifra in un conto e decide di calcolare quanto tempo impiegherà il suo capitale ad superare una somma prefissata, sapendo che ogni anno il saldo aumenta del 5% (interesse composto). Scrivi un programma che legga l'importo iniziale e l'obiettivo e stampi il numero di anni necessari a raggiungere l'obiettivo.

##### ESEMPIO
```
Importo iniziale: 1000
Obiettivo: 2000

Ci vorranno 15 anni per raggiungere o superare l'obiettivo
```

## c24. Temperature estreme
Un meteorologo registra le temperature giornaliere finché non inserisce un valore negativo. Scrivi un programma che legga i valori e, al termine, stampi la temperatura massima e minima registrata.

##### ESEMPIO
```
Inserisci la temperatura: 15
Inserisci la temperatura: 22
Inserisci la temperatura: 5
Inserisci la temperatura: -1

Temperatura massima: 22
Temperatura minima: 5
```


## c25. Countdown per razzo
Scrivi un programma che stampi il conto alla rovescia da 10 a 0 usando un ciclo **for**. Al termine scrivi "LANCIO!".

##### ESEMPIO
```
10
9
8
7
6
5
4
3
2
1
0
LANCIO!
```


## c26. Conversione in binario
Scrivi un programma che legga un numero intero positivo e stampi la sua rappresentazione in base 2 utilizzando ripetute divisioni per 2 e un ciclo **while**.

##### ESEMPIO
```
Inserisci un numero: 13

La rappresentazione binaria è 1101
```


## c27. Somma dei dispari
Scrivi un programma che legga un numero **n** e calcoli la somma dei numeri dispari da 1 a **n** usando un ciclo **for**.

##### ESEMPIO
```
Inserisci un numero: 9

La somma dei numeri dispari fino a 9 è 25
```


## c28. Potenza iterativa
Scrivi un programma che legga due numeri interi positivi **base** ed **esponente** e calcoli la potenza usando un ciclo **for** (non usare l'operatore exponent).

##### ESEMPIO
```
Base: 3
Esponente: 4

3^4 = 81
```


## c29. Voti in classe
Un insegnante inserisce i voti degli studenti finché non scrive -1. Scrivi un programma che conti quanti studenti sono promossi (voto >= 6) e quanti bocciati.

##### ESEMPIO
```
Inserisci un voto: 5
Inserisci un voto: 8
Inserisci un voto: 6
Inserisci un voto: 3
Inserisci un voto: -1

Promossi: 2
Bocciati: 2
```


## c30. Sequenza di Collatz
Dato un numero intero positivo, la sequenza di Collatz si ottiene: se il numero è pari si divide per 2, se è dispari si moltiplica per 3 e si aggiunge 1. Ripeti il processo finché non si raggiunge 1. Scrivi un programma che stampi la sequenza.

##### ESEMPIO
```
Inserisci un numero: 6

6
3
10
5
16
8
4
2
1
```


## c31. Minimo comune multiplo
Scrivi un programma che legga due numeri interi positivi e calcoli il loro minimo comune multiplo (mcm) utilizzando un ciclo **while** o **for**.

##### ESEMPIO
```
Inserisci il primo numero: 4
Inserisci il secondo numero: 6

Il mcm è 12
```


## c32. Conteggio cifre
Scrivi un programma che legga un numero intero (positivo o negativo) e stampi quante cifre ha utilizzando un ciclo **while**.

##### ESEMPIO
```
Inserisci un numero: -12345

Il numero ha 5 cifre
```


## c33. Somma dei numeri di una riga
Scrivi un programma che legga una riga di interi separati da spazi e ne calcoli la somma usando un ciclo **for** per scorrere i numeri.

##### ESEMPIO
```
Inserisci una riga di numeri: 3 5 7 2

La somma è 17
```

