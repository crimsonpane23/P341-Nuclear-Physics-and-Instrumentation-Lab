import numpy as np
import matplotlib.pyplot as plt

x = np.array([-30, -25, -20, -15, -10, -5, 5, 10, 15, 20, 25, 30], dtype=float)
y = np.array([
    0.49323004661359743, 0.8948660433649347, 2.796892185003242,
    11.659911513483951, 24.377635769515706, 19.191191585096416,
    17.989175162517256, 20.504359710715153, 6.765025369050662,
    1.7675327100769624, 0.5523208813647074, 0.33615041393410783
], dtype=float)

plt.plot(x[:6], y[:6], label="Negative Angle data", color='red')
plt.plot(x[6:], y[6:], label="Negative Angle data", color='red')
plt.xlabel("Scattering angle θ (degrees)")
plt.ylabel("N(θ) (space-corrected)")
plt.title("Rutherford Scattering: N(θ) vs θ")
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.show()
