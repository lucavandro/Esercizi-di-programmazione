# Input/Output

## a1. Precedente e successivo
Scrivere un programma che, letto un numero in ingresso, stampi il precedente e il successivo

##### ESEMPIO
```
Inserisci un numero: 2

Precedente 1
Successivo 3
```
##### [Soluzioni](soluzioni/a/a1.md)


## a2. Il quadrato
Scrivere un programma che, letto un numero in ingresso, stampi il suo quadrato

##### ESEMPIO
```
Inserisci un numero: 3

Il quadrato di 3 è 9
```

##### [Soluzioni](soluzioni/a/a2.md)

## a3. Il rettangolo
Scrivere un programma che legga in input la base e l'altezza di un rettangolo e stampi il suo perimetro

##### ESEMPIO
```
Inserisci base: 3
Inserisci altezza: 5

Perimetro = 16
Area = 15
```

##### [Soluzioni](soluzioni/a/a3.md)

## a4. La classifica del campionato
Nelle competizioni calcistiche ad ogni squadra vengono assegnati 3 punti per ogni vittoria,1 punto per ogni pareggio, 0 punti per ogni sconfitta. Scrivi un programma che legga il numero di vittorie, il numero di pareggi e il numero di sconfitte di una squadra di calcio e stampi quanti punti ha ottenuto in totale.

##### ESEMPIO
```
Inserisci il numero di vittorie: 3
Inserisci il numero di pareggi: 4
Inserisci il numero di sconfitte: 0

Punti totali 13
```

##### [Soluzioni](soluzioni/a/a4.md)

## a5. Il consumo di un'auto
Un'automobile consuma 5 litri per percorrere 100km. Un litro di benzina costa 1.6 Euro. Dato in input la lunghezza di un tragitto espressa in km, calcolare e stampare:
- quanti litri di benzina vengono consumati dall'auto
- il costo totale dei litri di benzina consumati

##### ESEMPIO 
```
Inserisci il numero di km da percorrere: 150

Litri di benzina consumati 7.5
Costo totale del carburante 12 Euro
```

##### [Soluzioni](soluzioni/a/a5.md)


## a6. Il consumo di un'auto 2
Scriviamo un programma che calcoli i consumi di un'automobile. Vengono dati in input

- il consumo espresso come litri ogni 100km
- il costo di un litro di carburante
- la lunghezza di un tragitto espressa in km

Calcolare e stampare:

- quanti litri di benzina vengono consumati dall'auto
- il costo totale dei litri di benzina consumati 

##### ESEMPIO
```
Quanti km devi percorrere? 150
Quanti litri consuma ogni 100km? 4
Quanto costa 1 litro di carburante? 1.4

Litri di benzina consumati 6
Costo totale del carburante 8.4 Euro
```

##### [Soluzioni](soluzioni/a/a6.md)


## a7. Calorie
Ogni cibo è composto da carboidrati, proteine e grassi:

- Ogni grammo di carboidrati fornisce 3.8 kcal
- Ogni grammo di proteine fornisce 4kcal
- Ogni grammo di grassi fornisce 9 kcal

Scrivere un programma che legga i valori nutrizionali di un alimento e in particolare:

- i grammi di carboidrati
- i grammi di proteine
- i grammi di grassi

e calcoli quante kcal apporta quell'alimento

##### ESEMPIO
```
Inserisci i grammi di carboidrati: 10
Inserisci i grammi di proteine: 2
Inserisci i grammi di grassi: 3

Apporto calorico 73kcal
```

##### [Soluzioni](soluzioni/a/a7.md)


## a8. Teorema di Pitagora
Il teorema di Pitagora è una nota formula che consente di calcolare la lunghezza dell'ipotenusa, conoscendo la misura dei due cateti.

Scrivi un programma che legga la misura dei due cateti e calcoli la misura dell'ipotenusa

###### *Suggerimento n.1* 
Se non ricordi il teorema di Pitagora e la sua formula, cercala su Internet (**e imparala a memoria!**)

###### *Suggerimento n.2* 
Il teorema di Pitagora richiede il calcolo della radice quadrata di un numero: questa operazione richiede, per la maggior parte dei linguaggi di programmazione, l'utilizzo di funzioni di libreria. Cerca su Internet come si calcola la radice quadrata nel linguaggio di programmazione che stai imparando. Ad esempio, puoi cercare *"come calcolare la radice quadrata in c++"*

##### ESEMPIO
```
Inserisci la misura del primo cateto: 4
Inserisci la misura del secondo cateto: 3

L'ipotenusa misura 5
```

##### [Soluzioni](soluzioni/a/a8.md)


## a9. Saldi
Durante la stagione dei saldi, un negozio ha bisogno di un programma per aggiornare i prezzi dei suoi prodotti.

Scrivere un programma che legga in input:

- il costo di un prodotto
- la percentuale di sconto applicata

e calcoli il prezzo del prodotto una volta scontato.

##### ESEMPIO
```
Inserisci il prezzo del prodotto: 100
Inserisci la percentuale di sconto: 30

Il prezzo scontato è 70 Euro
```

##### [Soluzioni](soluzioni/a/a9.md)

## a10. Saldi 2
Finita la stagione dei saldi, un negozio ha bisogno di un programma per rimuovere lo sconto dai prezzi dei suoi prodotti e riportarli al prezzo originario.

Scrivere un programma che legga in input:

- il costo di un prodotto scontato
- la percentuale di sconto applicata

e calcoli il prezzo del prodotto originario.

##### ESEMPIO
```
Inserisci il prezzo scontato: 70
Inserisci la percentuale di sconto: 30

Il prezzo originario è 100 Euro
```

##### [Soluzioni](soluzioni/a/a10.md)


## a11. Le divisioni alle elementari
Che bei tempi quelli delle scuole elementari! Ricordi quando facevi le divisioni? 7 / 2 non faceva ancora 3.5, ma il risultato giusto era 3 con il resto di 1.

Proviamo a creare un programma che effettui la divisione di due numeri e calcoli:
- il quozione *(mi raccomando: rigorosamente senza virgola!)*
- il resto

###### *Suggerimento*
Per calcolare il resto avrai bisogno di un operatore detto ***modulo*** che nella maggior parte dei linguaggi di programmazione è rappresentato dal simbolo **%**. Cerca l'operatore modulo su Internet e informati sul suo funzionamento.

##### ESEMPIO
```
Inserisci il dividendo: 7
Inserisci il divisore: 2

Il quoziente è 3
Il resto è 1
```

##### [Soluzioni](soluzioni/a/a11.md)

## a12. Peso ideale
Esistono vari modi per calcolare il peso ideale di una persona. Uno di questi utilizza la seguente formula

peso ideale = (altezza in metri)<sup>2</sup> * 22

Scrivere un programma che calcoli il peso ideale utilizzando questa formula.

##### ESEMPIO
```
Inserisci altezza: 1.70

Il tuo peso ideale è 63.58 kg
```

##### [Soluzioni](soluzioni/a/a12.md)

## a13. Maratona TV
Caterina e Luca sono grandi appassionati di serie tv. Questo weekend vogliono vedere una serie TV ma vorrebbero sapere quante ore saranno neccessarie per vedere tutti gli episodi di tutte le
stagioni.

Scrivere un programma che prenda in input:

- il numero di stagioni
- il numero di episodi per stagione *(tutte le stagioni hanno lo stasso numero di episodi)*
- la durata in minuti di un singolo episodio *(tutti gli episodi hanno la stessa durata)*

e stampi quante ore e quanti minuti saranno necessari per vedere tutti gli episodi di tutte le stagioni.

##### ESEMPIO
```
Inserisci il numero di stagioni: 4
Inserisci il numero di episodi per ogni stagione: 12
Inserisci la durata di ogni episodio (in minuti): 42

Per vedere l'intera serie saranno necessarie 33 ore e 36 minuti
```

##### [Soluzioni](soluzioni/a/a13.md)

## a14. Somma dei numeri da 1 a n
Scrivere un programma che dato in input un numero n, stampi la somma dei numeri da 1 a n.

###### *Incoraggiamento*
Pensi sia un programma troppo difficile? Pensa che nel 1785, un bambino di 8 anni di nome Carl Friedrich Gauss, riuscì a fare la somma dei numeri da 1 a 100 in pochi secondi e senza usare computer o calcolatrici! Vuoi scoprire come ha fatto? Cerca su Internet la sua storia! Sarà un ottimo aiuto per comprendere come scrivere questo programma.

##### ESEMPIO
```
Inserisci un numero: 100

La somma dei numeri da 1 a 100 è 5050
```
##### [Soluzioni](soluzioni/a/a14.md)

## a15. Numeri a caso
Scrivere un programma che stampi un numero a caso compreso tra un valore minimo e un valore massimo forniti in input.

###### *Suggerimento*
Per generare dei numeri casuali ogni linguaggio di programmazione utilizza una specifica libreria. Cerca su Internet maggiori informazioni. Ad esempio puoi cercare "Come generare numeri casuali in Python"

##### ESEMPIO 1a
```
Inserisci il minimo: 10
Inserisci il massimo: 20

Il numero generato è 13
```
##### ESEMPIO 1b
```
Inserisci il minimo: 10
Inserisci il massimo: 20

Il numero generato è 18
```

##### [Soluzioni](soluzioni/a/a15.md)

## a16. Il birrificio
Il birrificio "ScaccoMalto" acquista dai suoi clienti le bottiglie di birra vuote a 10 centesimi l'una.
I clienti devono riportare le bottiglie in negozio all'interno di apposite confezioni, ciascune contenente 6 bottiglie. Le confezioni non complete, cioè quelle che non contengono esattamente 6 bottiglie, non verranno accettate dal birrificio.

Scrivere un programma che prenda in input un numero di bottiglie e stampi:

- il numero di cassette che verranno riempite
- il prezzo pagato per le bottiglie consegnate
- il numero di bottiglie che, non completando una cassetta da 6, non potranno essere consegnate.

##### ESEMPIO 1
```
Inserisci il numero di bottiglie: 60

Con 60 bottiglie riempirai 10 cassette
Il prezzo pagato sarà di 6 euro
Avanzano 0 bottiglie
```
##### ESEMPIO 2
```
Inserisci il numero di bottiglie: 64

Con 64 bottiglie riempirai 10 cassette
Il prezzo pagato sarà di 6 euro
Avanzano 4 bottiglie
```
##### [Soluzioni](soluzioni/a/a16.md)

## a17. Gradi e radianti
Gli angolo possono essere misurati sia in gradi che radianti. 180 gradi equivalgono a circa 3.14 radianti.
Scrivere un programma che dato in input la misura di un angolo espresso in **gradi**, calcoli la misura corrispondente in **radianti**.

##### ESEMPIO 1
```
Inserisci la misura di un angolo in gradi: 90

90 gradi equivalgono a circa 1.57 radianti
```
##### [Soluzioni](soluzioni/a/a17.md)

## a18. Gradi e radianti 2
Gli angolo possono essere misurati sia in gradi che radianti. 180 gradi equivalgono a circa 3.14 radianti.
Scrivere un programma che dato in input la misura di un angolo espresso in **radianti**, calcoli la misura corrispondente in **gradi**.

##### ESEMPIO 1
```
Inserisci la misura di un angolo in radianti: 1

1 radianti equivalgono a circa 57.32 gradi
```

##### [Soluzioni](soluzioni/a/a18.md)

## a19. Basket
In una partita di basket i punti vengono assegnati secondo le seguenti regole:
- **1 punto** per ogni canestro segnato da tiro libero
- **2 punti** per ogni canestro segnato dall'interno dell'area
- **3 punti** per ogni canestro segnato da fuori area

Scrivere un programma che, dati i numeri di canestri segnati da ciascuna posizione, stabilisca il punteggio totale.

##### ESEMPIO 1
```
Canestri da tiro libero: 2
Canestri dall'interno dell'area: 4
Canestri da fuori area: 2

I punti totali sono 16
```

##### [Soluzioni](soluzioni/a/a19.md)


