open Microsoft.Quantum.Measurement;

namespace shor {

// Encontra o MDC (máximo divisor comum) de dois números
function GCD(a : Int, b : Int) : Int {
    if (b == 0) {
        return a;
    } else {
        return GCD(b, a % b);
    }
}

    operation OrderFinding(N : Int) : Int {
        mutable i = 1;
        mutable order = 2;
        repeat {
            if (GCD(order, N) > 1) {
                return order;
            }
            set order = order * 2;
            set i += 1;
        }
    }

    operation ShorAlgorithm() : Unit {
        // O número que queremos fatorar
        let N = 21;
        let message = "";

        // Encontra a ordem modular
        let r = OrderFinding(N);
        message($"Encontrada ordem r = {r}");
    }
}
