method = input('Вас приветствует программа: Шифр Цезаря. Вы хотите зашифровать или расшифровать текст? (1 - шифрование / 2 - дешифрование) \n')
while method != '1' and method != '2':
    method = input('Введите цифру 1 или 2 \n')
lang = input('На каком языке написан текст (1 - английский / 2 - русский) \n')
while lang != '1' and lang != '2':
    lang = input('Введите цифру 1 или 2 \n')
step = input('Укажите шаг сдвига(со сдвигом вправо) \n')
while step.isdigit() == False:
    step = input('Введите цифру \n')
step = int(step)
text = input('Какой текст нужно обработать сейчас? \n')
text1 = text
engBIG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
engSmall = 'abcdefghijklmnopqrstuvwxyz'
rusBIG = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
rusSmall = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

# if method == '1':
#     print(True)
#     if lang == '2':
#         print(True)
#         for i in range(len(text)):
#             print(text[i], rusBIG[(rusBIG.find(text[i]))])
#             if text[i] in rusBIG:
#                 text = text[:i] + rusBIG[(rusBIG.find(text[i]) + step) % 32] + text[i + 1:]
#             elif text[i] in rusSmall:
#                 text = text[:i] + rusSmall[(rusSmall.find(text[i]) + step) % 32] + text[i + 1:]

def caesar_cipher(method, lang, step, text):
    if method == '1':
        if lang == '1':
            for i in range(len(text)):
                if text[i] in engBIG:
                    text = text[:i] + engBIG[(engBIG.find(text[i]) + step) % 26] + text[i + 1:]
                elif text[i] in engSmall:
                    text = text[:i] + engSmall[(engSmall.find(text[i]) + step) % 26] + text[i + 1:]
        if lang == '2':
            for i in range(len(text)):
                if text[i] in rusBIG:
                    text = text[:i] + rusBIG[(rusBIG.find(text[i]) + step) % 32] + text[i + 1:]
                elif text[i] in rusSmall:
                    text = text[:i] + rusSmall[(rusSmall.find(text[i]) + step) % 32] + text[i + 1:]
    if method == '2':
        if lang == '1':
            for i in range(len(text)):
                if text[i] in engBIG:
                    text = text[:i] + engBIG[(engBIG.find(text[i]) - step) % 26] + text[i + 1:]
                elif text[i] in engSmall:
                    text = text[:i] + engSmall[(engSmall.find(text[i]) - step) % 26] + text[i + 1:]
        if lang == '2':
            for i in range(len(text)):
                if text[i] in rusBIG:
                    text = text[:i] + rusBIG[(rusBIG.find(text[i]) - step) % 32] + text[i + 1:]
                elif text[i] in rusSmall:
                    text = text[:i] + rusSmall[(rusSmall.find(text[i]) - step) % 32] + text[i + 1:]
    return text
print(caesar_cipher(method, lang, step, text))
if method == '2':
    rep = input('Если вас не устраивает результат расшифровки, то программа может вывести варианты с другими шагами (д - вывести все возможные варианты) \n')
    text = text1
    step = 1
    tryresult = 1
    if rep == 'д':
        if lang == '1':
            while tryresult != 26:
                for i in range(len(text)):
                    if text[i] in engBIG:
                        text = text[:i] + engBIG[(engBIG.find(text[i]) - step) % 26] + text[i + 1:]
                    elif text[i] in engSmall:
                        text = text[:i] + engSmall[(engSmall.find(text[i]) - step) % 26] + text[i + 1:]
                print(text, 'Смещение на:', tryresult)
                tryresult += 1
        if lang == '2':
            while tryresult != 32:
                for i in range(len(text)):
                    if text[i] in rusBIG:
                        text = text[:i] + rusBIG[(rusBIG.find(text[i]) - step) % 32] + text[i + 1:]
                    elif text[i] in rusSmall:
                        text = text[:i] + rusSmall[(rusSmall.find(text[i]) - step) % 32] + text[i + 1:]
                print(text, 'Смещение на:', tryresult)
                tryresult += 1