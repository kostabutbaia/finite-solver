import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 1

def get_A(A: float, LAMBDA: float) -> float:
    return LAMBDA*A - A**3

def get_sol_nofric(A_0: float, Av_0: float, h: float, max_r: float):
    r_range = np.arange(0, max_r, h)
    A = [A_0]

    A.append(A_0 + Av_0*h + 1/2*get_A(A_0, LAMBDA)*h**2)

    for _ in range(len(r_range) - 2):
        A_next = 2*A[-1] - A[-2] + h**2*get_A(A[-1], LAMBDA)
        A.append(A_next)

    return r_range, A

def check_crossing(sol) -> bool:
    return any([A < 0 for A in sol])

def find_A0(N: int, h: float, max_r: float, a0: float, b0: float) -> float:
    a_n, b_n = a0, b0

    for _ in range(N):
        midpoint = (a_n + b_n)/2

        _, sol_m = get_sol_nofric(midpoint, 0, h, max_r)
        if check_crossing(sol_m):
            b_n = midpoint
        else:
            a_n = midpoint
    return (a_n + b_n)/2


def main():
    # equation: A'' - lambda*A+A^3=0
    # potential U(r) = lambda*A^2 - 1/2*A^4
    A_start = np.sqrt(2*LAMBDA)

    # A0_num = find_A0(80, 0.0001, 20, A_start-0.5, A_start+0.5)

    r_range, A = get_sol_nofric(A_start, 0, 0.001, 20)

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