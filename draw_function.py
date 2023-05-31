import numpy as np
import warnings
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from calculate_functions import func, prepare

warnings.filterwarnings("ignore")


def draw(r: str, h: str):
    r = float(prepare(r))
    h = float(prepare(h))
    x = np.linspace(0 - 8, int(np.ceil(r) + 8), 20000)
    y = [func(val, r, h) for val in x]
    fig, ax = plt.subplots()
    plt.xlabel(f'$z$')

    plt.ylabel(r'$\frac{\sqrt{z(2R-z)}dz}{\sqrt{z+h}}$')
    plt.grid()
    plt.plot(x, y, color='orange')

    ix = np.linspace(0, r)
    iy = [func(val, r, h) for val in ix]

    lines = [(.0, .0)] + list(zip(ix, iy)) + [(r, .0)]
    poly = Polygon(lines, facecolor='cyan')
    ax.add_patch(poly)

    plt.title('График исследуемой функции')
    plt.show()
