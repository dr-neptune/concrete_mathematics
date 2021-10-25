def euclids_algo(m: int, n: int) -> int:
    if m < 0:
        return 0
    if m == 0:
        return n
    else:
        new_m = n % m
        return euclids_algo(new_m, m)


euclids_algo(12, 18)
euclids_algo(226, 430)
