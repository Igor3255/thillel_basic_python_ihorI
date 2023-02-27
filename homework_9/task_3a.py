def copydeep(orig):
    if isinstance(orig, (str, int, float, bool)):
        # якщо елемент - примітивний тип, повертаємо його без змін
        return orig
    elif isinstance(orig, list):
        # якщо елемент - список, копіюємо його елементи рекурсивно
        newlist = []
        for elem in orig:
            newlist.append(copydeep(elem))
        return newlist
    elif isinstance(orig, dict):
        # якщо елемент - словник, копіюємо його елементи рекурсивно
        newdict = {}
        for key, value in orig.items():
            newdict[key] = copydeep(value)
        return newdict
    elif isinstance(orig, tuple):
        # якщо елемент - кортеж, копіюємо його елементи рекурсивно і повертаємо новий кортеж
        newtuple = tuple([copydeep(elem) for elem in orig])
        return newtuple
    else:
        # якщо елемент не підтримується, повертаємо None
        return None


original_list = [1, 2, [3, 4, {'a': 5, 'b': 6}], 7]
copy_list = copydeep(original_list)
print(original_list == copy_list)  # True
print(original_list is copy_list)  # False

original_dict = {'a': 1, 'b': [2, 3, {'c': 4, 'd': [5, 6]}], 'e': {'f': 7}}
copy_dict = copydeep(original_dict)
print(original_dict == copy_dict)  # True
print(original_dict is copy_dict)  # False
