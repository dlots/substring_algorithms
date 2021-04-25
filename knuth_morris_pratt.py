def prefix(st):
    output = [0]

    for i in range(1, len(st)):
        j = output[i - 1]

        while j > 0 and st[j] != st[i]:
            j = output[j - 1]

        if st[j] == st[i]:
            j = j + 1

        output.append(j)
    return output


def knuth_morris_pratt(text, st):
    compare = 0
    pref = prefix(st)
    mas = []
    i = 0
    j = 0

    while i < len(text):
        compare += 1
        if text[i] == st[j]:
            if j == len(st) - 1:
                mas.append(i - len(st) + 1)
                if pref[j] != 0:
                    i = i - j
                j = 0
            else:
                j += 1
            i += 1

        elif j:
            j = pref[j - 1]
        else:
            # если остаток текста >= длине слова и первый символ не совпадает
            if i >= len(text) - len(st) and text[i] != st[0]:
                return mas, compare
            i += 1
    return mas, compare
