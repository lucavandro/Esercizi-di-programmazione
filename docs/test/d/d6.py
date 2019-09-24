def codice_fiscale(cf):
    # SCRIVI IL TUO CODICE QUI SOTTO
    return ...

"""
NON MODIFICARE QUESTA SEZIONE
"""
if __name__ == "__main__":
    from colorama import Fore, Style

    test = [
        { "i" : "VPCASD87D09G781K", "o": True},
        { "i" : "vpcSsd87d09g781K", "o": True},
        { "i" : "vpcSsd87d09g781",  "o": False},
        { "i" : "vpcSsd87d09g7819", "o": False},
        { "i" : "v1cSsd87d09g781K", "o": False},
        { "i" : "vpcSsd8ad09g781K", "o": False},
    ]

    for i, t in enumerate(test):
        output = codice_fiscale(t["i"]) 
        expected_output = t["o"]

        if output == expected_output:
            print(f"{Fore.GREEN}TEST {i+1} / {len(test)} : SUPERATO {Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}TEST {i+1} / {len(test)} : FALLITO {Style.RESET_ALL}")
            print(f"INPUT : {t['i']}")
            print(f"OUTPUT ATTESO : {expected_output}")
            print(f"OUTPUT PRODOTTO : {output}")