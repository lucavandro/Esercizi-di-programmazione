## d1. Iniziali
Scrivi un programma che data in input una stringa stampi il primo carattere in essa
contenuto

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

Scrivere un programma che data una password in ingresso, stabilisca se essa è sicura oppure no.

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

Spazi e punteggiaura venivano preservati.

Scrivere un programma che dato una stringa contenente un messaggio in chiaro la decodifichi utilizzando le regole stabilite da Giulio Cesare.

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
