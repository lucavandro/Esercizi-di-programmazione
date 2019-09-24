def password_sicura(password):
    # SCRIVI IL TUO CODICE QUI SOTTO
    return ...


"""
NON MODIFICARE QUESTA SEZIONE
"""
if __name__ == "__main__":
    from colorama import Fore, Style

    test = [
        { "i" : ["12345678"], "o": False},
        { "i" : ["pippo14"], "o": False},
        { "i" : ["Hackme!2"], "o": True},
        { "i" : ["cappero5678#"], "o": False},
        { "i" : ["Pippo!"], "o": False},
        { "i" : ["Villaggio2019@"], "o": True},
    ]

    for i, t in enumerate(test):
        output = password_sicura(*t["i"]) 
        expected_output = t["o"]

        if output == expected_output:
            print(f"{Fore.GREEN}TEST {i+1} / {len(test)} : SUPERATO {Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}TEST {i+1} / {len(test)} : FALLITO {Style.RESET_ALL}")
            print(f"INPUT : {t['i']}")
            print(f"OUTPUT ATTESO : {expected_output}")
            print(f"OUTPUT PRODOTTO : {output}")