numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            not_primes.append(i)
            break
    if not i in not_primes:
        primes.append(i)
           # break
print (" составные числа: ", not_primes)
print (" простые числа: ", primes)
