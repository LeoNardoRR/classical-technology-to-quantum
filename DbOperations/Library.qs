namespace DbOperations {
    
    open Microsoft.Quantum.Intrinsic;

    operation SayHello(name : String) : Unit {
        Message($"Hello, {name}!");
    }
}
