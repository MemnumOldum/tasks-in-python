nsyst = input('Программа переводит числа из одной системы счисления в другую. Выберите системы.'
         '(1 - из двоичной в десятичную, 2 - из шестнадцатиричной в десятичную), '
              '3 - из десятичной в шестнадцатеричную, 4 - из десятичной в двоичную \n')
input_number = input('Введите число для перевода в десятичную систему счисления \n')
generate_number = 0
lvl = 0
if nsyst == '1':
    for i in range(-1, -len(input_number) - 1, -1):
        generate_number += int(input_number[i]) * 2 ** lvl
        print(int(input_number[i]) * 2 ** lvl)
        lvl += 1
if nsyst == '2':
    list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    list2 = ['10', '11', '12', '13', '14', '15', '16']
    for i in range(-1, -len(input_number) - 1, -1):
        if input_number[i] in 'ABCDEFG':
            generate_number += int(list2[list1.index(input_number[i])]) * 16 ** lvl

        else:
            generate_number += int(input_number[i]) * 16 ** lvl
        lvl += 1
if nsyst == '3':
    n = int(input_number)
    m = 16
    s = ""
    vol = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    while n != 0:
        ch = n % m
        s = str(vol[ch]) + s
        n //= m
    generate_number = s
if nsyst == '4':
    n = int(input_number)
    m = 2
    s = ""
    vol = [0, 1]
    while n != 0:
        ch = n % m
        s = str(vol[ch]) + s
        n //= m
    generate_number = s

print(generate_number)
