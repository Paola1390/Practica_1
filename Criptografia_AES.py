from Crypto.Cipher import AES 
from Crypto.Random import get_random_bytes

#generar la clave y vector inicializion
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)

#Cifrar 
mensaje = b"Seguridad Informatica"
ciphertext, tag = cipher.encrypt_and_digest(mensaje)
print("Cifrado:", ciphertext)

#Descifrar
decipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
plaintext = decipher.decrypt(ciphertext)
print("Descifrado:", plaintext.decode())
