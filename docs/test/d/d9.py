def al_contrario(parola):
    # SCRIVI IL TUO CODICE QUI SOTTO
    return ...

"""
NON MODIFICARE QUESTA SEZIONE
"""
if __name__ == "__main__":
    from colorama import Fore, Style

    test = [
        { "i" : ["pallone"], "o": "enollap"},
        { "i" : ["bella ciao"], "o": "oaic alleb"},
        { "i" : ["banana33"], "o": "33ananab"},
        { "i" : ["pizza"], "o": "azzip"},
        { "i" : ["nutella"], "o": "alletun"},
        { "i" : ["cocacola"], "o": "alocacoc"},
    ]

    for i, t in enumerate(test):
        output = al_contrario(*t["i"]) 
        expected_output = t["o"]

        if output == expected_output:
            print(f"{Fore.GREEN}TEST {i+1} / {len(test)} : SUPERATO {Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}TEST {i+1} / {len(test)} : FALLITO {Style.RESET_ALL}")
            print(f"INPUT : {t['i']}")
            print(f"OUTPUT ATTESO : {expected_output}")
            print(f"OUTPUT PRODOTTO : {output}")