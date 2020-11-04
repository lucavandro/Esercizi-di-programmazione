## g1. Quadrato
Creare una classe chiamata *Quadrato*. La classe è costituta da un membro privato chiamato lato e da 3 metodi pubblici:
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