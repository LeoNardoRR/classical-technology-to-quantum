from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# Generate an RSA private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Extract the public key from the private key
public_key = private_key.public_key()

# Retrieve the value of the modulus (n) from the public key
n = public_key.public_numbers().n
print("Valor de N:", n)
