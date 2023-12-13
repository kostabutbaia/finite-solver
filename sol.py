import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 1

def get_A(A: float, LAMBDA: float) -> float:
    return LAMBDA*A - A**3

def get_sol(A_0: float, Av_0: float, h: float, max_r: float):
    r_range = np.arange(0, max_r, h)
    A = [A_0]

    A.append(A_0 + Av_0*h + 1/2*get_A(A_0, LAMBDA)*h**2)

    for _ in range(len(r_range) - 2):
        A_next = 2*A[-1] - A[-2] + h**2*get_A(A[-1], LAMBDA)
        A.append(A_next)

    return r_range, A

def main():
    # equation: A'' - lambda*A+A^3=0
    # potential U(r) = lambda*A^2 - 1/2*A^4
    A_start = np.sqrt(2*LAMBDA)
    print(A_start)
    r_range, A = get_sol(A_start, 0, 0.0001, 20)

    # plot minimums
    plt.plot(r_range, [np.sqrt(LAMBDA)]*len(r_range), 'r--')
    plt.plot(r_range, [-np.sqrt(LAMBDA)]*len(r_range), 'r--')

    # plot solution
    plt.plot(r_range, A, 'b')
    plt.grid()
    plt.ylim([-2, 2])
    plt.show()



if __name__ == '__main__':
    main()