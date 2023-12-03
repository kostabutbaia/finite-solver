import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

bound = 10

N = 100
h = 2*bound/(N-1)

OMEGA = 0.8

def get_a(i: int, N_points: int) -> int:
    return i

def get_psi(i: int, N_points: int) -> int:
    return N_points + i

def equations(p):
    eqs_to_add = []

    # Add equation from a
    for i in range(1, N - 1):
        eqs_to_add.append(
            (p[get_a(i+1, N)] - 2*p[get_a(i, N)] + p[get_a(i-1, N)])/h**2 + \
            (OMEGA**2*p[get_a(i, N)]+p[get_a(i, N)]*(p[get_a(i, N)]**2-(1+p[get_psi(i, N)])**2))
        )

    # Add equation from psi
    for i in range(1, N - 1):
        eqs_to_add.append(
            (p[get_psi(i+1, N)] - 2*p[get_psi(i, N)] + p[get_psi(i-1, N)])/h**2 + \
            (1 + (1+p[get_psi(i, N)])*(p[get_a(i, N)]**2-(1+p[get_psi(i, N)])**2))
        )
    
    # Boundary Conditions
    eqs_to_add.append(p[get_a(0, N)])
    eqs_to_add.append(p[get_a(N - 1, N)])

    eqs_to_add.append(p[get_psi(0, N)])
    eqs_to_add.append(p[get_psi(N - 1, N)])

    return eqs_to_add

def main():
    z_range = np.linspace(-bound, bound, N)
    init_guess = [14]*(2*N)
    res = fsolve(equations, init_guess)
    plt.plot(z_range, res[:N], label='a')
    plt.plot(z_range, res[N:2*N], label='psi')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()