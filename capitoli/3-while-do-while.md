# While / do-while

1. [Contiamo!](#contiamo)
2. [Contiamo al contrario!](#contiamo-al-contrario)
3. [Contiamo 2](#contiamo-2)
4. [Contiamo 3](#contiamo-3)
5. [I numeri di Fibonacci](#i-numeri-di-fibonacci)
6. [C'è posta per te](#cè-posta-per-te)
7. [Consegne a domicilio](#consegne-a-domicilio)
8. [Il fattoriale](#il-fattoriale)
9. [Indovina il numero](#indovina-il-numero)
10. [Indovina il numero 2](#indovina-il-numero-2)
11. [Il bancomat](#il-bancomat)
12. [Il distributore di caffè](#il-distributore-di-caffè)
13.  [Il distributore di caffè 2](#il-distributore-di-caffè-2)

## 1. Contiamo!
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
## 2. Contiamo al contrario!
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
## 3. Contiamo! 2
Scrivi un programma che stampi i numeri da 1 ad un numero **n** inserito dall'utente.

##### Attenzione!
Assicurati che l'utente inserisca un numero maggiore di 0 o il tuo programma potrebbe comportarsi in modo *"inaspettato"*

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
Errore: Devi inserire un numero maggiore di 0
Inserisci un numero: 33

1
2
3
...
32
33
```

## 4. Contiamo! 3
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
## 5. I numeri di Fibonacci
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
## 6. C'è posta per te
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

## 7. Consegne a domicilio
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

## 8. Il fattoriale
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
## 9. Indovina il numero
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

## 10. Indovina il numero 2
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


## 11. Il bancomat
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

## 12. Il distributore di caffè
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
Resto 0 cent.
```
## 13. Il distributore di caffè 2
In un distributore automatico:

- un caffè costa 50 cent. 
- un caffè decaffeinato costa 60 cent.
- un tè costa 40 cent.
- una cioccolata calda costa 70 cent.

Il distributore accetta solo monete da 5, 10 e 20 cent.
Scrivere un programma che chieda al cliente di selezionare una bevanda, mostri il costo della bevanda selezionata e legga le monete inserite e che rispetti i seguenti requisiti:

- Se la scelta della bevanda non rientra fra quelle disponibili, il programma stampa un messaggio di errore e mostra nuovamente l'elenco delle bevande disponibili.
- accetti solo monete da 5, 10 e 20: se viene inserito un taglio diverso, il distributore stampa un messaggio di errore e chiede di inserire una nuova moneta.
- una volta che la somma delle monete inserite raggiunge il costo della bevanda, il programma smette di chiedere di inserire monete.
- se la somma delle monete inserite supera il costo della bevanda,viene stampato l'importo dell'eventuale resto.

##### ESEMPIO 1
```
1 - Caffè
2 - Decaffeinato
3 - Tè
4 - Cioccolata calda
Seleziona la tua bevanda: 3
Il costo del tè è di 40 centesimi
Inserisci una moneta: 5
Inserisci una moneta: 20
Inserisci una moneta: 5
Inserisci una moneta: 10

Tè erogato
Resto 0 cent.
```
##### ESEMPIO 2
```
1 - Caffè
2 - Decaffeinato
3 - Tè
4 - Cioccolata calda
Seleziona la tua bevanda: 6
Errore: nessuna bevanda disponibile con il numero 6
1 - Caffè
2 - Decaffeinato
3 - Tè
4 - Cioccolata calda
Seleziona la tua bevanda: 2
Il costo del decaffeinato è di 60 centesimi

Inserisci una moneta: 20
Inserisci una moneta: 20
Inserisci una moneta: 20

Caffè decaffeinato erogato
Resto 0 cent.
```