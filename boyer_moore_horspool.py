def boyer_moore_horspool(st, subst):
    indices = []  # искомый массив индексов
    unique = set()  # уникальные символы в подстроке
    offsets = {}  # словарь смещений

    # формирование словаря смещений
    # смещения для всех символов, кроме последнего
    for i in range(len(subst) - 2, -1, -1):  # итерации с предпоследнего символа
        if subst[i] not in unique:  # если символ еще не добавлен в словарь
            unique.add(subst[i])
            offsets[subst[i]] = len(subst) - i - 1  # m=6

    # смещение для последнего символа
    if subst[len(subst) - 1] not in unique:
        offsets[subst[len(subst) - 1]] = len(subst)

    # смещение для прочих символов
    offsets['*'] = len(subst)

    # поиск подстроки в строке
    k = len(subst) - 1

    while k < len(st):
        j = len(subst) - 1  # счетчик проверяемого символа в подстроке
        i = k  # счетчик проверяемого символа в строке
        while j >= 0 and st[i] == subst[j]:
            j -= 1
            i -= 1

        if j == len(subst) - 1:  # не совпал последний символ
            if offsets.get(st[i]) is None:
                off = offsets['*']
            else:
                off = offsets[st[i]]
        else:  # не совпал любой символ, кроме последнего
            off = offsets[subst[j]]

        if j == -1:  # образ найден
            indices.append(i + 1)

        k += off

    return indices
