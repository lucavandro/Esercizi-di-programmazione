## f1. Anni bisestili
Un anno bisestile è composto da 366 giorni anzichè 365 e si verifica ogni 4 anni. Creare una funzione chiamata anno_bisestile che prenda in input un anno e determini
se è bisestile o meno.

##### ESEMPIO 
```
> anno_bisestile(2016)
True

> anno_bisestile(2018)
False

> anno_bisestile(2020)
True

> anno_bisestile(2015)
False
```

## f2. Teorema di pitagora
Il teorema di Pitagora è una nota formula per calcolare l'ipotenusa di un triangolo rettangolo note le misure dei due cateti.
Creare una funziona chiamata *pitagora* che prende in input le misure di due cateti e restituisca la misura dell'ipotenusa.

##### ESEMPIO 
```
> pitagora(3,4)
5

> pitagora(5,12)
13
```

## f3. Il gioco dei dadi
Vogliamo simulare il lancio dei dadi. Per farlo vogliamo
1. Creare una funzione chiamata *dado* che ritorna un numero casuale compreso tra 1 e 6. 
2. Creare una funzione chiamata *leggi_dadi* che chieda all'utente quanti dadi vuole lanciare e restituisca il risultato sottoforma di numero intero
3. Creare una funzione chiamata *lancia_dadi" che accetta come parametro un numero di dadi e restitutisca un array contenente il risultato dei lanci effettuati
4. Creare una funzione chaimata *calcola_risultato* che accetta come parametro un array di interi e restituisca la somma.
Il programma dovrà inoltre stampare il numero generato dal lancio di ciascun dado e il risultato finale.

##### ESEMPIO 1
```
> Quanti dadi vuoi lanciare?
2
> 5, 4
> Risultato = 9
```

##### ESEMPIO 
```
> Quanti dadi vuoi lanciare?
4
> 3, 2, 6, 1
> Risultato = 12
```


## f4. Compito in classe
Il prof. Furio è amante delle statistiche. Infatti ogni volta che effettua un compito in classe registra i voti dei propri allievi ed effettua una serie di calcoli:
- calcola la media dei voti
- quanti alunni hanno ottenuto un voto sopra la media
- quanti alunni hanno ottenuto un voto sotto la media
- il voto massimo e il voto minimo

Scrivere una funzione chiamata **statistiche** che prenda in input una lista di voti e stampi i dati statistici richiesti dal prof. Furio.


##### ESEMPIO 
```
> voti = [4,6,9,10,2,5,7,8]
> statistiche(voti)
media: 6.375
voti sopra la media: 4
voti sotto la media: 6
voto massimo: 10
voto minimo: 2
```

## f5. Superenalotto
Il superenalotto è un famoso gioco a premi italiano: ogni giocatore può giocare 6 numeri diversi scelti tra 1 e 90. Ogni settimana vengono estratti 6 numeri, sempre compresi tra 1 e 90. 
Se un giocatore indovina almeno 3 numeri tra quelli estratti vince un premio in denaro.

Scrivere una serie di funzioni che simulino il gioco del superenalotto in particolare:
- la funzione **compila_schedina** : che consente all'utente di inserire da tastiera 6 numeri compresi tra 1 e 90. La funzione controlla che i numeri siano esattamente 6, tutti diversi e compresi tra 1 e 90.
Se l'utente inserisce per errore un numero già inserito o non compreso tra 1 e 90, il numero viene chiesto nuovamente. La funzione alla fine ritorna la lista dei numeri inseriti dall'utente.
- la funzione **effettua_estrazione** che ritorna una lista di 6 numeri casuali compresi tra 1 e 90 senza duplicati
- la funzione **controlla_estrazione** che prende in input le liste generate dalle due funzioni precedenti e stampa quanti numeri sono presenti sia nella schedina che nell'estrazione


##### ESEMPIO 
```
> schedina = compila_schedina()
Inserisci un numero: 10
Inserisci un numero: 25
Inserisci un numero: 32
Inserisci un numero: 45
Inserisci un numero: 70
Inserisci un numero: 79
> print(schedina)
[10,25,32,45,70,79]

> estrazione = genera_estrazione()
> print(estrazione)
[10,23,39,45,62,79]

> controlla_estrazione(schedina, estrazione)
3
```

## f6. Persone al parco
Alcune persone sono in fila in un parco. Ci sono alberi tra loro che non possono essere spostati. Il tuo compito è di scrivere una funzione che prenda come parametro una lista simile a questa
```
altezze = [-1, 150, 190, 170, -1, -1, 160, 180]
```
dove i -1 indicano gli alberi, mentre i gli altri numeri indicano le altezze delle persone, e riordinare solo le altezze delle persone, senza toccare gli alberi.

##### ESEMPIO 1 
```
> altezze = [-1, 150, 190, 170, -1, -1, 160, 180]
> ordina(altezze)
[-1, 150, 160, 170, -1, -1, 180, 190]
```

##### ESEMPIO 2 
```
> altezze = [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]
> ordina(altezze)
[1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77]
```
**Suggerimento** ripassa l'algoritmo *bubble sort*


## f8. Verifica indirizzi ip
Un indirizzo IP è una sequenza numerica assegnata a ciascun dispositivo (ad es. Computer, stampante) collegato ad una rete. 
Un indirizzo ip è formato da 4 numeri compresi tra 0 e 255 e separati da un punto.

Ecco alcuni esempi di indirizzi ip validi

**192.168.1.1**
**255.255.0.0**
**192.168.1.1**
**192.168.1.1**

Scrivere una funzione chiamata *valida_IP* che prendere in input una stringa contentente un indirizzo ip e indica se valido oppure no.
##### ESEMPIO 
```
> valida_ip("192.168.1.1")
True

> valida_ip("255.255.255.0")
True

> valida_ip("256.256.255.0")
False

> valida_ip("255.255.255.0.0")
False

> valida_ip("192.168.1")
False

```

## f9. Colloquio di lavoro
Un'azienda sta cercando un programmatore che sia laureato, che abbia meno di 25 anni e che conosca come linguaggio di programmazione
Python. 
Putroppo sono arrivati tanti curriculum e molti di questi non soddisfano i requisiti.
Scrivere una funzione *filtra_cv* che data in input una lista di curriculum (dove ciascun curriculum è rappresentato da un dizionario) restituisca tutti i curriculum
che rispettano i requisiti (laurea, età minore di 25 anni e conoscenza del linguaggio python), come mostrato nell'esempio.


##### ESEMPIO 
```
> curriculum = [
    { "nome": "Mario", "cognome": "Rossi", "anni": 25, "laureato": True, "linguaggi": ["C++", "PHP"] },
    { "nome": "Luca", "cognome": "Verdi", "anni": 32, "laureato": True, "linguaggi": ["Python", "PHP"] },
    { "nome": "Marco", "cognome": "Neri", "anni": 24, "laureato": True, "linguaggi": ["Python", "Javascript"] },
    { "nome": "Antonio", "cognome": "Russo", "anni": 34, "laureato": False, "linguaggi": ["Python", "Javascript"] },
    { "nome": "Maria", "cognome": "Abate", "anni": 22, "laureato": True, "linguaggi": ["Python", "C++"] },
]
> filtra_cv(curriculum)
[
    { "nome": "Marco", "cognome": "Neri", "anni": 24, "laureato": True, "linguaggi": ["Python", "Javascript"] },
    { "nome": "Maria", "cognome": "Abate", "anni": 22, "laureato": True, "linguaggi": ["Python", "C++"] },
]
```

## f10. Menu del bancomat
Creare una funzione che mostri il menu riportato nell'esempio, legga la scelta effettuata dall'utente e ritorni un numero corrispondente.
Se l'utente inserisce un numero non valido, la funzione stampa un messaggio di errore e chiede nuovamente all'utente di inserire un numero


##### ESEMPIO 1
```
> menu()
Digita:
1 - per effettuare un prelievo
2 - per effettuare un versamento
3 - per stampare l'estratto conto
4 - uscire
Quale operazione vuoi effettuare? 3

3
```

##### ESEMPIO 2
```
> menu()
Digita:
1 - per effettuare un prelievo
2 - per effettuare un versamento
3 - per stampare l'estratto conto
4 - uscire
Quale operazione vuoi effettuare? 5
Operazione non valida!
Quale operazione vuoi effettuare? 0
Operazione non valida!
Quale operazione vuoi effettuare? 1

1
```