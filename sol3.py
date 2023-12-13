import numpy as np

OMEGA = 1

def N(a: float, psi: float, epsilon: float) -> float:
    return (1 + psi)/(epsilon**(3/2)*((1 + psi)**2 - a**2)**(1/2))*((1 + psi)**2-(1 + a**2-epsilon))**(3/2)

def N_2(a: float, psi: float) -> float:
    return (1 + psi)*((1 + psi)**2- a**2)

def get_A_psi(a, psi) -> float:
    return N_2(a, psi) - 1

def get_A_a(a, psi) -> float:
    return a*((1-OMEGA**2) + N_2(a, psi)/(1+psi) - 1)

def get_sol(h: float, psi0: float, a0: float, psi0_v: float, a0_v: float):
    psi = [psi0]
    a = [a0]
    
    psi.append(psi0 + psi0_v*h + 1/2*get_A_psi(a0, psi0)*h**2)
    a.append(a0 + a0_v*h + 1/2*get_A_a(a0, psi0)*h**2)


def main():
    pass


if __name__ == '__main__':
    main()