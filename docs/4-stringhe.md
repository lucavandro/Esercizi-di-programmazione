## d1. Iniziali
Scrivi un programma che data in input una stringa stampi il primo carattere in essa
contenuto

<a href="https://raw.githubusercontent.com/lucavandro/Esercizi-di-programmazione/master/docs/test/d/d1.py" download>Python Tester</a>

##### ESEMPIO 1
```
Inserisci una stringa: Mamma
M
```

##### ESEMPIO 2
```
Inserisci una stringa: pizza
p
```
<!---
##### [Soluzioni](soluzioni/c/c1.md)
-->


## d2. Tagliamo a corto
Giulia dirige un giornale online. I suoi giornalisti però sono troppo prolissi e molto spesso scrivono articoli che hanno un titolo troppo lungo. Giulia decide di fissare la lunghezza massima per un titolo a 25 caratteri compresi gli spazi: tutti i titoli più lunghi verranno abbreviati con 3 puntini sospensivi "..." in modo che titolo abbreviato e 3 puntini sospensivi rientri comunque in un massimo di 25 caratteri.

<a href="https://raw.githubusercontent.com/lucavandro/Esercizi-di-programmazione/master/docs/test/d/d2.py" download>Python Tester</a>

##### ESEMPIO 1
```
Inserisci un titolo: L'Inghilterra vince i mondiali

L'Inghilterra vince i m...
```

##### ESEMPIO 2
```
Inserisci un titolo: L'Italia vince i mondiali

L'Italia vince i mondiali
```
<!--
##### [Soluzioni](soluzioni/c/c2.md)
-->

## d3. Password sicura
Una password è considerata sicura se rispetta tutti i seguenti criteri:
1. La sua lunghezza è di almeno 8 caratteri
2. Al suo interno c'è almeno 1 lettera maiuscola
3. Al suo interno c'è almeno 1 numero
4. Al suo interno c'è almeno 1 carattere speciale tra i seguenti: #, !, $, @, %, ?

Scrivere un programma che data una password in ingresso, ritorni True se la password rispetta tutti i criteri. In caso non rispetti anche solo 1 criterio, ritorna False.

<a href="https://raw.githubusercontent.com/lucavandro/Esercizi-di-programmazione/master/docs/test/d/d3.py" download>Python Tester</a>

##### ESEMPIO 1
```
Inserisci una password: 12345678

La password non è sicura perchè: 
- non contiene lettere maiuscole
- non contine caratteri speciali 
```

##### ESEMPIO 2
```
Inserisci una password: pippo14

La password non è sicura perchè: 
- non è composta da almeno 8 caratteri
- non contiene lettere maiuscole
- non contine caratteri speciali 
```

##### ESEMPIO 3
```
Inserisci una password: Hackme!2

La password è sicura
```
<!--
##### [Soluzioni](soluzioni/c/c3.md)
-->

## d4. Password sicura 2
A volte trovare una password sicura è davvero difficile! Una tecnica comune è quella di prendere una parola comune ed effettuare le seguenti sostituzioni:
- Sostituire tutte le lettere **s** con il carattere **$**
- Sostituire tutte le lettere **a** con il carattere **@**
- Sostituire tutte le lettere **l** con il numero **1**
- Sostituire tutte le lettere **e** con il numero **3**
- Sostituire tutte le lettere **o** con il numero **0**
- Sostituire tutte le lettere **g** con il numero **6**
- Sostituire tutti gli spazi con il carattere "_"

Inoltre se la password non arriva ad 8 caratteri di lunghezza, vengono aggiunti una serie di simboli "#" alla fine della password in modo da raggiungere la lunghezza standard di 8 caratteri.

<a href="https://raw.githubusercontent.com/lucavandro/Esercizi-di-programmazione/master/docs/test/d/d4.py" download>Python Tester</a>

##### ESEMPIO 1
```
Inserisci una parola: pallone

p@110n3#
```

##### ESEMPIO 2
```
Inserisci una parola: bella ciao

b311@_ci@0
```
<!--
##### [Soluzioni](soluzioni/c/c4.md)
-->

## d5. Codice fiscale 1
Un codice fiscale dovrebbe essere composto solo da lettere maiuscole e numeri. Molto spesso gli utenti di un sito web sbagliano a compilare il modulo di iscrizione inserendo il proprio codice fiscale utilizzando le lettere minuscole. 

Scrivere un programma che dato in ingresso un codice fiscale contenente una o più lettere minuscole, stampi il codice fiscale corretto con tutte le lettere maiuscole.

<a href="https://raw.githubusercontent.com/lucavandro/Esercizi-di-programmazione/master/docs/test/d/d5.py" download>Python Tester</a>

##### ESEMPIO 1
```
Inserisci codice fiscale: vpcasd87d09g781k

VPCASD87D09G781K
```

##### ESEMPIO 2
```
Inserisci codice fiscale: VpcasD87D09G781K

VPCASD87D09G781K
```

## d6. Codice fiscale 2
Un codice fiscale è una stringa che risponde alle seguenti caratteristiche:
- è composta da 16 caratteri
- i primi 6 caratteri sono lettere
- il 7° e 8° carattere sono numeri
- il 9° carattere è una lettera
- il 10° e 11° carattere sono numeri
- il 12° carattere è una lettera
- il 13°, 14° e 15° carattere sono numeri
- il 16° carattere è una lettera

Scrivere un programma che dato un codice fiscale stabilisca se è valido oppure no.

<a href="https://raw.githubusercontent.com/lucavandro/Esercizi-di-programmazione/master/docs/test/d/d6.py" download>Python Tester</a>

##### ESEMPIO 1
```
Inserisci codice fiscale: VPCASD87D09G781K

Codice fiscale valido
```

##### ESEMPIO 2
```
Inserisci codice fiscale: VPCASD87D09G781

Codice fiscale NON valido
```

##### ESEMPIO 3
```
Inserisci codice fiscale: V123SD87D09G781K

Codice fiscale NON valido
```

## d7. Codici segreti 1
Giulio Cesare inventò un semplice sistema per rendere i suoi messaggi incomprensibili ai nemici che ne fossero entrati in possesso: sostituiva ogni lettera alfabetica di un messaggio con la successiva.

```
a -> b
b -> c
c -> d
....
z -> a
```

Spazi e punteggiaura venivano preservati. Si considerino solo le lettere dell'alfabeto italiano.

Scrivere un programma che dato una stringa contenente un messaggio in chiaro la decodifichi utilizzando le regole stabilite da Giulio Cesare.

<a href="https://raw.githubusercontent.com/lucavandro/Esercizi-di-programmazione/master/docs/test/d/d7.py" download>Python Tester</a>

##### ESEMPIO 1
```
Inserisci un messaggio: Viva la pizza

Zlzb gb qlaab
```

##### ESEMPIO 2
```
Inserisci un messaggio: Caramella

Dbsbnfmmb
```

## d8. Codici segreti 2
Il codice inventato da Giulio Cesare è molto sicuro infatti nessuno dei suoi nemici è mai riuscito a decifrarlo...ma neanche i suoi amici!

Scrivi un programma per gli amici di Giulio Cesare che data una stringa codificata secondo le regole stabilite nel esercizio precedente, la converta nella sua forma originale.

<a href="https://raw.githubusercontent.com/lucavandro/Esercizi-di-programmazione/master/docs/test/d/d8.py" download>Python Tester</a>

##### ESEMPIO 1
```
Inserisci un messaggio: Zlzb gb qlaab

Viva la pizza
```

##### ESEMPIO 2
```
Inserisci un messaggio: Dbsbnfmmb

Caramella
```

## d9. Al contrario
Scrivere un programma che data una stringa in input, la scriva al contrario ovvero da destra verso sinistra.

<a href="https://raw.githubusercontent.com/lucavandro/Esercizi-di-programmazione/master/docs/test/d/d9.py" download>Python Tester</a>

##### ESEMPIO 1
```
Inserisci una parola: Pizza

azziP
```

##### ESEMPIO 2
```
Inserisci una parola: Cioccolato

'otaloccoiC'
```

## d10. Palindromi
Un palindromo è una parola che può essere scritta al contrario senza cambiare di significato.
Alcuni esempi di palindromo sono le parole: Anna, oro, radar, ossesso.

Scrivere un programma che data una parola stabilisca se è palindroma o meno.

<a href="https://raw.githubusercontent.com/lucavandro/Esercizi-di-programmazione/master/docs/test/d/d10.py" download>Python Tester</a>

##### ESEMPIO 1
```
Inserisci una parola: radar

Radar è una parola parindroma
```

##### ESEMPIO 2
```
Inserisci una parola: pizza

pizza non è una parola palindroma
```

## d11. La lista della spesa
Luca ha lasciato a Caterina la lista della spesa elencando tutti le cose da comprare
una dopo l'altra separandole con una virgola. Per Caterina questa cosa è inaccettabile! La lista della spesa va scritta in modo ordinato, utilizzando una lista numerata per ogni cosa da camporare!

Scrivere un programma che legga un stringa contenente un elenco di parole separate dalla virgola e la trasformi in una lista ordinata come mostrato nell'esampio.

**BONUS** : Ordinare gli alimenti nella lista in ordine alfabetico

##### ESEMPIO 1
```
Inserisci una la lista della spesa: pane, latte, pasta, fette biscottate, marmellata

1. Pane
2. Latte
3. Pasta
4. Fette biscottate
5. Marmellata
```

##### ESEMPIO 1 con bonus
```
Inserisci una la lista della spesa: pane, latte, pasta, fette biscottate, marmellata

1. Fette biscottatePane
2. Latte
3. Marmellata
4. Pane
5. Pasta
```

## d12. Conta parole
Data una stringa di parole separate da uno spazio, creare un programma che conti quante parole sono contenute 
nella stringa.

##### ESEMPIO 1
```
Inserisci una frase: Viva la pizza con la nutella

Parole: 6
```

##### ESEMPIO 2
```
Inserisci una frase: Il dado è tratto

Parole: 4
```

## d13. Conta parole 2
Data una stringa di parole separate da uno spazio, creare un programma che conti quante parole diverse (cioè senza duplicati)sono contenute nella stringa.

##### ESEMPIO 1
```
Inserisci una frase: Viva la pizza con la nutella

Parole: 5
```

##### ESEMPIO 2
```
Inserisci una frase: La la la

Parole: 1
```

## d14. Trova la parola più lungua
Data una stringa di parole separate da uno spazio, creare un programma che trovi all'interno della stringa la parola più lunga (cioè qualla con il maggior numero di caratteri).

##### ESEMPIO 1
```
Inserisci una frase: Viva la pizza con la nutella

Parole più lunga: nutella
```

##### ESEMPIO 2
```
Inserisci una frase: Mary Poppins diceva supercalifragilistichespiralidoso

Parole più lunga: supercalifragilistichespiralidoso
```

## d.15 I numeri narcisistici
Un numero narcisistico (o numero di Armstrong) è un numero positivo che è la somma delle sue stesse cifre, ciascuna elevata alla potenza del numero di cifre in una data base. 

Ad esempio, prendi 153 (3 cifre), che è narcisistico:

    1<sup>3</sup> + 5<sup>3</sup> + 3<sup>3</sup> = 1 + 125 + 27 = 153
e 1652 (4 cifre), che non è:

    1<sup>4</sup> + 6<sup>4</sup> + 5<sup>4</sup> + 2<sup>4</sup> = 1 + 1296 + 625 + 16 = 1938

Il tuo codice deve restituire vero o falso seconda che un numero inserito dall'utente sia narcisistico o meno.

##### ESEMPIO 1
```
Inserisci una numero: 153
True
```

##### ESEMPIO 2
```
Inserisci una numero: 12
False
```

# d.16 Codice alfabetico
Scrivere un programma che legga una stringa e che sostituisca ogni lettera al suo interno con la sua posizione nell'alfabeto (si consideri l'alfabeto italiano). Gli spazi o eventuali caratteri speciali (virgole, punti, apostrofi etc.) vanno ignorati

##### ESEMPIO 1
```
Inserisci una parola: pizza
14 9 21 21 1
```

##### ESEMPIO 2
```
Inserisci una parola: nutella
12 19 18 5 10 10 1
```

# d.17 Encoding CD
"Pit" e "Land" sono caratteristiche fisiche della superficie di un CD che rappresentano dati binari. I "Pit" sono piccoli buchi o scanalature sulla superficie del CD, mentre i "Land" sono aree pianeggianti tra due "Pit" adiacenti.

"Pit" e "Land" non rappresentano direttamente gli zeri e gli uno dei dati binari, ma la codifica avviene nel seguente modo: 
- un passaggio da pit a terra o da terra a fossa indica uno
- nessun cambiamento indica uno zero.

In questo esercizio dovrai creare un programma che chiede in input un numero intero compreso tra 0 e 255 (8 bit) e restituisce:
- la rappresentazione binaria su 8 bit del numero inserito
- la combinazione di "Pit" e "Land" che codificano il numero sottoforma di una stringa, dove le P indicano un Pit e le L un land


##### ESEMPIO 1
Inserisci un numero: 5
Rappresentazione binaria (8 bit): 00000101
"Pit & Land": PPPPPPLLP

# d.18 Alfanumerico
In questo esempio devi convalidare se una stringa di input utente è alfanumerica. 
La stringa deve rispettare le seguenti condizioni per essere alfanumerica:

1. Almeno un carattere ("" non è valido)
2. I caratteri consentiti sono lettere latine maiuscole/minuscole e cifre da 0 a 9
3. Niente spazi bianchi / caratteri di sottolineatura

Nel caso la stringa sia alfanumerica, il programma stampa True, altrimenti stampa False

##### ESEMPI
```
Inserisci una stringa: hello world_
False

Inserisci una stringa: PassW0rd
True

Inserisci una stringa: __ * __
False

Inserisci una stringa: 43534h56jmTHHF3
True
```

# d.19 Il cubo di Rubik 1
Molti appassionati del cubo di Rubik utilizzano una notazione sviluppata da David Singmaster, nota come "notazione di Singmaster", per distinguere i vari movimenti eseguibili sul cubo.
La notazione prevede 12 possibili movimenti:
1. **F** rotazione di 90° in senso orario della faccia frontale
2. **F'** rotazione di 90° in senso anti-orario della faccia frontale
3. **B** rotazione di 90° in senso orario della faccia posteriore
4. **B'** rotazione di 90° in senso anti-orario della faccia posteriore
5. **R** rotazione di 90° in senso orario della faccia di destra
6. **R'** rotazione di 90° in senso anti-orario della faccia di destra
7. **L** rotazione di 90° in senso orario della faccia di sinistra
8. **L'** rotazione di 90° in senso anti-orario della faccia di sinistra
9. **U** rotazione di 90° in senso orario della faccia superiore
10. **U'** rotazione di 90° in senso anti-orario della faccia superiore
11. **D** rotazione di 90° in senso orario della faccia inferiore
12. **D'** rotazione di 90° in senso anti-orario della faccia inferiore

Questa notazione viene utilizzata per descrivere gli algoritmi, che non sono altro che una serie di movimenti che portano alla risoluzione del cubo o di una parte di esso.

Tuttavia negli algoritmi se ci sono due movimenti uguali, uno dopo l'altro, vengono abbreviati. Ad esempio:
- F F diventa F2 (rotazione di 180° della faccia frontale). In questo caso non importa che il senso sia orario o antiorario in quanto una rotazione di 180° produce lo stesso risultato sia che venga fatta in senso orario che in senso antiorario.
- Anche F' F' diventa F2, per i motivi che abbiamo detto sopra.
- Se ci sono due movimenti opposti di seguito, es. F seguito da F' (F F'), che si annullano a vicenda, non vengono considerati, in quanto se si annullano a vicenda sono semplicemente inutili.

