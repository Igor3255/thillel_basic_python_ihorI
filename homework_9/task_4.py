import itertools

def lchain(*iterables):
    return list(itertools.chain(*iterables))


assert lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)) == [1, 2, 3, '5', 6, 7, 8, 9]

