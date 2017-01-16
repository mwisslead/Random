'''Find the area of the largest rectangle inside histogram'''

def pop_stack(current_max, pos, stack):
    '''Remove item from stack and return area and start position'''
    start, height = stack.pop()
    return max(current_max, height * (pos - start)), start

def largest_rectangle(hist):
    '''Find area of largest rectangle inside histogram'''
    current_max = 0
    stack = []
    i = -1
    for i, height in enumerate(hist):
        if not stack or height > stack[-1][1]:
            stack.append((i, height))
        elif height < stack[-1][1]:
            while stack and height < stack[-1][1]:
                current_max, start = pop_stack(current_max, i, stack)
            stack.append((start, height))
    while stack:
        current_max = pop_stack(current_max, i+1, stack)[0]
    return current_max

def main():
    '''Main function for testing'''
    print(largest_rectangle([1, 3, 5, 3, 0, 2, 3, 3, 1, 0, 3, 6]))
    print(largest_rectangle([1, 3, 5, 3, 2, 2, 3, 3, 1, 0, 3, 6]))
    print(largest_rectangle([1, 2, 3, 1, 1]))

if __name__ == '__main__':
    main()
