def codice_fiscale(cf):
    # SCRIVI IL TUO CODICE QUI SOTTO
    return cf.upper()

"""
NON MODIFICARE QUESTA SEZIONE
"""
if __name__ == "__main__":
    from colorama import Fore, Style

    test = [
        { "i" : "vpcasd87d09g781k", "o": "VPCASD87D09G781K"},
        { "i" : "vpcSsd87d09g781K", "o": "VPCSSD87D09G781K"},
        { "i" : "VpcasD87D09G781K", "o": "VPCASD87D09G781K"},
        { "i" : "VPCASD87D09G781K", "o": "VPCASD87D09G781K"}
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