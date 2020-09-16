import math
import stdio


""" Reads in the displacements produced by beadtracker.py from standard
input; computes an estimate of Boltzmann's constant and Avogadro's number;
and writes those estimates to standard output. """

"""
whe have to add jpg one by one inorder to print output or get dsplacment files of text files
"""

def main():
    n = 0
    Var = .00
    while not stdio.isEmpty():
        a = stdio.readFloat() * (.175 * (10 ** -6))
        Var += a * a
        n += 1
    Var = Var / (2 * n)
    VIS = 9.135 * 10 ** -4
    RO = 0.5 * 10 ** -6
    T = 297.0
    R = 8.31457
    k = 6 * ( math.pi * Var * VIS * RO ) / T
    N_A = R / k
    stdio.writef('Boltzman = %e\nAvogadro = %e\n', k, N_A)

if __name__ == '__main__':
    main()
