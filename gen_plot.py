import matplotlib.pyplot as plt
import numpy as np
import os

cwd = os.getcwd()

x = np.linspace(0, 100, 100001)
y = np.random.random(size=x.shape[0])

fig,ax = plt.subplots(
    nrows=1,
    ncols=1,
    figsize=(10,5)
)

ax.plot(
    x,
    y,
    "--k"
)

plt.tight_layout()
fig.savefig(os.path.join(cwd, "test_plot.png"), dpi=200)
fig.savefig(os.path.join(cwd, "test_plot.jpg"), dpi=200)
fig.savefig(os.path.join(cwd, "test_plot.pdf"), dpi=200)
plt.show()