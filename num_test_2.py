import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

bound = 15

N = 150
h = 2*bound/(N-1)
OMEGA = 0.7683
epsilon = 1

def get_a(i: int, N_points: int) -> int:
    return i

def get_psi(i: int, N_points: int) -> int:
    return N_points + i

def N_func(a: float, psi: float, epsilon: float) -> float:
    return (1 + psi)/(epsilon**(3/2)*((1 + psi)**2 - a**2)**(1/2))*((1 + psi)**2-(1 + a**2-epsilon))**(3/2)

def N_func_2(a: float, psi: float) -> float:
    return (1 + psi)*((1 + psi)**2- a**2)

def equations(p, z_range):
    eqs_to_add = []

    # Add equation from a
    for i in range(1, N - 1):
        eqs_to_add.append(
            (p[get_a(i+1, N)] - 2*p[get_a(i, N)] + p[get_a(i-1, N)])/h**2 - \
            (1-OMEGA**2)*p[get_a(i, N)] + \
            1/z_range[i]*(p[get_a(i+1, N)] - p[get_a(i, N)])/h + \
            (1-N_func_2(p[get_a(i, N)], p[get_psi(i, N)])/(1+p[get_psi(i, N)]))*p[get_a(i, N)]
        )

    # Add equation from psi
    for i in range(1, N - 1):
        eqs_to_add.append(
            (p[get_psi(i+1, N)] - 2*p[get_psi(i, N)] + p[get_psi(i-1, N)])/h**2 + \
            1/z_range[i]*(p[get_psi(i+1, N)] - p[get_psi(i, N)])/h + \
            (1-N_func_2(p[get_a(i, N)], p[get_psi(i, N)]))
        )
    
    # Boundary Conditions
    eqs_to_add.append(p[get_a(0, N)])
    eqs_to_add.append(p[get_a(N - 1, N)])

    eqs_to_add.append(p[get_psi(0, N)])
    eqs_to_add.append(p[get_psi(N - 1, N)])

    return eqs_to_add

def main():
    z_range = np.linspace(-bound, bound, N)
    guess = 2.2727272727272725
    # guess = 2.3727272727272725
    init_guess = [guess]*(2*N)
    res = fsolve(equations, init_guess, args=z_range)
    plt.plot(z_range, res[:N], label='a')
    plt.plot(z_range, res[N:2*N], label='psi')

    # N_points = []
    # for i in range(len(z_range)):
    #     N_points.append(N_func_2(res[:N][i], res[N:2*N][i]))

    # plt.plot(z_range, N_points, label='N')
    plt.grid()
    plt.xlim([0, bound])
    plt.legend()
    plt.show()


    # guesses = np.linspace(0, 5, 12)
    # for i in guesses:
    #     init_guess = [i]*(2*N)
    #     res = fsolve(equations, init_guess)
    #     plt.plot(z_range, res[:N], label=f'{i}')

if __name__ == '__main__':
    main()