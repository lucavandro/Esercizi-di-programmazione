def palindromo(parola):
    # SCRIVI IL TUO CODICE QUI SOTTO
    return parola == parola[::-1]

"""
NON MODIFICARE QUESTA SEZIONE
"""
if __name__ == "__main__":
    from colorama import Fore, Style

    test = [
        { "i" : ["pallone"], "o": False},
        { "i" : ["bella ciao"], "o": False},
        { "i" : ["banana33"], "o": False},
        { "i" : ["pizza"], "o": False},
        { "i" : ["nutella"], "o": False},
        { "i" : ["cocacola"], "o": False},
        { "i" : ["radar"], "o": True},
        { "i" : ["anna"], "o": True},
        { "i" : ["oro"], "o": True},
        { "i" : ["ossesso"], "o": True},
    ]

    for i, t in enumerate(test):
        output = palindromo(*t["i"]) 
        expected_output = t["o"]

        if output == expected_output:
            print(f"{Fore.GREEN}TEST {i+1} / {len(test)} : SUPERATO {Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}TEST {i+1} / {len(test)} : FALLITO {Style.RESET_ALL}")
            print(f"INPUT : {t['i']}")
            print(f"OUTPUT ATTESO : {expected_output}")
            print(f"OUTPUT PRODOTTO : {output}")