import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 42., 101)
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
fig.savefig("test_plot.png", dpi=200)
fig.savefig("test_plot.jpg", dpi=200)
fig.savefig("test_plot.pdf")
plt.show()


import matplotlib
gui_env = [i for i in matplotlib.rcsetup.interactive_bk]
non_gui_backends = matplotlib.rcsetup.non_interactive_bk
print ("Gui backends I will test for", gui_env)
for gui in gui_env:
    print ("testing", gui)
    try:
        matplotlib.use(gui, force=True)
        from matplotlib import pyplot as plt
        print ("    ",gui, "Is Available")
        plt.plot([1.5,2.0,2.5])
        fig = plt.gcf()
        fig.suptitle(gui)
        fig.savefig(f"test_plot_{gui=}.png", dpi=200)
        fig.savefig(f"test_plot_{gui=}.jpg", dpi=200)
        fig.savefig(f"test_plot_{gui=}.pdf")

        print ("Using ..... ",matplotlib.get_backend())
    except:
        print ("    ",gui, "Not found")

print ("Non Gui backends are:", non_gui_backends)
for non_gui in non_gui_backends:
    print ("testing", non_gui)
    try:
        matplotlib.use(non_gui, force=True)
        from matplotlib import pyplot as plt
        print ("    ",non_gui, "Is Available")
        plt.plot([1.5,2.0,2.5])
        fig = plt.gcf()
        fig.suptitle(gui)
        fig.savefig(f"test_plot_{non_gui=}.png", dpi=200)
        fig.savefig(f"test_plot_{non_gui=}.jpg", dpi=200)
        fig.savefig(f"test_plot_{non_gui=}.pdf")

        print ("Using ..... ",matplotlib.get_backend())
    except:
        print ("    ", non_gui, "Not found")