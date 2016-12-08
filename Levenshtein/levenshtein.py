import sys

def levenshtein(a, b, i, j):
    if min(i,j) == 0:
        return max(i,j)
    return min(
        levenshtein(a, b, i-1, j) + 1,
        levenshtein(a, b, i, j-1) + 1,
        levenshtein(a, b, i-1, j-1) + (0 if a[i-1] == b[j-1] else 1)
    )

def main(argv):
    print(levenshtein(argv[1], argv[2], len(argv[1]), len(argv[2])))

if __name__ == '__main__':
    main(sys.argv)
