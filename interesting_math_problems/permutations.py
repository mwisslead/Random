'''Generate permutations'''
def _reverse_ordered_tail(permutation):
    '''While tail items are in order, create the reversed list of them'''
    tail = [permutation[-1]]
    for item in reversed(permutation[:-1]):
        if item < tail[-1]:
            break
        tail.append(item)
    return tail

def _next_permutation(permutation):
    '''Produce the next permutation after "permutation"'''
    tail = _reverse_ordered_tail(permutation)
    if len(tail) == len(permutation):
        return
    head_len = len(permutation)-len(tail)-1
    head = permutation[:head_len]
    pivot = permutation[head_len]
    ind, middle = next((i, p) for i, p in enumerate(tail) if p > pivot)
    tail[ind] = pivot
    return head + [middle] + tail

def permutations(things):
    '''Generate all permutations of "things"'''
    permutation = list(range(len(things)))
    while permutation:
        yield [things[i] for i in permutation]
        permutation = _next_permutation(permutation)

def main():
    '''Main function for testing'''
    items = ['orange', 'apple', False, None]
    for permutation in permutations(items):
        print(permutation)

if __name__ == '__main__':
    main()
