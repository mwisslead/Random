import argparse

import numpy as np
import scipy.stats


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description='xorcrack attempts to determine the ')
    parser.add_argument("key_min", help="minimum key length to try", type=int)
    parser.add_argument("key_max", help="maximum key length to try", type=int)
    parser.add_argument("common", help="most common character in decoded message", type=str)
    parser.add_argument("msg", help="file containing encrypted message", type=str)
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    x = np.array(range(args.key_min, args.key_max+1))

    orig = np.fromfile(args.msg, dtype=np.uint8)

    orig_len = orig.size
    length = len(orig) - args.key_max

    y = np.array([length - np.count_nonzero(orig[:length] ^ orig[shift:length+shift]) for shift in x])

    shift = x[list(y).index(max(y))]

    print('Determined key length: {}'.format(shift))

    pad_width = shift - (len(orig) % shift)
    padwidth = pad_width if pad_width != shift else 0
    orig = np.pad(orig, (0, padwidth), mode='constant')

    orig = np.reshape(orig, (orig.size//shift, shift))

    key = np.squeeze(scipy.stats.mode(orig, axis=0)[0]) ^ ord(args.common)
    
    print('Key determined to be: {}'.format(key.tostring()))
    orig ^= key

    print('Deciphered Message:')
    print(orig.flatten()[:orig_len].tostring())


if __name__ == '__main__':
    main()
