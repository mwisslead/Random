'''Generate consecutive triplets that are all the sum of two squares'''
from __future__ import division, print_function

import argparse

def parse_args(argv=None):
    '''Parse arguments'''
    parser = argparse.ArgumentParser(
        description='Generate consecutive triplets that are all the sum of two squares')
    parser.add_argument('number', metavar='number', help='number of triplets to print', type=int)
    return parser.parse_args(argv)

def consecutive_squares(ind):
    '''Generate consecutive triplet numbers to square'''
    base = ind**2 + ind
    return [
        [base, base],
        [abs(base - ind - 1), base + ind],
        [abs(base - 1), base + 1]
    ]

def main(argv=None):
    '''Main'''
    args = parse_args(argv)
    print(args)
    for ind in range(args.number):
        consecutive_parts = consecutive_squares(ind)
        for nums in consecutive_parts:
            print('%d = %d**2 + %d**2' % (nums[0]**2 + nums[1]**2, nums[0], nums[1]))

if __name__ == '__main__':
    main()
