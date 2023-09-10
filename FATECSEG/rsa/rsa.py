from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import getpass
import time

inicio = time.time()

with open('public_key.pem', 'rb') as f:
    public_key = serialization.load_pem_public_key(f.read())

with open('private_key.pem', 'rb') as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

mensagem = getpass.getpass("Digite a senha/texto a ser criptografado: ")

mensagem_bytes = mensagem.encode("utf-8")

ciphertext = public_key.encrypt(
    mensagem_bytes,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

plaintext_bytes = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

plaintext = plaintext_bytes.decode("utf-8")

print("Texto cifrado:", ciphertext)
print("Texto decifrado:", plaintext)

fim = time.time()

tempo_execucao = fim - inicio