def password_sicura2(password):
    # SCRIVI IL TUO CODICE QUI SOTTO
    return ...

"""
NON MODIFICARE QUESTA SEZIONE
"""
if __name__ == "__main__":
    from colorama import Fore, Style

    test = [
        { "i" : ["pallone"], "o": "p@110n3#"},
        { "i" : ["bella ciao"], "o": "b311@_ci@0"},
        { "i" : ["banana33"], "o": "b@n@n@33"},
        { "i" : ["pizza"], "o": "pizz@###"},
        { "i" : ["nutella"], "o": "nut311@#"},
        { "i" : ["cocacola"], "o": "c0c@c01@"},
    ]

    for i, t in enumerate(test):
        output = password_sicura2(*t["i"]) 
        expected_output = t["o"]

        if output == expected_output:
            print(f"{Fore.GREEN}TEST {i+1} / {len(test)} : SUPERATO {Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}TEST {i+1} / {len(test)} : FALLITO {Style.RESET_ALL}")
            print(f"INPUT : {t['i']}")
            print(f"OUTPUT ATTESO : {expected_output}")
            print(f"OUTPUT PRODOTTO : {output}")