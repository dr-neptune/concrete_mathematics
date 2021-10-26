from pprint import pprint

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

def euclid_numbers(n):
    vals = {0: 1}
    i = 1
    while i <= n:
        j = 0
        val = 1
        while j < i:
            val *= vals[j]
            j += 1
        print("val:\t", val + 1)
        vals[i] = val + 1
        i += 1
    return vals

pprint(euclid_numbers(8))
pprint(euclid_numbers(10))
