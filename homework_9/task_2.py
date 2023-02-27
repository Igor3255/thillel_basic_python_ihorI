import random

def diff_odd_even(num_limit, lower_bound, upper_bound):
    even_sum = 0
    odd_sum = 0
    count = 0
    while count < num_limit:
        num = random.randint(lower_bound, upper_bound)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
        count += 1
    return even_sum - odd_sum


