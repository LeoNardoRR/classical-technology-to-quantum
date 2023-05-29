namespace DbOperations {
    
    open Microsoft.Quantum.Intrinsic;

    operation SayHello(name : String) : Unit {
        Message($"Hello, {name}!");
    }
}

//namespace DbOperation {

    // Operação quântica para descriptografia
//    operation QuantumDecrypt(secretKey : Int) : Int {
        // Cria um qubit para armazenar o segredo criptografado
  //      using (register = Qubit()) {
            // Aplica uma porta X condicional ao qubit se a chave secreta for 1
    //        if (secretKey == 1) {
      //          X(register);
        //    }
            // Mede o qubit e retorna o resultado
  //          return M(register);
      //  }
   // }
//}
