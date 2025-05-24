import random
import unicodedata
import tkinter as tk
from tkinter import messagebox

def cles():
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,/:;<=>?[\]^_{|}~"
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789@."
    random_symbols = random.sample(symbols, random.randint(8, 16))
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

root = tk.Tk()
root.title("Cryptage César Variable")
root.geometry("700x650")
root.config(bg="#C0DFEF")
root.resizable(False, False)

label_title = tk.Label(root, text="Cryptage César Variable", font=("Helvetica", 18, "bold"), fg="#4A90E2", bg="#C2DFEF")
label_title.pack(pady=15)

label_message = tk.Label(root, text="Message à crypter :", font=("Helvetica", 12), fg="#000", bg="#C2DFEF")
label_message.pack(pady=5)
entry_message = tk.Entry(root, font=("Helvetica", 12), width=60, relief="solid", bd=1, fg="#000")
entry_message.pack(pady=10)

label_encrypted = tk.Label(root, text="Message crypté :", font=("Helvetica", 12), fg="#000", bg="#C2DFEF")
label_encrypted.pack(pady=5)
entry_encrypted = tk.Entry(root, font=("Helvetica", 12), width=60, state="readonly", relief="solid", bd=1, fg="#000")
entry_encrypted.pack(pady=10)

label_key = tk.Label(root, text="Clé du cryptage :", font=("Helvetica", 12), fg="#000", bg="#C2DFEF")
label_key.pack(pady=5)
entry_key = tk.Entry(root, font=("Helvetica", 12), width=60, state="readonly", relief="solid", bd=1, fg="#000")
entry_key.pack(pady=10)

label_decrypt_message = tk.Label(root, text="Message à décrypter :", font=("Helvetica", 12), fg="#000", bg="#C2DFEF")
label_decrypt_message.pack(pady=5)
entry_decrypt_message = tk.Entry(root, font=("Helvetica", 12), width=60, relief="solid", bd=1, fg="#000")
entry_decrypt_message.pack(pady=10)

label_decrypt_key = tk.Label(root, text="Clé du cryptage (format : base_index-alphabet) :", font=("Helvetica", 12), fg="#000", bg="#C2DFEF")
label_decrypt_key.pack(pady=5)
entry_decrypt_key = tk.Entry(root, font=("Helvetica", 12), width=60, relief="solid", bd=1, fg="#000")
entry_decrypt_key.pack(pady=10)

label_decrypted = tk.Label(root, text="Message décrypté :", font=("Helvetica", 12), fg="#000", bg="#C2DFEF")
label_decrypted.pack(pady=5)
entry_decrypted = tk.Entry(root, font=("Helvetica", 12), width=60, state="readonly", relief="solid", bd=1, fg="#000")
entry_decrypted.pack(pady=10)

def encrypt_message():
    message = entry_message.get()
    if not message:
        messagebox.showwarning("Avertissement", "Veuillez entrer un message à crypter.")
        return

    message_sans_accents = remove_accents(message.lower())
    new_alphabet = cles()
    encrypted_message, key = cesar_variable(message_sans_accents, new_alphabet)

    entry_encrypted.config(state="normal")
    entry_encrypted.delete(0, tk.END)
    entry_encrypted.insert(0, encrypted_message)
    entry_encrypted.config(state="readonly")

    entry_key.config(state="normal")
    entry_key.delete(0, tk.END)
    entry_key.insert(0, key)
    entry_key.config(state="readonly")

def decrypt_message():
    encrypted_message = entry_decrypt_message.get()
    key = entry_decrypt_key.get()
    
    if not encrypted_message or not key:
        messagebox.showwarning("Avertissement", "Veuillez entrer un message et une clé à décrypter.")
        return

    try:
        decrypted_message = decrypt(encrypted_message, key)
        entry_decrypted.config(state="normal")
        entry_decrypted.delete(0, tk.END)
        entry_decrypted.insert(0, decrypted_message)
        entry_decrypted.config(state="readonly")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors du décryptage : {e}")

btn_encrypt = tk.Button(root, text="Crypter", font=("Helvetica", 12), bg="#4A90E2", fg="white", command=encrypt_message, relief="raised", bd=2)
btn_encrypt.pack(pady=15)

btn_decrypt = tk.Button(root, text="Décrypter", font=("Helvetica", 12), bg="#4A90E2", fg="white", command=decrypt_message, relief="raised", bd=2)
btn_decrypt.pack(pady=10)

root.mainloop()
