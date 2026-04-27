import nacl.secret
import nacl.utils
from nacl.encoding import HexEncoder

def run_atelier2():
    print("--- Atelier 2 : Chiffrement avec PyNaCl (SecretBox) ---")

    key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
    box = nacl.secret.SecretBox(key)
    
    print(f"✅ Clé générée (hex) : {key.hex()}")

    message = b"Ceci est un message chiffre avec XSalsa20-Poly1305"
    print(f"Original : {message.decode()}")

    encrypted = box.encrypt(message)
    
    print(f"🔒 Chiffré (hex) : {encrypted.hex()}")

    decrypted = box.decrypt(encrypted)
    
    print(f"🔓 Déchiffré : {decrypted.decode()}")

if __name__ == "__main__":
    run_atelier2()