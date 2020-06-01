#
# Highly divisible triangular number
# https://projecteuler.net/problem=12

# Brute force approach:
# Tn = sum(i), i=1 to n
# d is factor of Tn if Tn % d is zero
# Iterating on all possible values of n and d by brute force will take a night to solve this problem

# Approach based on prime factors decomposition:
# Based on https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
# In number theory, the fundamental theorem of arithmetic, also called the unique factorization theorem or
# the unique-prime-factorization theorem, states that every integer greater than 1 either is a prime number itself
# or can be represented as the product of prime numbers and that, moreover, this representation is unique,
# up to (except for) the order of the factors
# e.g. 500 = 2 * 2 * 5 * 5 * 5 = 2^2 * 5^3

# The divisors of a number will be all the combinations of the prime factors up to their multiplicity
# e.g. divisors of 500 are: 2^0; 2^1, 2^2, 5^0, 5^1, 5^2, 5^3  =  1,2,4,5,25,125,500

import itertools


def nbr_of_prime_factors(n):
    """
    Return a dictionary where the key is a prime factor and the value the number of occurences
    :param n:
    :return:
    """

    # get the prime factors of n in a list 'pf'
    i = 2
    pf = []
    while i * i <= n:
        if n % i == 0:
            n = int(n/i)
            pf.append(i)
        else:
            i += 1

    if n > 1:
        pf.append(n)

    # get the number of occurrences for each prime factor
    npf = {}
    for p in pf:
        if p in npf:
            npf[p] += 1
        else:
            npf[p] = 1
    return npf


def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result


def divisors(n):
    div = []
    # get the prime factors & multiplicity
    npf = nbr_of_prime_factors(n)

    # get the list of powers for each prime factor
    powers = [
        [factor ** i for i in range(count + 1)]
        for factor, count in npf.items()
    ]

    # get the combinations
    for p in itertools.product(*powers):
        div.append(prod(p))

    return div


def main():
    """

    :return:
    """
    n = 2
    target = 500

    while True:
        d = []
        # calculate the triangle number
        t = sum(range(1, n+1))
        # d = [x for x in range(1, int(t/2)+1) if t % x == 0]
        d = divisors(t)
        count = len(d)

        if count >= target:
            print(f'First triangle number with more than {target} divisors is {t}')
            print(f'T{n} = {t} with {count} divisors = {d}')
            exit(0)
        n += 1


if __name__ == "__main__":
    main()
