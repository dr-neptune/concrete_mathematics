from typing import List, Tuple
from pprint import pprint
from random import randint
from math import floor, log, factorial

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


def ruler_function(n, p, exp=1,sum=0):
    fl = floor(n / p**exp)
    if fl > 0:
        print(f"n: {n} p: {p} fl: {fl}")
        sum += fl
        exp += 1
        return ruler_function(n, p, exp, sum)
    else:
        return sum

ruler_function(10, 2)
ruler_function(100, 2)
ruler_function(100, 3)

def stern_brocot_fraction(m, n):
    if m == n:
        return
    if m < n:
        print('L')
        return stern_brocot_fraction(m, n - m)
    else:
        print('R')
        return stern_brocot_fraction(m - n, n)

stern_brocot_fraction(5, 7)   # LRRL
stern_brocot_fraction(1, 700) # all L
stern_brocot_fraction(12, 1)  # all R

# some of the examples for deducing fractions in the book
stern_brocot_fraction(299, 110)
stern_brocot_fraction(878, 323)

def stern_brocot_infinite_representation_truncated(alpha, times=100):
    if times == 0:
        return
    if alpha < 1:
        print('L')
        stern_brocot_infinite_representation_truncated(alpha / (1 - alpha), times - 1)
    else:
        print('R')
        stern_brocot_infinite_representation_truncated(alpha - 1, times - 1)

stern_brocot_infinite_representation_truncated(2.71828182845904523536028747135266249775724709369995)
# 1000 hits maximum recursion depth for python :/
stern_brocot_infinite_representation_truncated(1) # RLLLL...


# problem 8
for x in range(1, 10000):
    for y in range(1, 10000):
        lhs = 10 * x + y
        rhs = x % 3
        rhs2 = y % 5
        rhs = int(''.join([str(rhs), str(rhs2)]))
        if lhs == rhs:
            print(f"Found a solution: {lhs} == {rhs}")
