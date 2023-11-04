key_size = 16
key = randprime(2**(key_size-1), 2**key_size)
print(f"Chave gerada: {key}")
print("-" * 40)