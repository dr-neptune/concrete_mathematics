from typing import List, Tuple
from pprint import pprint
from random import randint
from math import floor, log

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

def sieve_of_eratosthenes(n: int) -> List[int]:
    if n <= 2:
        return []
    sieve = [True] * (n + 1)
    for x in range(3, int(n**0.5) + 1, 2):
        for y in range(3, (n // x) + 1, 2):
            sieve[(x * y)] = False
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

sieve_of_eratosthenes(10)


def miller_rabin(n: int, accuracy: int = 100):
    def decomp(n: int) -> Tuple[int, int]:
        exp_of_two = 0
        while n % 2 == 0:
            n = int(n / 2)
            exp_of_two += 1
        return exp_of_two, n

    def witness(possible: int, p: int, exp: int, rem: int) -> bool:
        possible = pow(possible, rem, p)
        if possible == 1 or possible == p - 1:
            return False
        for _ in range(exp):
            if not p == floor(p):
                print(p)
            possible = pow(possible, 2, p)
            if possible == p - 1:
                return False
        return True

    if n == 2 or n == 3:
        return True
    elif n < 2:
        return False
    else:
        exp, rem = decomp(n - 1)
        for _ in range(accuracy):
            possible = randint(2, n - 2)
            if witness(possible, n, exp, rem):
                return False
        return True


miller_rabin(3263443)

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

prime_factors(10650056950807)

def check_euclid_numbers(n):
    """
    Checks each Euclid Number for primality
    If prime, print, else factor and mark
    """
    nums = euclid_numbers(n)
    for k, v in nums.items():
        if miller_rabin(v):
            print(f"Prime Euclid Number:\t{k}\nNumber:\t{v}\n")
        else:
            # not prime
            factors = "*".join([str(i) for i in prime_factors(v)])
            print(f"Non-Prime Euclid Number:\t{k}\n" \
                  f"Number:\t{v}\n" \
                  f"Factorization:\t{factors}\n")

check_euclid_numbers(7)

def check_mersenne_primes(n_primes):
    """For the first n_primes primes, return the set of mersenne primes"""
    primes = set(sieve_of_eratosthenes(n_primes))
    # get mersenne numbers
    mersenne = []
    for i in range(2, int(log(n_primes + 1, 2)) + 1):
        mersenne.append(2**i - 1)
    return sorted(list(primes.intersection(set(mersenne))))

check_mersenne_primes(10000000)

# check sieve plots
import matplotlib.pyplot as plt

y = sieve_of_eratosthenes(1000000)
x = list(range(1, len(y) + 1))
plt.plot(x, y)
plt.show()
