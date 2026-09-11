from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)
nonce = os.urandom(12)
plaintext = b"Isha-`RabTech Academy - Secret Data"

ciphertext = aesgcm.encrypt(nonce, plaintext, None)
decrypted = aesgcm.decrypt(nonce, ciphertext, None)

print(f"Key: {key.hex()}")
print(f"Encrypted: {ciphertext.hex()}")
print(f"Decrypted: {decrypted.decode()}")
