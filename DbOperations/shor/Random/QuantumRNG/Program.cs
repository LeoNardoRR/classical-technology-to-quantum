using System;
using Microsoft.Quantum.Simulation.Core;
using Microsoft.Quantum.Simulation.Simulators;

namespace YourNamespace
{
    class Program
    {
        static void Main(string[] args)
        {
            using var sim = new QuantumSimulator();

            // Chama a operação Q# SampleRandomNumber
            var randomNumber = QuantumRNG.SampleRandomNumber.Run(sim).Result;

            Console.WriteLine($"Número aleatório gerado: {randomNumber}");
        }
    }
}

