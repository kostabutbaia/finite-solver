import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

bound = 1

N = 400
h = 2*bound/(N-1)

def get_y(i: int, N_points: int) -> int:
    return i

def get_x(i: int, N_points: int) -> int:
    return N_points + i

def equations(p):
    eqs_to_add = []

    # Add equation from y
    for i in range(1, N - 1):
        eqs_to_add.append(
            p[get_y(i+1, N)] - 2*p[get_y(i, N)] + p[get_y(i-1, N)] + \
            h**2*p[get_x(i, N)]
        )

    # Add equation from x
    for i in range(1, N - 1):
        eqs_to_add.append(
            p[get_x(i+1, N)] - 2*p[get_x(i, N)] + p[get_x(i-1, N)] + \
            h**2*p[get_y(i, N)]
        )
    
    # Boundary Conditions
    eqs_to_add.append(p[get_x(0, N)])
    eqs_to_add.append(p[get_y(0, N)])

    eqs_to_add.append(p[get_x(N - 1, N)] - 1)
    eqs_to_add.append(p[get_y(N - 1, N)] - 1)

    return eqs_to_add

def main():
    z_range = np.linspace(-bound, bound, N)
    init_guess = [5]*(2*N)
    res = fsolve(equations, init_guess)
    plt.plot(z_range, res[N:2*N], '--')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()