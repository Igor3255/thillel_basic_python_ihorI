def sort_by_first_digit(lst):
    def get_first_digit(elem):
        if isinstance(elem, int):
            return elem // (10 ** (len(str(abs(elem))) - 1))
        elif isinstance(elem, str) and elem.isdigit():
            return int(elem[0])
        else:
            return -1

    return sorted(lst, key=get_first_digit)


lst = ["105","52","88","1", "93","356","67", "444", "0"]
lst_sorted = sort_by_first_digit(lst)
print(lst_sorted)  # виведе [1, 105, "93", 0, 356, 52, 67, 88, "444"]
