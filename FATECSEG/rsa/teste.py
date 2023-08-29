from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Gerando um par de chaves RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# Mensagem a ser criptografada
mensagem_original = ("Esta é uma mensagem secreta.")

# Criptografando a mensagem usando a chave pública
mensagem_criptografada = public_key.encrypt(
    mensagem_original,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Mensagem original:", mensagem_original)
print("Mensagem criptografada:", mensagem_criptografada)

# Descriptografando a mensagem usando a chave privada
mensagem_descriptografada = private_key.decrypt(
    mensagem_criptografada,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Mensagem descriptografada:", mensagem_descriptografada.decode('utf-8'))
