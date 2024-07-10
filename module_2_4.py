numbers = list(range(1, 16))

not_primes = []
primes = []

for candidate in numbers[1:]:
    divisors = list(range(2, candidate // 2 + 1))
    if len(divisors) == 0:
        primes.append(candidate)
        continue
    flag = 1
    for divisor in divisors:
        if candidate % divisor != 0:
            continue
        else:
            flag = 0
            not_primes.append(candidate)
            break
    if flag:
        primes.append(candidate)

print(primes)
print(not_primes)
