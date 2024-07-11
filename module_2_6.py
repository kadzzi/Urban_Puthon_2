primes = [2, 3, 5, 7, 11, 13, 17, 19]

input_value = int(input('Input number in [3, 4, ..., 20]: '))

quotient = input_value
decomposition = []
quotients_up = [input_value]
for divider in primes:
    while quotient % divider == 0:
        quotient /= divider
        decomposition.append(divider)
        if quotient != 1:
            quotients_up.append(int(quotient))

quotient = input_value
quotients_down = [input_value]
for divider in primes[::-1]:
    while quotient % divider == 0:
        quotient /= divider
        if quotient != 1:
            quotients_down.append(int(quotient))


print(f'Prime divisors: {decomposition}')
quotients = list(set(quotients_up).union(set(quotients_down)))
quotients.sort()
print(f'All divisible numbers: {quotients}\n')

all_pairs = []
for item in quotients:
    left_n = list(range(1, int(item // 2 + 1)))
    right_n = [item - x for x in left_n]
    all_pairs.extend(list(zip(left_n, right_n)))
    if all_pairs[-1][0] == all_pairs[-1][1]:
        del all_pairs[-1]

all_pairs.sort()
result = ''.join([''.join(map(str, x)) for x in all_pairs])
print(f'Key for {input_value} is {result}')
