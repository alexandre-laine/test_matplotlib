import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np
import os

cwd = os.getcwd()

fig,ax = plt.subplots(
    nrows=1,
    ncols=1,
    figsize=(10,5)
)

for i in tqdm(range(10)):

    x = np.linspace(0, 100, 100001)
    y = np.random.random(size=x.shape[0])



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