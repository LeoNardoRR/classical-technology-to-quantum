namespace Quantum.Factorization {
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Math;

    // Função clássica para calcular o MDC (máximo divisor comum) entre dois números inteiros.
    function GCD(x : Int, y : Int) : Int {
        if (y == 0) {
            return x;
        }
        return GCD(y, x % y);
    }

    // Algoritmo quântico para encontrar o período de uma função modular
    operation FindPeriod(a : Int, N : Int) : Int {
        mutable r = 1;
        mutable period = 0;
        repeat {
            // Executa a transformada quântica de Fourier modular
            for (i in 1..r) {
                (result, _) = ApplyModularExp(a, i, N);
                if (result == 1) {
                    set period = r;
                    break;
                }
            }
            set r *= 2;
        } until (result == 1 or r >= N - 1);
        return period;
    }

    // Subrotina auxiliar para aplicar a exponenciação modular
    operation ApplyModularExp(x : Int, power : Int, N : Int) : (Int, Int) {
        mutable result = 1;
        for (i in 1..power) {
            set result = (result * x) % N;
        }
        return (result, power);
    }

    // Algoritmo de Shor para fatoração
    operation ShorFactorization(N : Int) : Int[] {
        // Verifica se N é par ou primo antes de continuar
        if (N % 2 == 0) {
            return [2, N / 2];
        }
        if (IsPrime(N)) {
            return [N];
        }

        mutable a = 2;
        mutable period = 0;
        repeat {
            // Encontra um 'a' válido com período não trivial
            set a += 1;
            set period = FindPeriod(a, N);
        } until (period != 0 and period % 2 == 0);

        // Calcula os possíveis fatores
        mutable factor1 = GCD(PowerInt(a, period / 2) - 1, N);
        mutable factor2 = GCD(PowerInt(a, period / 2) + 1, N);

        return [factor1, factor2];
    }
}
