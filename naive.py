def naive(text, st):
    mas = []
    i = 0
    j = 0
    compare = 0

    while i < len(text):
        compare += 1
        if text[i] == st[j]:

            if j == len(st) - 1:
                mas.append(i + 1 - len(st))
                i = i - j + 1
                j = 0

            else:
                i += 1
                j += 1

        elif j != 0:
            i = i - j + 1
            j = 0
        else:
            # если остаток текста >= длине слова и первый символ не совпадает
            if i >= len(text) - len(st) and text[i] != st[0]:
                return mas, compare
            i += 1
    return mas, compare
