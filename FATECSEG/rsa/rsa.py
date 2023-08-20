from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import getpass
import time

# Registrar o tempo de início
inicio = time.time()

# Carregar chave pública do destinatário a partir de um arquivo PEM
with open('public_key.pem', 'rb') as f:
    public_key = serialization.load_pem_public_key(f.read())

# Carregar chave privada do remetente a partir de um arquivo PEM
with open('private_key.pem', 'rb') as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

# Solicitar que o usuário digite o texto a ser criptografado
mensagem = getpass.getpass("Digite a senha/texto a ser criptografado: ")

# Converter a mensagem em bytes usando a codificação UTF-8
mensagem_bytes = mensagem.encode("utf-8")

# Criptografar a mensagem com a chave pública
ciphertext = public_key.encrypt(
    mensagem_bytes,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Descriptografar o texto cifrado com a chave privada
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

# Registrar o tempo de término
fim = time.time()

# Calcular o tempo de execução
tempo_execucao = fim - inicio