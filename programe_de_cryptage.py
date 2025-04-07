alphabet = "a(b^cÇd!eÉf,ghiïj;klmn/oÔpqrstuùvwxyÿz"

def cesar_variable_custom_alphabet(phrase, alphabet):
    resultat = ""
    index_dans_mot = 0
    taille = len(alphabet)

    for lettre in phrase:
        if lettre in alphabet:
            index_dans_mot += 1
            index_lettre = alphabet.index(lettre)
            nouvel_index = (index_lettre + index_dans_mot) % taille
            resultat += alphabet[nouvel_index]
        else:
            resultat += lettre
            index_dans_mot = 0

    return resultat

message = "à la pêche"
message = message.lower()

chiffre = cesar_variable_custom_alphabet(message, alphabet)
print(f"Message original : {message}")
print(f"Message chiffré  : {chiffre}")
