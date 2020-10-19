with open('input.txt', 'r') as f:
    x = list(map(int, f.read().split()))
with open('output.txt', 'w') as f:
    f.write(str(sum(x)))
    f.write('\n')
