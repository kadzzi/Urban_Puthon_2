num_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

my_list = []
while len(num_list) != 0:
    current = num_list.pop(0)
    if current < 0:
        break
    if current > 0:
        print(current)
