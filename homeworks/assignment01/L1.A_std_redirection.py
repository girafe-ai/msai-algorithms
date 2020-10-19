import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

x = list(map(int, input().split()))
print(sum(x))
