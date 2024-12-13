import numpy as np
import matplotlib.pyplot as plt

# Konstanty
hbar = 1.0545718e-34  # Planckova konstanta dělená 2π [J·s]
m = 9.10938356e-31    # Hmotnost elektronu [kg]
E = 1.0e-19           # Celková energie částice [J]
U0 = (3/4) * E        # Potenciálová energie [J]

# Vlnová čísla
k1 = np.sqrt(2 * m * E) / hbar              # Pro x <= 0
k2 = np.sqrt(2 * m * (E - U0)) / hbar       # Pro x > 0

# Koeficienty odrazu a přenosu
r = (k1 - k2) / (k1 + k2)
t = (2 * k1) / (k1 + k2)

# Amplitudy
A = 1  # Amplituda přicházející vlny
B = r * A
C = t * A

# Prostorová osa
x1 = np.linspace(-1e-9, 0, 500)  # Oblast I: x ≤ 0
x2 = np.linspace(0, 1e-9, 500)   # Oblast II: x > 0

# Vlnové funkce
psi_I = A * np.exp(1j * k1 * x1) + B * np.exp(-1j * k1 * x1)
psi_II = C * np.exp(1j * k2 * x2)

# Pravděpodobnostní hustota
prob_I = np.abs(psi_I)**2
prob_II = np.abs(psi_II)**2

# Potenciálová funkce
U_x1 = np.full_like(x1, 0)
U_x2 = np.full_like(x2, U0)

# Vykreslení potenciálu
plt.figure(figsize=(10, 6))
plt.plot(x1, U_x1 / E, label='Potenciál U(x)', color='black')
plt.plot(x2, U_x2 / E, color='black')

# Vykreslení reálné části vlnové funkce
plt.plot(x1, np.real(psi_I), label='Reálná část ψ(x) v oblasti I', color='blue')
plt.plot(x2, np.real(psi_II), label='Reálná část ψ(x) v oblasti II', color='red')

plt.title('Vlnová funkce a potenciálový schod')
plt.xlabel('Pozice x [m]')
plt.ylabel('Amplituda / Potenciál [relativní jednotky]')
plt.legend()
plt.grid()
plt.show()

# Vykreslení pravděpodobnostní hustoty
plt.figure(figsize=(10, 6))
plt.plot(x1, prob_I, label='Pravděpodobnostní hustota v oblasti I', color='blue')
plt.plot(x2, prob_II, label='Pravděpodobnostní hustota v oblasti II', color='red')

plt.title('Pravděpodobnostní hustota $|\psi(x)|^2$')
plt.xlabel('Pozice x [m]')
plt.ylabel('Pravděpodobnostní hustota [relativní jednotky]')
plt.legend()
plt.grid()
plt.show()
