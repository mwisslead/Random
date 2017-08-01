import os
import glob
import sys

import base_n_encode

def main():
    wordlist = sys.argv[1] # name of file containing '\n' seperated words. Tested with one from https://github.com/first20hours/google-10000-english
    with open(wordlist, 'rb') as fid:
        words = [word for word in fid.read().decode('ascii').split('\n') if word]

    print(' '.join(words[i] for i in base_n_encode.base_n_convert(list(os.urandom(10)), 256, len(words))))

if __name__ == '__main__':
    main()
