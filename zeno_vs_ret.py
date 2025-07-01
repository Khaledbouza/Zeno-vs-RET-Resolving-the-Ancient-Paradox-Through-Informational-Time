import matplotlib.pyplot as plt
import numpy as np

# Setup
n_steps = 50
initial_position = 0.0
ticks = np.arange(0, n_steps + 1)

# Zeno Model: Halving the gap each step
positions_zeno = [1.0 - 0.5**i for i in ticks]

# RET Model: Fixed recursive increment
delta = 1.0 / n_steps
positions_ret = [initial_position]
for _ in range(n_steps):
    positions_ret.append(positions_ret[-1] + delta)

# Plotting
plt.figure(figsize=(8, 4))
plt.plot(ticks, positions_zeno, 'o--', label='Zeno: Classical Halving')
plt.plot(ticks, positions_ret, 'x-', label='RET: Recursive Time')
plt.title("🔍 Zeno vs RET: Reaching the Goal in Finite Time")
plt.xlabel("Tick")
plt.ylabel("Position")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
