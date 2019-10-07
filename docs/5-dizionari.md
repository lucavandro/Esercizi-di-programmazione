## e1. La pizzeria
Una pizzeria espone il seguente menu

| Pizza       | Costo |
|-------------|-------|
| Margherita  | 4.00  |
| Marinara    | 3.60  |
| Capricciosa | 5.00  |
| Bufalina    | 4.50  |
| Bianca      | 3.50  |
| Calzone     | 4.20  |
| Birra       | 3.20  |
| Acqua       | 1.20  |
| Coca-cola   | 2.30  |

Scrivere un programma che, utilizzando un dizionario, legga in input il nome di un prodotto e stampi il suo costo. Il programma deve accettare il nome del prodotto indipendemente da come vengono usate le lettere minuscole o maiuscole, come mostrato negli esempi.

##### ESEMPIO 1
```
Inserisci una prodotto: Margherita
4.00
```

##### ESEMPIO 2
```
Inserisci una prodotto: margherita
4.00
```

##### ESEMPIO 3
```
Inserisci una prodotto: ACQUA
1.20
```

## e2. La pizzeria 2
Una pizzeria espone il seguente menu

| Pizza       | Costo |
|-------------|-------|
| Margherita  | 4.00  |
| Marinara    | 3.60  |
| Capricciosa | 5.00  |
| Bufalina    | 4.50  |
| Bianca      | 3.50  |
| Calzone     | 4.20  |
| Birra       | 3.20  |
| Acqua       | 1.20  |
| Coca-cola   | 2.30  |

Scrivere un programma che, utilizzando un dizionario, legga in input una lista di prodotti separati da uno spazio e stampi il costo totale dei prodotti. Il programma deve accettare il nome del prodotto indipendemente da come vengono usate le lettere minuscole o maiuscole, come mostrato negli esempi.

##### ESEMPIO 1
```
Inserisci i prodotti: margherita acqua
TOTALE: 5.20
```

##### ESEMPIO 2
```
Inserisci i prodotti: calzone margherita birra
TOTALE: 11.40
```

## e4. Il gioco della chimica
A ogni elemento della tavola periodica corrisponde un simbolo. Ad esempio l'idrogeno ha il simbolo H, l'ossigeno la O,
l'oro Au e così via.

Consideriamo i seguenti elementi

| Elemento | Simbolo   |
|----------|-----------|
| Argento  | Ag        |
| Azoto    | N         |
| Calcio   | Ca        |
| Carbonio | C         |
| Cloro    | Cl        |
| Elio     | He        |
| Ferro    | Fe        |
| Fluoro   | F         |
| Idrogeno | H         |
| Iodio    | I         |
| Magnesio | Mg        |
| Mercurio | Hg        |
| Neon     | Ne        |
| Oro      | Au        |
| Ossigeno | O         |
| Potassio | K         |
| Rame     | Cu        |
| Sodio    | Na        |
| Titanio  | Ti        |
| Zinco    | Zn        |
| Zolfo    | S         |

Creare un gioco che, utilizzando un dizionario, chieda all'utente di inserire il simbolo di ciascun elemento.
Se l'utente sbaglia, il gioco inizia da capo. Il gioco termina quando l'utente risponde a tutte le domande.

##### ESEMPIO 1
```
Inserisci il simbolo dell'argento: Ag
Inserisci il simbolo dell'azoto: N
Inserisci il simbolo del calcio: C
Sbagliato!
Inserisci il simbolo dell'argento: Ag
Inserisci il simbolo dell'azoto: N
Inserisci il simbolo del calcio: Ca
Inserisci il simbolo del Carbonio: C
....
```

### Bonus
Alla fine del gioco stampare il tempo impegato per rispondere correttamente a tutte le domande.


## e5. Il gioco della chimica 2
A ogni elemento della tavola periodica corrisponde un simbolo. Ad esempio l'idrogeno ha il simbolo H, l'ossigeno la O,
l'oro Au e così via.

Consideriamo i seguenti elementi

| Elemento | Simbolo   |
|----------|-----------|
| Argento  | Ag        |
| Azoto    | N         |
| Calcio   | Ca        |
| Carbonio | C         |
| Cloro    | Cl        |
| Elio     | He        |
| Ferro    | Fe        |
| Fluoro   | F         |
| Idrogeno | H         |
| Iodio    | I         |
| Magnesio | Mg        |
| Mercurio | Hg        |
| Neon     | Ne        |
| Oro      | Au        |
| Ossigeno | O         |
| Potassio | K         |
| Rame     | Cu        |
| Sodio    | Na        |
| Titanio  | Ti        |
| Zinco    | Zn        |
| Zolfo    | S         |

Creare un gioco che, utilizzando un dizionario, chieda all'utente di inserire l'elemento di ciascun simbolo.
Se l'utente sbaglia, il gioco inizia da capo. Il gioco termina quando l'utente risponde a tutte le domande.

##### ESEMPIO 1
```
A che elemento corrisponde Ag? Argento
A che elemento corrisponde N? Azoto
A che elemento corrisponde C? Calcio
Sbagliato!
A che elemento corrisponde Ag? Argento
A che elemento corrisponde N? Azoto
A che elemento corrisponde C? Carbonio
A che elemento corrisponde Ca? Calcio
....
```
### Bonus
Alla fine del gioco stampare il tempo impegato per rispondere correttamente a tutte le domande.

## e6. Capoluoghi di regione
Ogni regione ha il suo capoluogo di provincia. Ricordarli tutti non è semplice, per questo motivo andremo a creare
un piccolo gioco che ci aiuterà ad impararli.

Il gioco sceglie a caso una regione e chiede all'utente di inserire il nome del relativo capoluogo di provincia:
se l'utente risponde correttamente guadagna 1 punto, se sbaglia invece ottiene 0 punti.

Il gioco va avanti fino a quando l'utente non raggiunge 10 punti.

Ogni volta che l'utente fornisce una risposta, il gioco gli dice se è giusta o sbagliata e stampa il riepilogo dei punti.

| Regione               | Capoluogo  |
|-----------------------|------------|
| Abruzzo               | L'Aquila   |
| Basilicata            | Potenza    |
| Calabria              | Catanzaro  |
| Campania              | Napoli     |
| Emilia-Romagna        | Bologna    |
| Friuli-Venezia Giulia | Trieste    |
| Lazio                 | Roma       |
| Liguria               | Genova     |
| Lombardia             | Milano     |
| Marche                | Ancona     |
| Molise                | Campobasso |
| Piemonte              | Torino     |
| Puglia                | Bari       |
| Sardegna              | Cagliari   |
| Sicilia               | Palermo    |
| Trentino-Alto Adige   | Trento     |
| Umbria                | Perugia    |
| Valle d'Aosta         | Aosta      |
| Veneto                | Venezia    |

##### ESEMPIO 1
```
---------------------------------------------
Inserisci il capoluogo della Campania: Napoli

Esatto! Totale punti: 1
----------------------------------------------

----------------------------------------------
Inserisci il capoluogo della Sicilia: Milano

Sbagliato! Totale punti: 1
----------------------------------------------

----------------------------------------------
Inserisci il capoluogo della Liguria: Genova

Esatto! Totale punti: 2
----------------------------------------------
...
```
