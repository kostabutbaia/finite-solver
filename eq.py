import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

bound = 20

N = 400
h = bound/(N-1)

LAMBDA = 0.1

def get_A(i: int) -> int:
    return i

def equations(p, z_range):
    eqs_to_add = []

    # Add equation from y
    for i in range(1, N - 1):
        eqs_to_add.append(
            (p[get_A(i+1)] - 2*p[get_A(i)] + p[get_A(i-1)])/h**2 + \
            LAMBDA*p[get_A(i)] + p[get_A(i)]**3 
        )
    
    # Boundary Conditions
    eqs_to_add.append(p[get_A(0)] - 1.8)
    eqs_to_add.append(p[get_A(N - 1)])

    return eqs_to_add

def main():
    z_range = np.linspace(0, bound, N)
    init_guess = [2]*(N)
    res = fsolve(equations, init_guess, args=z_range)
    plt.plot(z_range, res, '--')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()