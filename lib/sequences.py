#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0 :
        print([])

    elif length == 1 :
        print([0])

    elif length == 2 :
        print ([0, 1])

    else:
        fib = [0, 1]
        while len(fib) < length:
            next_num = fib[-1] + fib[-2]
            fib.append(next_num)
        print(fib)