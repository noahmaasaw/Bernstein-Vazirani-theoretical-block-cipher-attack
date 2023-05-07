"""Bernstein-Vazirani theoretical block cipher attack"""
#WORK IN PROGRESS

import string
import random
import hashlib
import time
import binascii
import qiskit
from qiskit import IBMQ
IBMQ.save_account('2330fa80e6cdc16978c9d943bb82b00665b18d690f370cdc8874f617a1650490dba8b1aa035e152e40a7240c7f626592c9871f4f92d65945b63eb60e85f4a99d')
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
provider = IBMQ.load_account()

test_password = "guessguess"
hexkey = hashlib.sha256(test_password.encode()).hexdigest()
print("Hash: %s" % hexkey)
ini_string = hexkey
j = int(ini_string, 16)  
bStr = '' 
while j > 0:
    bStr = str(j % 2) + bStr
    j = j >> 1    
    res = bStr
print("BINARY HASH SOLUTION:", str(''.join(res)))
print("LENGTH:",len(str(''.join(res))))
n = int(hexkey, 16)         
print('Value in hexadecimal:', hexkey)
print('Value in decimal:', n,"\n")
key = str(res)

def bv(i):
        secretnumber = key
        circuit = QuantumCircuit(len(secretnumber) + 1, len(secretnumber))
        circuit.h(range(len(secretnumber)))
        circuit.x(len(secretnumber))
        circuit.h(len(secretnumber))
        circuit.barrier()

        for ii, yesno in enumerate(reversed(secretnumber)):
            if yesno == '1':
                circuit.cx(ii, len(secretnumber))

        circuit.barrier()
        circuit.h(range(len(secretnumber)))
        circuit.barrier()
        circuit.measure(range(len(secretnumber)), range(len(secretnumber)))
        circuit.draw(output='mpl')
        circuit.barrier()
        
        simulator = Aer.get_backend('qasm_simulator')
        result = execute(circuit, backend=simulator, shots=100).result()
        counts = result.get_counts()
        countskey = list(counts.keys())[0]
        countedkeys = countskey
        return countedkeys
    
print("BINARY HASH SOLUTION:",res,"\n")
bv_return = bv(res)
print("^^^ The Bernstein-Vazirani algorithm mirrors each binary with a qubit. ^^^ \n")
print("BERNSTEIN-VAZIRANI QUANTUM ORACLE SOLUTION:", bv_return, "\n")
print("^^^ If there were theoretically the same number of qubits as the",
      "length of the Binary Hash then the Bernstein Vazirani algorithm ",
      "would serve as a method to be able to attack a block cipher. Since the",
      "Quantum State of the entangled n-qubit Bernstein Vazirani circuit",
      "assumes all 2^n states simultaneously, then that means that there exists a specific ideal, or subset",
      "within the quantum backend that produces the secret key. ^^^"
      
