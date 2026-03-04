import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# --- CONFIGURATION ---
# Define the target state as a bitstring (e.g., '10101')
# You can change this string to ANY length to change N
target_state = '10101' 
n = len(target_state) # Number of qubits derived from target length
nb_iterations = 2 # 0 for auto compute

print(f"Running Grover's Search for target state '{target_state}' on {n} qubits.")

if nb_iterations is None:
    # Calculate optimal number of iterations
    # R ≈ (pi/4) * sqrt(2^N)
    nb_iterations = int(np.floor((np.pi / 4) * np.sqrt(2**n)))
    print(f"Optimal number of iterations for N={n}: {nb_iterations}")

# Setup the circuit with n qubits and n classical bits
qc = QuantumCircuit(n, n)

# 1. Superposition: Place all qubits in an equal superposition
qc.h(range(n))

# Helper: Generalized Oracle
def apply_oracle(qc, target):
    """
    Marks the target state by flipping its phase.
    """
    n_qubits = qc.num_qubits
    
    # Flip '0' bits in target to '1' so that the target state becomes |11...1>
    # Note: Qiskit uses little-endian ordering (q0 is rightmost bit)
    # enumerate(target) goes left-to-right (MSB to LSB in string repr)
    # so index i corresponds to qubit n - 1 - i
    for i, bit in enumerate(target):
        if bit == '0':
            qc.x(n_qubits - 1 - i)
            
    # Apply multi-controlled Z (MCZ)
    # Constructed from H gates on target + MCX (Multi-controlled NOT)
    # We use qubit n-1 as the target for the MCX, and 0 to n-2 as controls
    qc.h(n_qubits-1)
    qc.mcx(list(range(n_qubits-1)), n_qubits-1) 
    qc.h(n_qubits-1)
    
    # Uncompute X gates (restore '0's to original state)
    for i, bit in enumerate(target):
        if bit == '0':
            qc.x(n_qubits - 1 - i)

# Helper: Generalized Diffuser (Reflection about Mean)
def apply_diffuser(qc, n_qubits):
    """
    Amplifies the amplitude of the marked state.
        Performs reflection about the state |s> = |++++>.
    """
    # Apply H to all
    qc.h(range(n_qubits))
    # Apply X to all
    qc.x(range(n_qubits))

    qc.barrier()
    # Multi-controlled Z (same mechanism as Oracle, targeting |11...1>)
    qc.h(n_qubits-1)
    qc.mcx(list(range(n_qubits-1)), n_qubits-1)
    qc.h(n_qubits-1)
    
    qc.barrier()
    # Uncompute X 
    qc.x(range(n_qubits))
    # Uncompute H
    qc.h(range(n_qubits))

# Apply Grover Iterations
for step in range(nb_iterations):
    qc.barrier() # Visual marker for circuit diagram
    apply_oracle(qc, target_state)
    qc.barrier()
    apply_diffuser(qc, n)

# 4. Measure
qc.measure(range(n), range(n))

# Simulation
sim = AerSimulator()
result = sim.run(qc, shots=1024).result().get_counts()

print("Result counts:", result)

# Visualization
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

# Visualize the Circuit
# fold=-1 keeps the circuit on one line (scroll horizontally in some viewers)
qc.draw("mpl", ax=ax1, fold=-1) 
ax1.set_title(f"Quantum Circuit (N={n}, Iterations={nb_iterations})")

# Visualize the Measurement Statistics
plot_histogram(result, ax=ax2)
ax2.set_title(f"Measurement Histogram (Target: {target_state})")

plt.tight_layout()
plt.show()
