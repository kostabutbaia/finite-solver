import numpy as np
import matplotlib.pyplot as plt

OMEGA = 0.8

def g(a, psi) -> float:
    if np.abs(a) > 10 or np.abs(psi) > 10:
        return 100
    return (1+psi)*((1+psi)**2-a**2)-1

def f(a, psi) -> float:
    if np.abs(a) > 10 or np.abs(psi) > 10:
        return 100
    return a*((1+psi)**2-a**2)-OMEGA**2*a

def get_sol(h: float, psi0: float, a0: float, psi0_v: float, a0_v: float, max_r: float):
    r_range = np.arange(0, max_r, h)
    
    a_v = [a0_v]
    a = [a0]
    
    psi_v = [psi0_v]
    psi = [psi0]

    for _ in range(len(r_range) - 1):
        a_v_next = a_v[-1] + h*f(a[-1], psi[-1])
        a_next = a[-1] + h*a_v[-1]

        psi_v_next = psi_v[-1] + h*g(a[-1], psi[-1])
        psi_next = psi[-1] + h*psi_v[-1]

        a_v.append(a_v_next)
        psi_v.append(psi_v_next)
        psi.append(psi_next)
        a.append(a_next)

    return r_range, a, psi

def check_crossing(sol) -> bool:
    return any([A < 0 for A in sol])

def find_0(N: int, h: float, max_r: float, a0: float, b0: float) -> float:
    a_n, b_n = a0, b0

    for _ in range(N):
        midpoint = (a_n + b_n)/2

        _, sol_m, _ = get_sol(h, midpoint, 2*midpoint, 0 ,0, max_r)
        if check_crossing(sol_m):
            a_n = midpoint
        else:
            b_n = midpoint
    return (a_n + b_n)/2

def main():
    a0 = np.sqrt(1-OMEGA**6)/OMEGA**2
    psi0 = (1-OMEGA**2)/OMEGA**2
    print(a0, psi0)
    # for c in np.linspace(0.5, 2, 50):
    #     a0 = c*np.sqrt(1-OMEGA**6)/OMEGA**2
    #     psi0 = c*(1-OMEGA**2)/OMEGA**2
    #     r_range, a, psi = get_sol(0.01, psi0, a0, 0, 0, 5)

    #     plt.plot(r_range, psi)

    plt.xlim([0, 5])
    plt.ylim([-2, 2])
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()