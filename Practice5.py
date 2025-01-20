a = int(input('Введите целое число: '))
if a < 2:
    print('Число меньше 2')
else:
    for i in range(2, a+1):
        if a % i == 0:
            print(i)
            break
