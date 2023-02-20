def sort_by_number(lst):
    def get_number(elem):
        return int(elem) if isinstance(elem, str) and elem.isdigit() else 0

    return sorted(lst, key=get_number)


lst = ["5", "2", "8", "1", "9", "3", "6", "7", "4"]
lst_sorted = sort_by_number(lst)
print(lst_sorted)  # виведе ["1", "2", "3", "4", 5, "6", "7", "8", "9"]
