import numpy as np
import matplotlib.pyplot as plt

OMEGA = 0.7683

def check_crossing(sol) -> bool:
    return any([A < 0 for A in sol])

def find_A0(N: int, h: float, max_r: float, a0: float, b0: float) -> float:
    a_n, b_n = a0, b0

    for _ in range(N):
        midpoint = (a_n + b_n)/2

        _, sol_m = get_sol(h, midpoint, 0, max_r)
        if check_crossing(sol_m):
            b_n = midpoint
        else:
            a_n = midpoint
    return (a_n + b_n)/2

def get_A(a) -> float:
    return a*(1-OMEGA**2) - 0.5*(1 - 1/3)*a**3

def get_sol(h: float, a0: float, a0_v: float, max_r: float):
    r_range = np.arange(0, max_r, h)
    a = [a0]
    
    
    return r_range, a

def main():
    a0 = find_A0(100, 0.1, 20, 1, 2)
    print(a0)
    r_range, a = get_sol(0.1, a0, 0, 20)

    plt.plot(r_range, a)
    plt.xlim([0, 10])
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()