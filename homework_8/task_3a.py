def custom_sort(elem):
    if isinstance(elem, str):
        return int(elem)
    else:
        return elem

lst = ["5", "2", "8", "1", "9", "3", "6", "7", "4", "3.14", "2.71"]
lst_sorted = sorted(lst, key=custom_sort)
print(lst_sorted)  # выведет ["1", "2", "3", "4", "2.71", "3.14", "5", "6", "7", "8", "9"]
