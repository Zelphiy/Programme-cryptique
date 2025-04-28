import random
import unicodedata

def cles():
    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,./:;<=>?@[\]^_{|}~"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    random_symbols = random.sample(symbols, random.randint(10, 20))
    new_alphabet = list(alphabet + ''.join(random_symbols))
    random.shuffle(new_alphabet)
    return ''.join(new_alphabet)

def remove_accents(text):
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != "Mn")
    return text

def cesar_variable(phrase, new_alphabet, base_index=0):
    resultat = ""
    index_dans_mot = base_index
    taille = len(new_alphabet)

    for lettre in phrase:
        if lettre in new_alphabet:
            index_dans_mot += 1
            index_lettre = new_alphabet.index(lettre)
            nouvel_index = (index_lettre + index_dans_mot) % taille
            resultat += new_alphabet[nouvel_index]
        else:
            resultat += lettre
            index_dans_mot = base_index

    key = f"{base_index}-{new_alphabet}"
    return resultat, key

def decrypt(message_crypte, key):
    base_index_str, new_alphabet = key.split("-")
    base_index = int(base_index_str)
    
    resultat = ""
    index_dans_mot = base_index
    taille = len(new_alphabet)
    
    for lettre in message_crypte:
        if lettre in new_alphabet:
            index_dans_mot += 1
            index_lettre = new_alphabet.index(lettre)
            nouvel_index = (index_lettre - index_dans_mot) % taille
            resultat += new_alphabet[nouvel_index]
        else:
            resultat += lettre
            index_dans_mot = base_index
            
    return resultat


new_alphabet = cles()

message = "à la pêche"
message_sans_accents = remove_accents(message.lower())

message_crypte, key  = cesar_variable(message_sans_accents, new_alphabet)
print("Clé : ", key)
print("Message crypté : ", message_crypte)

message_decode = decrypt(message_crypte, key)
print("Message décrypté : ", message_decode)