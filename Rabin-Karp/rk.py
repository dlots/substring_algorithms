d = 256  # мощность входного алфавита


def rk_search(subst, st, q):
    M = len(subst)
    N = len(st)
    indices = []

    i = 0
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
        if p == t:
            for j in range(M):
                if st[i + j] != subst[j]:
                    break
            j += 1
            if j == M:
                indices.append(i)

        if i < N - M:
            t = (d * (t - ord(st[i]) * h) + ord(st[i + M])) % q

            if t < 0:
                t = t + q
    return indices


st = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
subst = "aaaaaaaaab"

q = 101  #простое число

rk_search(subst, st, q)