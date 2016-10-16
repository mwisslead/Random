import sys

import math

NUMWORDS = [
        '',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten',
        'eleven',
        'twelve',
        'thirteen',
        'fourteen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eighteen',
        'nineteen'
        ]

TENWORDS = [
        '',
        '',
        'twenty',
        'thirty',
        'forty',
        'fifty',
        'sixty',
        'seventy',
        'eighty',
        'ninety'
        ]

NUMBER_BREAKS = [
        '',
        'thousand',
        'million',
        'billion',
        'trillion',
        'quadrillion',
        'pentillion',
        'sextillion',
        'septillion',
        'octillion',
        'nonillion',
        'decillion',
        'undecillion',
        'duodecillion',
        'tredecillion',
        'quattuordecillion',
        'quindecillion'
        ]

def split_num(num):
    if num == 0:
        return 'zero'
    absnum = abs(num)
    n = int(math.floor(math.log10(absnum)))
    s = (2 - n % 3) * '0' + str(absnum)
    nums = (under_1000(int(s[i:i+3])) for i in range(0, len(s), 3))
    n = (n - n % 3)/3

    return ('negative ' if num < 0 else '') + ' '.join(number + ' ' + NUMBER_BREAKS[n-i] for i, number in enumerate(nums) if number).strip()

def under_100(num):
    if num == 0:
        return ''
    if num < 20:
        return NUMWORDS[num]
    n1, n2 = [int(i) for i in str(num)]
    return (TENWORDS[n1] + '-' + NUMWORDS[n2]) if n2 else TENWORDS[n1]
 
def under_1000(num):
    if num < 100:
        return under_100(num)
    s = str(num)
    n1 = int(s[0])
    n2 = int(s[1:])
    return (NUMWORDS[n1] + ' hundred ' if n1 else '') + under_100(n2)
    
def main():
    print(split_num(int(sys.argv[1])))

if __name__ == '__main__':
    main()
