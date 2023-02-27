import random

def diff_min_max(num_limit, lower_bound, upper_bound):
    nums = [random.randint(lower_bound, upper_bound) for _ in range(num_limit)]
    return max(nums) - min(nums)


