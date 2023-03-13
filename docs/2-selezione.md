# Selezione

## b1. Facciamo ordine
Scrivere un programma che, letti due numeri in ingresso, stampi prima il numero più piccolo, poi quello più grande

##### ESEMPIO
```
Inserisci il primo numero: 9
Inserisci il secondo numero: 6

6
9
```

<!-- ##### [Soluzioni](soluzioni/b/b1.md) -->

## b2. Facciamo ordine 2 
Scrivere un programma che, letti tre numeri in ingresso, li stampi in ordine crescente (cioè dal più piccolo al più grande).

##### ESEMPIO
```
Inserisci il primo numero: 9
Inserisci il secondo numero: 6
Inserisci il terzo numero: 7

6
7
9
```

<!-- ##### [Soluzioni](soluzioni/b/b2.md) -->

## b3. Pari o dispari?
Scrivere un programma che letto un numero in ingresso, stampi se è pari o se è dispari.

##### ESEMPIO 1
```
Inserisci un numero: 9

Dispari
```
##### ESEMPIO 2
```
Inserisci un numero: 4

Pari
```

<!-- ##### [Soluzioni](soluzioni/b/b3.md) -->

## b4. Triangoli
I triangoli possono essere di tre tipi:

* Equilatero: tutti e tre i lati uguali
* Isoscele: due lati uguali
* Scaleno: nessun lato uguale agli altri

Scrivere un programma che legga in ingresso le misure dei lati di un triangolo e stampi:

* il tipo di triangolo (equilatero, isoscele o scaleno)
* la misura del perimetro

##### ESEMPIO
```
Inserisci il primo lato: 4
Inserisci il secondo lato: 9
Inserisci il terzo lato: 4

Il traingolo è isoscele e il suo perimetro misura 17
```

<!-- ##### [Soluzioni](soluzioni/b/b4.md) -->

## b5. Partita di calcio
Scrivere un programma che legga in input i goal segnati dalla squadra di casa e i goal segnati dalla squadra ospite.
Il programma stampa:

- **Vittoria** se la squadra di casa ha vinto
- **Pareggio** se c'è stato un pareggio
- **Sconfitta** se la squadra di casa ha perso

##### ESEMPIO 1
```
Goal segnati dalla squadra di casa: 2
Goal segnati dalla squadra ospite: 1

Vittoria
```

<!-- ##### [Soluzioni](soluzioni/b/b5.md) -->

## b6. Stasera pizza!
Una pizzeria effettua consegne a domicilio. 
Ogni pizza costa 5 Euro ai quali va aggiunto 1 Euro per il costo del trasporto. Se però si ordinano più di 5 pizze, il trasporto è gratuito.
Scrivere un programma che legga in input il numero delle pizze e stampi il totale da pagare comprensivo di eventuale trasporto.

##### ESEMPIO 1
```
Inserisci il numero di pizze: 3

Il totale da pagare è 18 Euro
```
##### ESEMPIO 2
```
Inserisci il numero di pizze: 6

Il totale da pagare è 30 Euro
```

<!-- ##### [Soluzioni](soluzioni/b/b6.md) -->

## b7. Stasera pizza! 2
Una pizzeria effettua consegne a domicilio. 
Ogni pizza costa 5 Euro ai quali va aggiunto 1 Euro per il costo del trasporto. Se però si ordinano più di 5 pizze, il trasporto è gratuito.
Inoltre se il totale supera i 50 euro si ha diritto ad uno sconto del 10%.

Scrivere un programma che legga in input il numero delle pizze e stampi il totale da pagare comprensivo di eventuale trasporto.

##### ESEMPIO 1
```
Inserisci il numero di pizze: 3

Il totale da pagare è 18 Euro
```
##### ESEMPIO 2
```
Inserisci il numero di pizze: 6

Il totale da pagare è 30 Euro
```
##### ESEMPIO 3
```
Inserisci il numero di pizze: 15

Il totale da pagare è 67.5 Euro
```

<!-- ##### [Soluzioni](soluzioni/b/b7.md) -->

## b8. Viaggio a Londra
Pierferdinando, detto Pif, ha deciso di andare per la prima volta nella sua vita a Londra. In Inghilterra però non si usa l'Euro ma la Sterlina. Pif ha bisogno di un programma che gli consenta di convertire i prezzi da Euro a Sterlina e viceversa.

1 Euro = 0.90 Sterline

1 Sterlina = 1.11 Euro 

Scrivere un programma che legga in input:

- Un numero, corrispondente ad un quantità di denaro
- Una lettera (**'E'** per indicare gli euro, **'S'** per le steriline)

se la lettera inserita è:

- la **E**, il programma converte la quantità di denaro da euro in sterline.
- la **S**, il programma converte la quantità di denaro da sterline in euro.

se la lettera inserita non è nel la **E** ne la **S** stampa il messaggio "Errore: moneta sconosciuta"

##### ESEMPIO 1
```
Inserisci quantità di denaro: 100
Inserisci moneta: E

100 Euro sono pari a 90 Sterline
```
##### ESEMPIO 2
```
Inserisci quantità di denaro: 100
Inserisci moneta: S

100 Sterline sono pari a 111 Euro
```
##### ESEMPIO 3
```
Inserisci quantità di denaro: 100
Inserisci moneta: K

Errore: moneta sconosciuta
```

<!-- ##### [Soluzioni](soluzioni/b/b8.md) -->

## b9. Raccolta differenziata
Il comune di Roncofritto ha avviato la raccolta differenziata e vuole progettare un'applicazione
da mettere a disposizione dai cittadini per aiutarli nella raccolta.
Il calendario è il seguente:

| Giorno        | Materiale     | 
| ------------- |:-------------:| 
| Lunedì        | Umido         | 
| Martedì       | Carta         | 
| Mercoledì     | Umido         |  
| Giovedì       | Plastica      | 
| Venerdì       | Umido         | 
| Sabato        | Vetro         | 
| Domenica      | Indifferenziata | 

Scrivere un programma che dato in input il giorno della settimana, stampi il materiale da raccogliere.

##### ESEMPIO 1
```
Inserisci il giorno: giovedì

Il giovedì si raccoglie la plastica.
```

<!-- ##### [Soluzioni](soluzioni/b/b9.md) -->

## b10. Raccolta differenziata 2
L'app sviluppata dal comune di Roncofritto nell'esercizio n.8 ha avuto grandissimo successo!
Ora il comune vuole aggiungere una nuova funzionalità all'app: vuole che l'app prenda in input il nome del materiale e mostri all'utente in che giorno è possibile effettuarne la raccolta.

##### ESEMPIO 1
```
Inserisci il materiale: Plastica

La plastica viene raccolta di giovedì
```
##### ESEMPIO 2
```
Inserisci il materiale: Umido

L'umido viene raccolto il lunedì, il mercoledì e il venerdì.
```

<!-- ##### [Soluzioni](soluzioni/b/b10.md) -->

## b11. Case vacanza
L'agenzia Casalmare affitta case di varie dimensioni e in vari mesi dell'anno e ha bisogno di un'applicazione da pubblicare sul suo sito web per permettere agli utenti di fare un preventivo.
Le tariffe per un giorno di permanenza seguono la seguente tabella.

|                      | Giugno | Luglio | Agosto |
|----------------------|--------|--------|--------|
| **fino a 2 persone** |   30   |   40   |   50   |
| **fino a 4 persone** |   45   |   60   |   75   |
| **fino a 8 persone** |   70   |   90   |   120  |

Scrivere un programma che dati in input:

- il numero di persone
- il mese
- il numero di giorni di permanenza

stampi il costo totale del soggiorno.

Se il numero di persone supera il massimo consentito (cioè 8 persone), o se viene inserito un mese non previsto dalla tabella (ad esempio "Settembre"), stampa un messaggio di errore.

##### ESEMPIO 1
```
Inserisci il numero di persone: 3
Inserisci il mese: Luglio
Inserisci il numero di giorni di permanenza: 10

Il costo totale del soggiorno è di 600 Euro
```
##### ESEMPIO 2
```
Inserisci il numero di persone: 10
Inserisci il mese: Agosto
Inserisci il numero di giorni di permanenza: 10

Non ci sono case disponibili per 10 persone. Il massimo è 8.
```
##### ESEMPIO 3
```
Inserisci il numero di persone: 4
Inserisci il mese: Maggio
Inserisci il numero di giorni di permanenza: 10

Siamo spiacenti: non è possibile prenotare a Maggio, ma solo nei mesi di Giugno, Luglio e Agosto
```
<!-- ##### [Soluzioni](soluzioni/b/b11.md) -->

## b12. Equazioni
Le equazioni di secondo grado sono del tipo

**a** x<sup>2</sup> + **b** x + **c** = 0

I coefficienti **a**, **b** e **c** sono numeri reali e possono essere utilizzati per calcolare un valore detto *discriminante* o ***delta***:

delta = b<sup>2</sup> - 4 ac

Se il delta è un valore maggiore di zero allora l'equazione ha due soluzioni reali e distinte:
 
x<sub>1</sub> = (-b + &radic;delta) / (2a)

x<sub>2</sub> = (-b - &radic;delta) / (2a)

Se il delta è uguale a zero le soluzioni sono coincidenti, cioè hanno lo stesso valore:

x<sub>1</sub> =  x<sub>2</sub> = -b / 2a

Se il delta è minore di zero allora non ci sono soluzioni reali.

Scrivere un programma che letti i coefficienti a,b,c stampi, se esistono, le soluzioni.

#### *Suggerimento* 

Questo esercizio richiede il calcolo della radice quadrata di un numero: questa operazione richiede, per la maggior parte dei linguaggi di programmazione, l'utilizzo di funzioni di libreria. Cerca su Internet come si calcola la radice quadrata nel linguaggio di programmazione che stai imparando. Ad esempio puoi cercare *"come calcolare la radice quadrata in c++"*

##### ESEMPIO 1
```
a: 1
b: -2
c: 1

Il delta è uguale a 0
Le soluzioni sono reali e coincidenti e corrispondono a 
x1=x2=1
```
##### ESEMPIO 2
```
a: 1
b: -5
c: 4

Il delta è uguale a 9
Le soluzioni sono reali e distinte e corrispondono a: 
x1=4
x2=1
```
##### ESEMPIO 3
```
a: 1
b: 1
c: 9

Il delta è uguale a -35
Non esistono soluzioni per questa equazione.
```

<!-- ##### [Soluzioni](soluzioni/b/b12.md) -->

## b13. In perfetta forma!
L'indice di massa corporea o BMI è un valore che ci consente di capire se siamo forma oppure se abbiamo bisogno di perdere o prendere peso.
Il BMI si calcola a partire dall'altezza e dal peso di una persona utilizzando la seguente formula:

BMI = peso / (altezza in metri)<sup>2</sup>

Usando il BMI e la tabella sottostante riusciamo a determinare il nostro status:

| BMI               | Condizione           |
|-------------------|----------------------|
| BMI < 16.5        | GRAVEMENTE SOTTOPESO |
| 16.5 < BMI < 18.5 | SOTTOPESO            |
| 18.5 < BMI < 24.5 | NORMOPESO            |
| 24.5 < BMI < 30   | SOVRAPPESO           |
| 30 < BMI < 34.5   | OBESO                |
| BMI > 14.5        | GRAVEMENTO OBESO     |

Inoltre se la condizione rilevata non è normopeso, il programma calcola anche il peso ideale utilizzando la seguente formula:

peso ideale = (altezza in metri)<sup>2</sup> * 22

##### ESEMPIO 1
```
Inserisci altezza: 1.72
Inserisci peso: 65

Il tuo BMI è 21.97 e la tua condizione è NORMOPESO
```
##### ESEMPIO 2
```
Inserisci altezza: 1.72
Inserisci peso: 50

Il tuo BMI è 16.9 e la tua condizione è SOTTOPESO
Il tuo peso ideale è di 65kg
```

<!-- ##### [Soluzioni](soluzioni/b/b13.md) -->

## b14. Benzina, Ibrido o Elettrico?
Un sito di motori ha deciso di mettere a disposizione dei propri utenti che vogliono acquistare un'auto nuova uno software che li aiuti a sciegliere tra alimentazione a benzina, elettrica e ibrida.
Per il suo funzionamento il software sfrutta la seguente tabella:

|           | Costo per km | Spese fisse |
|-----------|--------------|-------------|
| Benzina   | 0.2          | 1500        |
| Ibrido    | 0.15         | 3000        |
| Elettrico | 0.10         | 4500        |

I costi annuali sono calcolati con la seguente formula:

Costo annuale = km percorsi * costo per km + spese fisse

Dati in input i km percorsi annualmente, il programma stampa i costi annuali per ogni tipo di alimentazione e indica quale alimentazione ha il costo annuale minore

##### ESEMPIO 1
```
Inserisci i km che percorri in un anno: 10000

Benzina:   3500 Euro l'anno
Ibrido:    4500 Euro l'anno
Elettrico: 5500 Euro l'anno
L'alimentazione consigliata è a benzina
```
<!-- ##### [Soluzioni](soluzioni/b/b14.md) -->

## b15. Un po' di geometria
Scrivere un programma che stampi un menu che consenta di scegliere tra 4 forme geometriche:

1. Quadrato
2. Rettangolo
3. Triangolo rettangolo
4. Cerchio

In base alla scelta dell'utente il programma dovrà richiedere all'utente i dati necessari e stampare area e perimetro della forma geometrica scelta.

#### *Suggerimento 1*
Non ricordi come si calcolano area e perimetro di queste forme geometriche? Beh, allora è arrivato il momento di ripassarli! Cerca su Internet le formule e **imparale a memoria!**

#### *Suggerimento 2*
Guarda con attenzione gli esempi per capire come il programma dovrà comportarsi in ogni situazione.

##### ESEMPIO 1
```
Scegli:
1 - Per il quadrato
2 - Per il rettangolo
3 - Per il triangolo rettangolo
4 - Per il cerchio
Indica la tua scelta: 1

Inserisci il lato del quadrato: 2

Il perimetro del quadrato è 8
L'area del quadrato è 4
```
##### ESEMPIO 2
```
Scegli:
1 - Per il quadrato
2 - Per il rettangolo
3 - Per il triangolo rettangolo
4 - Per il cerchio
Indica la tua scelta: 2

Inserisci la base: 3
Inserisci l'altezza: 4

Il perimetro del rettangolo è 14
L'area del rettangolo è 12
```
##### ESEMPIO 3
```
Scegli:
1 - Per il quadrato
2 - Per il rettangolo
3 - Per il triangolo rettangolo
4 - Per il cerchio
Indica la tua scelta: 3

Inserisci il primo cateto: 3
Inserisci il secondo cateto: 4

L'ipotenusa del triangolo è 5
Il perimetro del triangolo è 12
L'area del triangolo è 6
```
##### ESEMPIO 4
```
Scegli:
1 - Per il quadrato
2 - Per il rettangolo
3 - Per il triangolo rettangolo
4 - Per il cerchio
Indica la tua scelta: 4

Inserisci il raggio: 3

La circonferenza del cerchio misura 18.84
L'area del cerchio misura 28.26
```
<!-- ##### [Soluzioni](soluzioni/b/b15.md) -->

## b16. Il focaccione
Il forno "Il focaccione" vende 3 tipi di focaccia:

- Foccaccia bianca
- Focaccia al pomodoro
- Focaccia con le olive

Ogni giorno il proprietario registra, per ogni tipo di focaccia, la percentuale di focaccie vendute, partendo da quella più venduta, a quella meno venduta.
Scrivere un programma che legga in input, per ogni tipo di focaccia, quanti pezzi sono stati venduti e stampi per ognuno di essi la percentuale seguendo un ordine decrescente.

##### ESEMPIO
```
Inserisci il numero di focacce bianche: 3
Inserisci il numero di focacce al pomodoro: 5
Inserisci il numero di focacce alle olive: 2

Focacce al pomodoro 50%
Focacce bianche 30%
Focacce alle olive 20%
```
<!-- ##### [Soluzioni](soluzioni/b/b16.md) -->

## b17. Anni bisestili
Un anno bisestile ha 366 giorni anzichè 365. Ogni 4 anni c'è un anno bisestile.
Gli ultimi anni 3 bisestili sono stati:

- 2016
- 2012
- 2008

Scrivi un programma che legga in input un anno e indichi se è bisestile o meno. Se l'anno **non** è bisestile, il programma indica:

- l'ultimo anno bisestile rispetto a quello inserito
- il prossimo anno bisestile rispetto a quello inserito

##### ESEMPIO 1
```
Inserisci un anno: 2016

Il 2016 è bisestile
```
##### ESEMPIO 2
```
Inserisci un anno: 2019

Il 2019 NON è bisestile
L'ultimo anno bisestile è stato il 2016
Il prossimo anno bisestile sarà il 2020
```
<!-- ##### [Soluzioni](soluzioni/b/b17.md) -->

## b18. Il cappello parlante
Il Cappello Parlante di Harry Potter è un oggetto magico utilizzato nella scuola di Hogwarts per assegnare ogni studente del primo anno ad una dlle quattro casate, cioè  Grifondoro, Tassorosso, Corvonero e Serpeverde.
In realtà il cappello non è così magico come può sembrare: i fondatori di Howgwarts lo hanno programmato con un algoritmo che segue delle regole ben precise:

- Se lo studente è maschio ed è nato tra gennaio e marzo, oppure se è femmina ed è nata tra ottobre e dicembre viene assegnato/a ai **Grifondoro**
- Se lo studente è maschio ed è nato tra aprile e giugno, oppure se è femmina ed è nata tra luglio e settembre viene assegnato/a ai **Tassorosso**
- Se lo studente è maschio ed è nato tra luglio e settembre, oppure se è femmina ed è nata tra aprile e giugno viene assegnato/a ai **Corvonero**
- Se lo studente è maschio ed è nato tra ottobre e dicembre, oppure se è femmina ed è nata tra gennaio e marzo viene assegnato/a ai **Serpeverde**

Scrivi un programma che legga il sesso e il mese di nascita di uno studente e stampi la casata a cui vengono assegnati. 

#### *Suggerimento 1*
Utilizza la lettera M per indicare i maschi, la lettera F per indicare le femmine. Se viene inserita una lettera diversa da M o F stampa un messaggio di errore.

#### *Suggerimento 2*
Utilizza i numeri da 1 a 12 per indicare i mesi dell'anno (1 per Gennaio, 2 per Febbraio e così via...). Se viene inserito un numero non compreso tra 1 e 12 stampa un messaggio di errore

##### ESEMPIO 1
```
Inserisci il sesso (M/F): M
Inserisci il mese di nascita: 2

La tua casa è....GRIFONDORO!
```
##### ESEMPIO 2
```
Inserisci il sesso (M/F): F
Inserisci il mese di nascita: 2

La tua casa è....SERPEVERDE!
```
##### ESEMPIO 3
```
Inserisci il sesso (M/F): k
Inserisci il mese di nascita: 2

ERRORE: k non è un valore valido per il campo sesso
```
##### ESEMPIO 4
```
Inserisci il sesso (M/F): M
Inserisci il mese di nascita: 19 

ERRORE: 19 non è un valore valido per il campo mese di nascita
```
<!-- ##### [Soluzioni](soluzioni/b/b18.md) -->

## b19. Supereroi
Ogni supereroe ha il suo alter-ego. Dai un'occhiata alla tabella qui sotto:

| Supereroe  | Vero nome    |
|------------|--------------|
| Spider-man | Peter Parker |
| Batman     | Bruce Wayne  |
| Superman   | Clark Kent   |
| Iron-man   | Tony Stark   |
| Hulk       | Bruce Banner |
| Wolverine  | Logan        |

Scrivi un programma che legga in input il nome di un supereroe e stampi il suo vero nome **e viceversa**.

##### ESEMPIO 1
```
Inserisci il nome: Spider-man

Il vero nome di Spider-man è Peter Parker
```
##### ESEMPIO 2
```
Inserisci il nome: Bruce Wayne

Bruce Wayne è Batman!
```
<!-- ##### [Soluzioni](soluzioni/b/b19.md) -->

## b20. Bim, bum, bam!
Hai mai giocato al gioco  **Bim, bum, bam** (detto anche **pari o dispari**)?  Due giocatori chiudono la mano a pugno: uno di essi si dichiara "pari", e l'altro risponde dichiarandosi "dispari"  (*o viceversa*). I due giocatori quindi aprono contemporaneamente la mano, mostrando con le dita un numero da 1 a 5. Se la somma dei due numeri mostrati è pari, vince il giocatore che aveva dichiarato "pari", e viceversa.
Prova a ricreare questo gioco utilizzando il computer come avversario, secondo la seguente modalità:
- L'utente inserisce da tastiera un numero compreso tra 1 e 5 (*se l'utente inserisce un numero errato viene stampato un messaggio di errore*)
- L'utente sceglie se essere pari o dispari
- Il computer genera un numero a caso tra 1 e 5
- Alla fine il programma ti dirà se hai vinto o hai perso

##### ESEMPIO 1
```
Inserisci un numero tra 1 e 5: 2
Vuoi essere pari o dispari?(P/D): P

Hai scelto di essere pari
Il computer sarà dispari
Il numero scelto dal computer è 3
La somma è 5
Mi dispiace...HAI PERSO
```
##### ESEMPIO 2
```
Inserisci un numero tra 1 e 5: 4
Vuoi essere pari o dispari?(P/D): D

Hai scelto di essere dispari
Il computer sarà pari
Il numero scelto dal computer è 5
La somma è 9
Complimenti! HAI VINTO!
```
##### ESEMPIO 3
```
Inserisci un numero tra 1 e 5: 7

Errore: puoi inserire solo numeri compresi tra 1 e 5
```
<!-- ##### [Soluzioni](soluzioni/b/b20.md) -->

## b21. Morra cinese (Carta, Sasso, Forbici)
Hai mai giocato alla **morra cinese** (detto anche **Carta, Sasso, Forbici**)?  Due giocatori chiudono la mano a pugno e contemporaneamente la riaprono mostrando uno dei sequenti segni: 

- mano aperta (**Carta**) 🫱
- mano chiusa (**Sasso**)👊
- mano chiusa con indice e medio estesi a formare una "V" (**Forbici**)✌️

Lo scopo è sconfiggere l'avversario scegliendo un segno in grado di battere quello dell'altro, secondo le seguenti regole:

- sasso batte forbici
- forbici batte carta
- carta batte sasso

Se i giocatori mostrano lo stesso segno c'è un pareggio.

Prova a ricreare questo gioco utilizzando il computer come avversario, secondo la seguente modalità:

- L'utente sceglie una mossa
- Il computer, utilizzando un numero casuale, risponde con la sua contromossa
- Alla fine il programma ti dirà se hai vinto o hai perso

##### ESEMPIO 1
```
Fai la tua mossa! 
1 - Per carta
2 - Per sasso
3 - Per forbici
Scegli: 2

Hai scelto SASSO
Il computer ha scelto FORBICI
Sasso batte forbici
Complimenti! Hai vinto!
```
##### ESEMPIO 2
```
Fai la tua mossa! 
1 - Per carta
2 - Per sasso
3 - Per forbici
Scegli: 3

Hai scelto FORBICI
Il computer ha scelto SASSO
Sasso batte forbici
Mi dispiace hai perso
```
##### ESEMPIO 3
```
Fai la tua mossa! 
1 - Per carta
2 - Per sasso
3 - Per forbici
Scegli: 3

Hai scelto FORBICI
Il computer ha scelto FORBICI
Pareggio!
```
##### ESEMPIO 4
```
Fai la tua mossa! 
1 - Per carta
2 - Per sasso
3 - Per forbici
Scegli: 4

Errore: 4 non è una scelta valida
```
<!-- ##### [Soluzioni](soluzioni/b/b21.md) -->

## b22. Testa o croce
A volte l'indecisione è una sensazione logorante: meglio lasciare la decisione al fato!
Scriviamo un programma che, utilizzando i numeri casuali, simuli il lancio di una monetina, stampando in maniera del tutto casuale la parola "Testa" o la parola "Croce"

#### *Nota*
In alcuni linguaggi di programmazione, potrebbe non essere necessario utilizzare if/else o altri operatori di selezione.

##### ESEMPIO 1
```
Testa
```
##### ESEMPIO 2
```
Croce
```
<!-- ##### [Soluzioni](soluzioni/b/b22.md) -->

## b23. La Pasqua
Nel 1800 il matematico tedesco Carl Friedrich Gauss (❤️) inventò un algoritmo per calcolare la data della Pasqua.

L'algoritmo funziona nel seguente modo:
L'anno di cui si calcola la Pasqua sia contrassegnato da Y; mod è l'operatore modulo che restituisce il resto della divisione fra numeri interi (ad esempio, 13 mod 5 = 3 perché 13 diviso 5 fa 2 con resto 3).

Si calcolano dapprima a, b e c nel seguente modo:

a = Y mod 19
b = Y mod 4
c = Y mod 7

Poi si calcolano

d = (19a + M) mod 30
e = (2b + 4c + 6d + N) mod 7

Dove M e N vanno calcolati secondo la seguente tabella
| Anni      | M  | N|
|-----------|----|----|
| 1583-1699 | 22 | 2 |
| 1700-1799 | 23 | 3 |
| 1800-1899 | 23 | 4 |
| 1900-2099 | 24 | 5 |
| 2100-2199 | 24 | 6 |
| 2200-2299 | 25 | 0 |
| 2300-2399 | 26 | 1 |
| 2400-2499 | 25 | 1 |


Se (d + e) < 10, allora la Pasqua cade il giorno (d + e + 22) del mese di marzo, altrimenti si verificherà il (d + e − 9)-esimo giorno del mese di aprile.

Scrivere un programma che legga in input l'anno e calcoli la data della Pasqua sfruttando l'algoritmo di Gauss.


##### ESEMPIO 1
```
Inserisci l'anno: 1987
19 aprile 1987
```

<!-- ##### [Soluzioni](soluzioni/b/b22.md) -->