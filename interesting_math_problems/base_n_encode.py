'''convert between string of bytes with 256 possible values and n possible values'''

from __future__ import print_function

STANDARD_CHARS = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def base_n_convert(int_list, base, new_base):
    '''convert list of ints from base to new_base'''
    if base < 2 or new_base < 2:
        raise ValueError('Number bases must be >= 2')
    output = []
    conv = base % new_base
    while any(int_list):
        new_base_digit, val_base_mod = 0, 1
        for val in int_list:
            new_base_digit += (val * val_base_mod) % new_base
            val_base_mod = (val_base_mod * conv) % new_base
        new_base_digit %= new_base
        output.append(new_base_digit)
        int_list[0] -= new_base_digit
        for i in range(len(int_list) - 1, 0, -1):
            remainder = int_list[i] % new_base
            int_list[i] = (int_list[i] - remainder) // new_base
            int_list[i-1] += remainder * base
        int_list[0] //= new_base
    return output

def base_n_encode(bytestr, encode_chars=STANDARD_CHARS):
    '''convert bytestr to str only containing encode_chars'''
    if isinstance(bytestr, str):
        bytestr = [ord(c) for c in bytestr]
    int_list = base_n_convert(list(bytestr), 256, len(encode_chars))
    return bytes(bytearray(encode_chars[x] for x in int_list))

def base_n_decode(bytestr, encode_chars=STANDARD_CHARS):
    '''convert bytestr only containing encode_chars to 256 values'''
    int_list = [encode_chars.index(c) for c in bytestr]
    return bytes(bytearray(base_n_convert(int_list, len(encode_chars), 256)))

def main():
    '''test cases'''
    teststr = b''
    encode_chars = b'abc'
    print(base_n_decode(base_n_encode(teststr, encode_chars), encode_chars))
    teststr = b'atebytes'
    encode_chars = b'abc'
    print(base_n_decode(base_n_encode(teststr, encode_chars), encode_chars))
    teststr = b'seven'
    encode_chars = b'01234567'
    print(base_n_decode(base_n_encode(teststr, encode_chars), encode_chars))
    teststr = b'atebytes'
    encode_chars = b'0'
    print(base_n_encode(teststr, encode_chars))

if __name__ == '__main__':
    main()
