import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

bound = 15

N = 100
h = 2*bound/(N-1)

lmbd = -0.4
H = 6

def get_W(i: int, N_points: int) -> int:
    return i

def get_P(i: int, N_points: int) -> int:
    return N_points + i

def get_phi(i: int, N_points: int) -> int:
    return 2*N_points + i

def equations(p):
    eqs_to_add = []

    # Add equation from W
    for i in range(1, N - 1):
        eqs_to_add.append(
            (p[get_W(i+1, N)] - 2*p[get_W(i, N)] + p[get_W(i-1, N)])/h**2 + \
            (lmbd - p[get_P(i, N)]**2/(1+p[get_W(i, N)]**2)**(1/2) + 1)*p[get_W(i, N)]
        )

    # Add equation from P
    for i in range(1, N - 1):
        eqs_to_add.append(
            H**2/2*(p[get_P(i+1, N)] - 2*p[get_P(i, N)] + p[get_P(i-1, N)])/h**2 + \
            (p[get_phi(i, N)]-(1+p[get_W(i, N)]**2)**(1/2) + 1)*p[get_P(i, N)]
        )

    # Add equation from phi
    for i in range(1, N - 1):
        eqs_to_add.append(
            (p[get_phi(i+1, N)] - 2*p[get_phi(i, N)] + p[get_phi(i-1, N)])/h**2 + \
            (1-p[get_P(i, N)]**2)
        )
    
    # Boundary Conditions
    eqs_to_add.append(p[get_W(0, N)])
    eqs_to_add.append(p[get_W(N - 1, N)])

    eqs_to_add.append(p[get_P(0, N)] - 1)
    eqs_to_add.append(p[get_P(N - 1, N)] - 1)

    eqs_to_add.append(p[get_phi(0, N)])
    eqs_to_add.append(p[get_phi(N - 1, N)])

    return eqs_to_add

def main():
    z_range = np.linspace(-bound, bound, N)
    init_guess = [1]*(3*N)
    res = fsolve(equations, init_guess)
    print(res[N:2*N][0], res[N:2*N][-1])
    plt.plot(z_range, res[:N], label='W')
    plt.plot(z_range, res[N:2*N], label='P')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()