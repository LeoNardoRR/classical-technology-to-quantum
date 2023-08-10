from math import gcd
from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.circuit.library.standard_gates import SwapGate

def q_a_mod_n(a, r, s):
    U = QuantumCircuit(s)
    for i in range(r):
        if s == 2:
            U.append(SwapGate(), [0, 1])
        elif s == 3:
            U.append(SwapGate(), [0, 1])
            U.append(SwapGate(), [1, 2])
        elif s == 4:
            U.append(SwapGate(), [0, 1])
            U.append(SwapGate(), [1, 2])
            U.append(SwapGate(), [2, 3])
        elif s == 5:
            U.append(SwapGate(), [0, 1])
            U.append(SwapGate(), [1, 2])
            U.append(SwapGate(), [2, 3])
            U.append(SwapGate(), [3, 4])
    U = U.to_gate()
    U.name = f"{a}^{r} mod n"
    c_U = U.control()
    return c_U

def q_circuito_shor(r, s, a):
    print("Criando o circuito de Shor...")
    cq_shor = QuantumCircuit(r + s, r)
    
    for i in range(r):
        cq_shor.h(i)
    
    cq_shor.x(s - 1 + r)
    
    for j in range(r):
        cq_shor.append(q_a_mod_n(a, 2 ** j, s), [j] + [k + r for k in range(s)])
    
    # dfe_dagger(r) is missing from the provided code
    
    print("Circuito de Shor criado!")
    return cq_shor

def ordem_multiplicativa_n(periodo):
    ord_mult_n = periodo // 2
    return ord_mult_n

def fator_n(ord_mult_n, a, n):
    fator = gcd((a ** ord_mult_n) - 1, n)
    return fator


#------------------------------------------------------


# Coloque os valores apropriados para r, s e a
r = 4
s = 10
a = 6

circuito_shor = q_circuito_shor(r, s, a)
print("Circuito de Shor:", circuito_shor)
