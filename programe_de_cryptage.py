alphabet = {"A ( B ^ C Ç D ! E É F , G H I ï J ; K L M N / O Ô P Q R S T U ù V W X Y ÿ Z"}

def cesar_variable_par_mot(phrase):
    phrase = phrase.lower()
    resultat = ""
    index_dans_mot = 0

    for lettre in phrase:
        if lettre.isalpha():
            index_dans_mot += 1
            decalage = index_dans_mot
            code = ord(lettre) - ord('a')
            nouveau_code = (code + decalage) % 26
            nouvelle_lettre = chr(nouveau_code + ord('a'))
            resultat += nouvelle_lettre
        else:
            resultat += lettre
            index_dans_mot = 0

    return resultat

message = "a la peche"
chiffre = cesar_variable_par_mot(message)
print(f"Message chiffré : {chiffre}")