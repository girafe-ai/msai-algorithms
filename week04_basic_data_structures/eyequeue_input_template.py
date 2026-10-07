# This is input template for W3.C EyeQueue problem.

import sys

if __name__ == '__main__':
    # Uncomment these lines to use file input/output:
    # sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('output.txt', 'r')

    N = int(input())

    # here comes initialization code if needed

    for line in sys.stdin:
        cmd = line.split()
        c_i = cmd[0]
        q_i = int(cmd[1]) if len(cmd) > 1 else None
        id_i = int(cmd[2]) if len(cmd) > 2 else None

        if c_i == '#':
            break
        elif c_i == '+':
            # Your code goes here
            pass
        elif c_i == '!':
            # Your code goes here
            pass
        elif c_i == '-':
            # Your code goes here
            pass
        elif c_i == '?':
            # Your code goes here
            pass
