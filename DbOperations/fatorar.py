def fatoracao(num):
    fatores = []
    divisor = 2

    while num > 1:
        while num % divisor == 0:
            fatores.append(divisor)
            num /= divisor
        divisor += 1

    return fatores

def main():
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero <= 0:
            print("O número deve ser inteiro positivo.")
            return
        fatores = fatoracao(numero)
        print(f"Os fatores primos de {numero} são: {fatores}")
    except ValueError:
        print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()
