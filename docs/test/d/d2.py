def tagliamo_a_corto(stringa):
    # SCRIVI IL TUO CODICE QUI SOTTO
    
    return ...


"""
NON MODIFICARE QUESTA SEZIONE
"""
if __name__ == "__main__":
    from colorama import Fore, Style

    test = [
        { "i" : ["L'Inghilterra vince i mondiali"], "o": "L'Inghilterra vince i m..."},
        { "i" : ["L'Italia vince i mondiali"], "o": "L'Italia vince i mondiali"},
        { "i" : ["Supercalifragilistichespiralidoso"], "o": "Supercalifragilistiches..."},
    ]

    for i, t in enumerate(test):
        output = tagliamo_a_corto(*t["i"]) 
        expected_output = t["o"]

        if output == expected_output:
            print(f"{Fore.GREEN}TEST {i+1} / {len(test)} : SUPERATO {Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}TEST {i+1} / {len(test)} : FALLITO {Style.RESET_ALL}")
            print(f"INPUT : {t['i']}")
            print(f"OUTPUT ATTESO : {expected_output}")
            print(f"OUTPUT PRODOTTO : {output}")