primes = [2, 3, 5, 7, 11, 13, 17, 19]
actual_primes = [2, 3, 5, 7]

input_value = int(input('Input number in [3, 4, ..., 20] '))

quotient = input_value
decomposition = []
#quotients = [input_value]
for divider in actual_primes:
    while quotient % divider == 0:
        quotient /= divider
        decomposition.append(divider)
        # if quotient != 1:
        #     quotients.append(int(quotient))


print(decomposition)


#print(quotients)

#left_n = list(range(1, input_value // 2))
#right_n = [input_value - x for x in left_n]
#print(list(zip(left_n, right_n)))

# all_pairs = []
# for item in quotients[::-1]:
#     left_n = list(range(1, int(item // 2 + 1)))
#     right_n = [item - x for x in left_n]
#     all_pairs.extend(list(zip(left_n, right_n)))
#     if all_pairs[-1][0] == all_pairs[-1][1]:
#         del all_pairs[-1]
#
# all_pairs.sort()
# #print(all_pairs)
# print(''.join([''.join(map(str, x)) for x in all_pairs]))

#print([''.join(str(x)) for x in [''.join(str(all_pairs[i]) for i, z in enumerate(all_pairs))]])

