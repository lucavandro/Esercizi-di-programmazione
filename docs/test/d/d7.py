def codici_segreti1(word):
    # SCRIVI IL TUO CODICE QUI SOTTO
    return ...

"""
NON MODIFICARE QUESTA SEZIONE
"""
if __name__ == "__main__":
    from colorama import Fore, Style

    test = [
        { "i" : "viva la pizza", "o": "zlzb mb qlaab"},
        { "i" : "hanno ucciso l'uomo ragno", "o": "iboop vddltp m'vpnp sbhop"},
        { "i" : "nel mezzo del cammin di nostra vita",  "o": "ofm nfaap efm dbnnlo el optusb zlub"},
        { "i" : "mi illumino d'immenso", "o": "nl lmmvnlop e'lnnfotp"},
        { "i" : "sempre caro mi fu quest'ermo colle", "o": "tfnqsf dbsp nl gv rvftu'fsnp dpmmf"},
        { "i" : "ei fu siccome immobile", "o": "fl gv tlddpnf lnnpclmf"},
    ]

    for i, t in enumerate(test):
        output = codici_segreti1(t["i"]) 
        expected_output = t["o"]

        if output == expected_output:
            print(f"{Fore.GREEN}TEST {i+1} / {len(test)} : SUPERATO {Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}TEST {i+1} / {len(test)} : FALLITO {Style.RESET_ALL}")
            print(f"INPUT : {t['i']}")
            print(f"OUTPUT ATTESO : {expected_output}")
            print(f"OUTPUT PRODOTTO : {output}")