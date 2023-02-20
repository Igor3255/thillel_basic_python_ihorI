def index(lst, elem):
    for i in range(len(lst)):
        if lst[i] == elem:
            return i
    return None


lst = [3, 5, 1, 8, 2]
print(index(lst, 1))  # виведе 2
print(index(lst, 6))  # виведе None
