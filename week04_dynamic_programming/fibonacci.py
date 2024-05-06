from time import time
from matplotlib import pyplot as plt


def fib_recursive(n):
    if n < 2:
        return n
    return (fib_recursive(n - 1) + fib_recursive(n - 2)) % 10**9


fibonacci_mem = {}


def fib_mem(n):
    if n < 2:
        return n
    if n not in fibonacci_mem:
        fibonacci_mem[n] = (fib_mem(n - 1) + fib_mem(n - 2)) % 10 ** 9
    return fibonacci_mem[n]


def fib_tab(n):
    res = [0] * max((n + 1), 2)
    res[0] = 0
    res[1] = 1
    for i in range(2, n + 1):
        res[i] = (res[i - 1] + res[i - 2]) % 10**9
    return res[n]


if __name__ == '__main__':
    times = []
    N_max = 35
    step = 1
    for i in range(1, N_max, step):
        t = time()

        # naive solution:
        x = fib_recursive(i)

        # memoization:
        # cache is resettet to calculate correct time for each i
        # otherwise it will take old values from cache:
        # fibonacci_mem = {}
        # x = fib_mem(i)

        # tabulation:
        # x = fib_tab(i)

        times.append(time() - t)
        print(f'N={i}: {times[-1]:.8f} sec.')

    plt.plot(times)
    plt.show()
