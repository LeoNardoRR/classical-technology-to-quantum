using System;
using Microsoft.Quantum.Simulation.Core;
using Microsoft.Quantum.Simulation.Simulators;

namespace ClassicalToQuantum
{
    class Program
    {
        static void Main(string[] args)
        {
            // Número a ser fatorado
            int numberToFactorize = 21;

            // Cria o simulador Q# para chamar a operação FactorizeNumber
            using var sim = new QuantumSimulator();

            // Chama a operação Q# para fatorar o número
            var factors = FactorizeNumber.Run(sim, numberToFactorize).Result;

            Console.WriteLine($"Os fatores primos de {numberToFactorize} são: {string.Join(", ", factors)}");
        }
    }

    // Defina a operação Q# como uma classe estática chamada FactorizeNumber
    public static class FactorizeNumber
    {
        public static async System.Threading.Tasks.Task<Int64[]> Run(QuantumSimulator sim, int N)
        {
            return await ClassicalToQuantum.FactorizeNumber.Run(sim, N);
        }
    }
}
