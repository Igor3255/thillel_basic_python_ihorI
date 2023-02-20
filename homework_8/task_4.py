def gen_primes():
    primes = []
    is_prime = [True] * 101  # запускаємо список is_prime з True для всіх елементів від 0 до 100
    for p in range(2, 101):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, 101, p):  # позначаємо всі кратні p числа як "не прості"
                is_prime[i] = False
    return primes


primes = gen_primes()
print(primes)
