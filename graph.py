import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

OMEGA = 0.8

def U_func(a, psi):
    return 1/4*(a**4 - psi**2*(6 + 4*psi + psi**2) + 2*a**2*(-1 + 2*psi + psi**2 + OMEGA**2))

def main():
    a_s = np.sqrt(1-OMEGA**6)/OMEGA**2
    psi_s = (1-OMEGA**2)/OMEGA**2

    a = np.arange(-a_s, a_s, 0.01)
    psi = np.arange(-psi_s, psi_s, 0.01)

    a, psi = np.meshgrid(a, psi, sparse=True)
    U = 2*psi - OMEGA**2 * a**2 - 1/2*(a**2-(1+psi)**2)**2+1/2
    ax = plt.axes(projection ='3d')
    ax.set_xlabel('a')
    ax.set_ylabel('psi')
    ax.plot_surface(a, psi, U, cmap=cm.coolwarm, zorder=1)
    print(a_s, psi_s)
    # ax.plot([a_s]*10, [psi_s]*10, np.linspace(U_func(a_s, psi_s)-5, U_func(a_s, psi_s)+5, 10), zorder=8)
    # ax.set_zlim([-8, 0.4])

    plt.show()


if __name__ == '__main__':
    main()