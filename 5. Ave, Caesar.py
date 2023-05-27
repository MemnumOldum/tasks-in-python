# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
# Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными.


text = input('Эта программа зашифровывает английский текст шифром Цезаря с смещением вправо. '
             'Каждое слово шифруется со сдвигом равным длине этого слова. Введите текст на английском языке: \n')
engBIG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
engSmall = 'abcdefghijklmnopqrstuvwxyz'
list1 = text.split()
list2 = []
list3 = []

def newtext_return(list1):
    for i in range(len(list1)):  # Считает шаг смещения для каждого слова, и сохраняет в список list2
        s = list1[i]
        word_len = 0
        for j in range(len(s)):
            if s[j] in engBIG or s[j] in engSmall:
                word_len += 1
        list2.append(word_len)
    for i in range(len(list1)):  # Возвращает изменённый текст с нужным смещением в виде списка list3
        s = ''
        for j in range(len(list1[i])):
            if list1[i][j] in engBIG:
                s = s + engBIG[(engBIG.find(list1[i][j]) + int(list2[i])) % 26]
            elif list1[i][j] in engSmall:
                s = s + engSmall[(engSmall.find(list1[i][j]) + int(list2[i])) % 26]
            else:
                s = s + list1[i][j]
        list3.append(s)
    return list3
print(*newtext_return(list1))
