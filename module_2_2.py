first, second, third = [input(f'Введите {str(x)} число: ') for x in ['1-е', '2-е', '3-е']]

uniq_num = {first, second, third}

if len(uniq_num) == 1:
    print(3)
elif len(uniq_num) == 2:
    print(2)
else:
    print(0)
