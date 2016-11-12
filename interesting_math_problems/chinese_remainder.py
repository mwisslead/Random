'''Calculate the small nonnegativenumber with specified remainders'''
from __future__ import division

import argparse

class Congruences(argparse.Action):
    '''class to check argument parsing'''
    def __call__(self, parser, namespace, values, option_string=None):
        if len(values) % 2 != 0:
            raise argparse.ArgumentTypeError('Congruences must contain pairs of integers')
        if len(values) < 4:
            raise argparse.ArgumentTypeError('Congruences must contain atleast two pairs of'
                                             ' integers')
        values = [(r, p) for r, p in zip(values[::2], values[1::2])]
        setattr(namespace, self.dest, values)

def parse_args(argv=None):
    '''Parse arguments'''
    parser = argparse.ArgumentParser(description='Calculate smallest nonnegative'
                                     'number with specified remainders')
    parser.add_argument('congruences', metavar='congruences', nargs='+', type=int,
                        action=Congruences)
    return parser.parse_args(argv)

def gcd(a, b):
    '''Greatest Commond Divisor'''
    while b != 0:
        a, b = b, a % b
    return a

def inverse(a, n):
    '''Calculate modulo inverse using extended euclid algorithm.'''
    t, next_t = 0, 1
    r, next_r = n, a
    while next_r != 0:
        quotient = r//next_r
        t, next_t = next_t, t - quotient * next_t
        r, next_r = next_r, r - quotient * next_r
    if r > 1:
        raise ValueError("No inverse")
    if t < 0:
        t = t + n
    return t

def mutuallyprime(*kwargs):
    '''Determine if list of numbers is mutually prime'''
    if len(kwargs) == 1:
        kwargs = kwargs[0]
    for i, num1 in enumerate(kwargs):
        for j, num2 in enumerate(kwargs):
            if i != j and gcd(num1, num2) != 1:
                return False
    return True

def solver(*kwargs):
    '''solve system of congruences defined by kwargs'''
    if len(kwargs) == 1:
        kwargs = kwargs[0]
    moduli = [k[1] for k in kwargs]
    if len(moduli) == 0 or not mutuallyprime(moduli):
        raise ValueError('not mutually prime')
    remainder = kwargs[0][0]
    modulo = kwargs[0][1]
    for next_remainder, next_modulo in kwargs[1:]:
        inv = inverse(modulo, next_modulo)
        i = (next_remainder - remainder) * inv
        i *= modulo
        remainder += i
        modulo *= next_modulo
        remainder %= modulo
    return remainder

def general_formula(moduli):
    s = 96
    output = ''
    final = 1
    for i, _ in enumerate(moduli):
        congruences = [(int(j == i), mod) for j, mod in enumerate(moduli)]
        s += 1
        output += '{} * {} + '.format(solver(congruences), chr(s))
        final *= congruences[i][1]
    return '({}) % {}'.format(output[:-3], final)

def main(argv=None):
    '''Main'''
    args = parse_args(argv)
    print(solver(args.congruences))
    print(general_formula([c[1] for c in args.congruences]))

if __name__ == '__main__':
    main()
