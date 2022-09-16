import math
import re
import sys


""" Reads in the displacements produced by beadtracker.py from standard
input; computes an estimate of Boltzmann's constant and Avogadro's number;
and writes those estimates to standard output. """

"""
whe have to add jpg one by one inorder to print output or get dsplacment files of text files
"""

def isEmpty():
    """
    Return True if no non-whitespace characters remain
    """
    global _buffer
    while _buffer.strip() == '':
        line = sys.stdin.readline()
        if sys.hexversion < 0x03000000:
            line = line.decode('utf-8')
        if line == '':
            return True
        _buffer += line
    return False


def _readRegExp(regExp):

    global _buffer
    if isEmpty():
        raise EOFError()
    compiledRegExp = re.compile(r'^\s*' + regExp)
    match = compiledRegExp.search(_buffer)
    if match is None:
        raise ValueError()
    s = match.group()
    _buffer = _buffer[match.end():]
    return s.lstrip()


def readFloat():
    """
    Discard leading white space characters from standard input
    """
    s = _readRegExp(r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?')
    return float(s)


def main():
    n = 0
    Var = .00
    while not isEmpty():
        a = readFloat() * (.175 * (10 ** -6))
        Var += a * a
        n += 1
    Var = Var / (2 * n)
    VIS = 9.135 * 10 ** -4
    RO = 0.5 * 10 ** -6
    T = 297.0
    R = 8.31457
    k = 6 * ( math.pi * Var * VIS * RO ) / T
    N_A = R / k
    print('Boltzman = %e\nAvogadro = %e\n', k, N_A)


if __name__ == '__main__':
    main()
