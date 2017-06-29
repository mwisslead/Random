from __future__ import print_function, division

import struct

class new_int(int):
    def __init__(self, val):
        super(type(self), self).__init__(val)

    def __neg__(self):
        return type(self)(~self + 1)

    def __sub__(self, val):
        val = type(self)(val)
        return type(self)(self + (-val))

    def __lshift__(self, val):
        val = type(self)(val)
        return type(self)(super(type(self), self).__lshift__(val))

    def __mul__(self, val):
        val = type(self)(val)
        valsign = val < 0
        if valsign:
            val = -val
        product = type(self)(sum(self << i for i in range(self.bit_length() + val.bit_length()) if val & (1 << i)))
        return -product if valsign else product

    def bit_length(self):
        return type(self)(super(type(self), self).bit_length())

    def div_rem(self, val):
        if val == 0:
            raise ZeroDivisionError('integer division or modulo by zero')
        val = type(self)(val)
        rem = type(self)(self)
        remsign = rem < 0
        valsign = val < 0
        if remsign:
            rem = -rem
        if valsign:
            val = -val
        result = type(self)(0)
        while rem >= val:
            bitdiff = (rem.bit_length() - val.bit_length() or 1) - 1
            result += type(self)(1) << bitdiff
            rem -= (val << bitdiff)
        if remsign != valsign:
            if rem == 0:
                result = -result
            else:
                result = ~result
        if valsign and rem:
            if remsign:
                rem = -rem
            else:
                rem -= val
        elif remsign and rem:
            rem = val - rem
        return result, rem

    def __div__(self, val):
        return self.__floordiv__(val)

    def __floordiv__(self, val):
        return self.div_rem(val)[0]

    def __mod__(self, val):
        return self.div_rem(val)[1]

    def __truediv__(self, val):
        if val == 0:
            raise ZeroDivisionError('float division by zero')
        val = type(self)(val)
        rem = type(self)(self)
        remsign = rem < 0
        valsign = val < 0
        if remsign:
            rem = -rem
        if valsign:
            val = -val
        result = new_int(0)
        mantissa = new_int(0)
        while result.bit_length() < 62:
            if rem == 0:
                break
            if rem < val:
                rem <<= 1
                mantissa -= 1
                result <<= 1
                continue
            bitdiff = (rem.bit_length() - val.bit_length() or 1) - 1
            result += 1 << bitdiff
            rem -= val << bitdiff
        if result != 0:
            mantissa -= 1 - result.bit_length() - 1023
            bitdiff = result.bit_length() - 54
            if bitdiff > 0:
                result >>= bitdiff
            else:
                result <<= -bitdiff
            if result & 1:
                result += 1
            result = (result >> 1) & 0xFFFFFFFFFFFFF
        float_bytes = bytearray(struct.pack('>Q', result))
        float_bytes[0] += mantissa >> 4
        float_bytes[1] += (mantissa & 0x0F) << 4
        if remsign != valsign:
            float_bytes[0] += 0x80
        return struct.unpack('>d', float_bytes)[0]


def main():
    ints = [-2, 2, -5, 5, -8, 8, -13, 13, -27, 27, -54, 54, -210, 210]
    for a in ints + [0]:
        for b in ints:
            an = new_int(a)
            bn = new_int(b)
            print(a - b, an - bn)
            assert a - b == an - bn, (a, b)
            print(a * b, an * bn)
            assert a * b == an * bn, (a, b)
            print(a // b, an // bn)
            assert a // b == an // bn, (a, b)
            print(a % b, an % bn)
            assert a % b == an % bn, (a, b)
            print(a / b, an / bn)
            assert a / b == an / bn, (a, b)

if __name__ == '__main__':
    main()
