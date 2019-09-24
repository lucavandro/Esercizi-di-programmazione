def codici_segreti2(word):
    # SCRIVI IL TUO CODICE QUI SOTTO
    return ...

"""
NON MODIFICARE QUESTA SEZIONE
"""
if __name__ == "__main__":
    from colorama import Fore, Style

    test = [
        { "o" : "viva la pizza", "i": "zlzb mb qlaab"},
        { "o" : "hanno ucciso l'uomo ragno", "i": "iboop vddltp m'vpnp sbhop"},
        { "o" : "nel mezzo del cammin di nostra vita",  "i": "ofm nfaap efm dbnnlo el optusb zlub"},
        { "o" : "mi illumino d'immenso", "i": "nl lmmvnlop e'lnnfotp"},
        { "o" : "sempre caro mi fu quest'ermo colle", "i": "tfnqsf dbsp nl gv rvftu'fsnp dpmmf"},
        { "o" : "ei fu siccome immobile", "i": "fl gv tlddpnf lnnpclmf"},
    ]

    for i, t in enumerate(test):
        output = codici_segreti2(t["i"]) 
        expected_output = t["o"]

        if output == expected_output:
            print(f"{Fore.GREEN}TEST {i+1} / {len(test)} : SUPERATO {Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}TEST {i+1} / {len(test)} : FALLITO {Style.RESET_ALL}")
            print(f"INPUT : {t['i']}")
            print(f"OUTPUT ATTESO : {expected_output}")
            print(f"OUTPUT PRODOTTO : {output}")