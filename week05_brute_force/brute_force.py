def permutations(x: list, perm=None):
    if perm is None:
        perm = []
    if len(x) == 0:
        yield perm
    for i in range(len(x)):
        yield from permutations(x[:i] + x[i+1:], perm + [x[i]])


def subsets(x, subset=None):
    if subset is None:
        subset = []
    if len(x) == 0:
        yield subset
    else:
        yield from subsets(x[1:], subset)
        yield from subsets(x[1:], subset + [x[0]])


def strings(x, n, string=''):
    if n == 0:
        yield string
    else:
        for v in x:
            yield from strings(x, n-1, string + v)


def permutations(x: list, perm=None):
    if perm is None:
        perm = []
    if len(x) == 0:
        yield perm
    for i in range(len(x)):
        yield from permutations(x[:i] + x[i+1:], perm + [x[i]])


def subsets(x, subset=None):
    if subset is None:
        subset = []
    if len(x) == 0:
        yield subset
    else:
        yield from subsets(x[1:], subset)
        yield from subsets(x[1:], subset + [x[0]])


def strings(x, n, string=''):
    if n == 0:
        yield string
    else:
        for v in x:
            yield from strings(x, n-1, string + v)


def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                continue
            for digit in range(1, 10):
                # function fits() check that this choice do has no condratiction with the rules:
                if not fits(board, row, col, digit):
                    continue
                board[row][col] = digit
                if solve(board):
                    return True
                # Otherwise,the choice was
                # incorrect,let’s clean it:
                board[row][col] = 0
                # Deeper cells are already cleaned.
            return False
    return True
