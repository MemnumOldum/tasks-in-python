import random
num = random.randint(1, 101)
print('Добро пожаловать в числовую угадайку')
def is_valid(n):
    if n.isdigit():
        n = int(n)
        if 1 <= n <= 100:
            return True
        else:
            return False
    else:
        return False
print('Угадайте число: от 1 до 100')
p = 1
while 0 < 45 < 101:
    n1 = input()
    if is_valid(n1) == False:
        print('А может быть все-таки введем целое число от 1 до 100?')
    else:
        n1 = int(n1)
        if n1 > num:
            print('Ваше число больше загаданного, попробуйте еще раз')
        elif n1 < num:
            print('Ваше число меньше загаданного, попробуйте еще раз')
        elif n1 == num:
            print('Вы угадали число c', p, 'попыток,', 'поздравляем!')
            break
    print('Количество попыток:', p)
    p += 1
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')