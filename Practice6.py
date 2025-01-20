S1 = input('Введите строку: ')
count = 0
for i in range(len(S1)):
    if S1[i] == ':':
        count += 1
print('Заменённая строка: ', S1.replace(':','%'))
print('Количество замен: ', count)
