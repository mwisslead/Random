'''Generate sequence of n symbols that alternate in a fair manner'''

def thue_morse(n, b=2):
    '''generate the nth symbol given b symbols to choose from'''
    if n < b:
        return n
    r = n % b
    return (thue_morse((n-r)//b, b) + r) % b

def main():
    '''Main'''
    import matplotlib.pyplot as plt
    import numpy as np
    num = 3
    iterations = num**4
    sequence = np.zeros((num, iterations+1))
    for n in range(iterations):
        sequence[:, n+1] = sequence[:, n]
        sequence[thue_morse(n, num), n+1] += 1
    plt.plot(sequence.T)
    plt.show()

if __name__ == '__main__':
    main()
