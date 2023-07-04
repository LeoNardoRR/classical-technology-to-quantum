namespace ShorAlgorithm 
{
    open Microsoft.Quantum.Diagnostics;
    open Microsoft.Quantum.Math;
    open Microsoft.Quantum.Canon;

    // Função modular a^x mod N
    function ModularExp(a : Int, x : Int, N : Int) : Int {
        mutable result = 1;
        for (i in 1..x) {
            set result = (result * a) % N;
        }
        return result;
    }

    // Algoritmo clássico de Euclides para encontrar o MDC
    function EuclideanAlgorithm(a : Int, b : Int) : Int {
        if (b == 0) {
            return a;
        }
        return EuclideanAlgorithm(b, a % b);
    }

    // Algoritmo de Shor
    operation ShorAlgorithm(N : Int) : Int {
        // Passo 1: Verificar se N é par ou igual a 1.
        if (N % 2 == 0 || N == 1) {
            return N;
        }

        mutable a = 2;
        repeat {
            // Passo 2: Escolher um 'a' aleatório menor que N.
            a += 1;

            // Passo 3: Calcular o MDC entre 'a' e N.
            let gcd = EuclideanAlgorithm(a, N);
            if (gcd != 1) {
                return gcd; // Fator encontrado!
            }

            // Resto do código do algoritmo aqui...

        } until (false);
        return N; // Fator não encontrado após várias iterações.
    }
}
