def sort_by_first_digit(lst):
    return sorted(lst, key=lambda x: str(x)[0] if isinstance(x, str) and x.isdigit() else str(x))

lst = ["105", "52", "88", "1", "93", "356", "67", "444", "0"]
lst_sorted = sort_by_first_digit(lst)
print(lst_sorted)  # выведет ["1", "105", "93", "0", "356", "52", "67", "88", "444"]
