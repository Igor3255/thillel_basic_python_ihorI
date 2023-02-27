def group_by_surname(list_of_enrollees):
    groups = [0, 0, 0, 0]
    for enrollee in list_of_enrollees:
        surname = enrollee.split()[1]
        if surname[0] >= 'A' and surname[0] <= 'I':
            groups[0] += 1
        elif surname[0] >= 'J' and surname[0] <= 'P':
            groups[1] += 1
        elif surname[0] >= 'Q' and surname[0] <= 'T':
            groups[2] += 1
        elif surname[0] >= 'U' and surname[0] <= 'Z':
            groups[3] += 1
    return tuple(groups)


enrollees = ['John Smith', 'Jane Doe', 'Will Turner', 'Sarah Williams', 'Alicia Keys']
groups = group_by_surname(enrollees)
print(groups) # (2, 1, 1, 1)
