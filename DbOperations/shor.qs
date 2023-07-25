namespace shor {

    // Operação auxiliar para tentar fatorar um número em seus fatores primos.
    operation FactorizeNumberHelper(N : Int, candidate : Int, factors : Int[]) : Int[] {
        if (N <= 1) {
            return factors;
        }

        if (N % candidate == 0) {
            // Encontrou um fator.
            set N = N / candidate;
            return FactorizeNumberHelper(N, candidate, factors + [candidate]);
        } else {
            // Tentativa com o próximo candidato.
            return FactorizeNumberHelper(N, candidate + 1, factors);
        }
    }

    // Operação para fatorar um número em seus fatores primos.
    operation FactorizeNumber(N : Int) : Int[] {
        return FactorizeNumberHelper(N, 2, new Int[]);
    }
}
