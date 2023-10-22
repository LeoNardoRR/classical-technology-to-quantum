open Microsoft.Quantum.Math;
open Microsoft.Quantum.Convert;
open Microsoft.Quantum.Arithmetic;
open Microsoft.Quantum.Canon;
open Microsoft.Quantum.Characterization;

operation ShorAlgorithm(n : Int) : Int {
    mutable foundPeriod = -1;
    
    for a in 2 .. n - 1 {
        let isCoprime = GreatestCommonDivisorI(a, n) == 1;
        
        if isCoprime {
            using (register = Qubit[n]) {
                // Quantum operations to implement Shor's algorithm
                ApplyToEachA(H, register);
                ApplyAexpModN(A(a, n), register);
                let result = QFTLE(Reverse(register));

                // Measure and interpret the result
                let measuredResult = MultiM(result);
                let periodGuess = continuedFraction(measuredResult);

                if periodGuess > 1 {
                    set foundPeriod = periodGuess;
                    break;
                }
            }
        }
    }
    
    return foundPeriod;
}
