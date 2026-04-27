import os
import sys
from cryptography.fernet import Fernet

def load_key():
    key = os.environ.get("FERNET_KEY")
    
    if not key:
        new_key = Fernet.generate_key()
        print("⚠️  Aucune clé trouvée (FERNET_KEY). Voici une clé générée :")
        print(new_key.decode())
        print("\n➡️  Copie de la clé dans l'environnement :")
        print("export FERNET_KEY='" + new_key.decode() + "'")
        return new_key
        
    try:
        return key.encode()
    except Exception as e:
        print(f"❌ Erreur lors de l'encodage de la clé : {e}")
        sys.exit(1)

def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_message(token, key):
    f = Fernet(key)
    return f.decrypt(token).decode()

if __name__ == "__main__":
    print("--- Atelier 1 : Chiffrement via Secrets ---")
    

    secret_key = load_key()
    print("✅ Clé récupérée avec succès.")

    text_to_hide = "Message top secret de l'Atelier 1"
    
    try:
        encrypted = encrypt_message(text_to_hide, secret_key)
        print(f"\n[+] Original : {text_to_hide}")
        print(f"[+] Chiffré  : {encrypted.decode()}")
        
        decrypted = decrypt_message(encrypted, secret_key)
        print(f"[+] Déchiffré : {decrypted}")
        
    except Exception as e:
        print(f"❌ Erreur lors du traitement : {e}")