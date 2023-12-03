import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

bound = 1

N = 100
h = 2*bound/(N-1)

def get_y(i: int, N_points: int) -> int:
    return i

def equations(p, z_range):
    eqs_to_add = []

    # Add equation from a
    for i in range(1, N - 1):
        eqs_to_add.append(
            p[get_y(i+1, N)] - 2*p[get_y(i, N)] + p[get_y(i-1, N)] - \
            h**2*z_range[i]
        )
    
    # Boundary Conditions
    eqs_to_add.append(p[get_y(0, N)])
    eqs_to_add.append(p[get_y(N - 1, N)])

    return eqs_to_add

def real_sol(z_range) -> list[float]:
    return [
        z**3/6-z/6 for z in z_range
    ]

def main():
    z_range = np.linspace(-bound, bound, N)
    guess = 0
    init_guess = [guess]*N
    res = fsolve(equations, init_guess, args=z_range)
    plt.plot(z_range, res[:N], label='y(x)')
    plt.plot(z_range, real_sol(z_range), label='real y(x)')
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()