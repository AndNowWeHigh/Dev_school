def find_nb(m):
    N = 1
    SUM = 0

    while m > SUM:
        SUM += N ** 3
        N += 1

    if SUM == m:
        return N - 1
    else:
        return -1

