import matplotlib.pyplot as plt
import numpy as np
import os

cwd = os.getcwd()

x = np.linspace(0, 100, 1001)
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
fig.savefig(os.path.join(cwd, "test_plot.png"))
fig.savefig(os.path.join(cwd, "test_plot.jpg"))
fig.savefig(os.path.join(cwd, "test_plot.pdf"))
plt.show()