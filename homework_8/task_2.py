def copydeep(obj):
    if isinstance(obj, (str, int, float)):
        return obj
    elif isinstance(obj, list):
        copy = []
        for item in obj:
            copy.append(copydeep(item))
        return copy
    elif isinstance(obj, tuple):
        copy = ()
        for item in obj:
            copy += (copydeep(item),)
        return copy


lst = [1, 2, [3, 4], 5]
lst_copy = copydeep(lst)
lst[2][0] = 10  # змінюємо елемент списку на глибині
print(lst)  # виведе [1, 2, [10, 4], 5]
print(lst_copy)  # виведе [1, 2, [3, 4], 5], копія не має змінюватися
