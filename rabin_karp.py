d = 256  # мощность входного алфавита


def rabin_karp(st, subst, q=101):
    compares = 0
    M = len(subst)
    N = len(st)
    indices = []

    j = 0
    p = 0  # хэш для subst
    t = 0  # хэш для st
    h = 1

    for i in range(M - 1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(subst[i])) % q
        t = (d * t + ord(st[i])) % q

    for i in range(N - M + 1):
        compares += 1
        if p == t:
            for j in range(M):
                compares += 1
                if st[i + j] != subst[j]:
                    break
            j += 1
            compares += 1
            if j == M:
                indices.append(i)

        compares += 1
        if i < N - M:
            t = (d * (t - ord(st[i]) * h) + ord(st[i + M])) % q

            compares += 1
            if t < 0:
                t = t + q
    return indices, compares


if __name__ == '__main__':
    st = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    subst = "aaaaaaaaab"
    print(rabin_karp(st, subst))
