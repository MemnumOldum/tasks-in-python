import random
digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
excOn_letters = 'il1Lo0O'
chars = ''
cntPw = int(input('Укажите количество паролей для генерации:'))
lenPw = int(input('Укажите длину одного пароля:'))
digOn = input('Включать ли цифры 0123456789? (д/н)')
if digOn == 'д':
    digOn = 1
else:
    digOn = 0
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (д/н)')
if ABCon == 'д':
    ABCon = 1
else:
    ABCon = 0
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (д/н)')
if abcOn == 'д':
    abcOn = 1
else:
    abcOn = 0
chOn = input('Включать ли символы !#$%&*+-=?@^_? (д/н)')
if chOn == 'д':
    chOn = 1
else:
    chOn = 0
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (д/н)')
if excOn == 'д':
    excOn = 1
else:
    excOn = 0
chars = digits * digOn + uppercase_letters * ABCon + lowercase_letters * abcOn + punctuation * chOn + excOn_letters * excOn
def generate_pasword(lenPw, chars):
    pwrd = ''
    for i in range(lenPw):
        pwrd = pwrd + chars[random.randint(0, len(chars))]
    return pwrd
for i in range(cntPw):
    print(generate_pasword(lenPw, chars))

