#
# Highly divisible triangular number
# https://projecteuler.net/problem=12

# Tn = sum(i), i=1 to n
# d is factor of Tn if Tn/k is integer


# Brute force approach:
# Tn = sum(i), i=1 to n
# d is factor of Tn if Tn % d is zero
# Iterating on all possible values of n and d by brute force will take a night to solve this problem


target = 500


def main():
    """

    :return:
    """
    n = 2

    while True:
        d = []

        t = sum(range(1, n+1))
        d = [x for x in range(1, int(t/2)+1) if t % x == 0]
        d.append(t)
        print(f'T{n} = {t} with {len(d)} divisors = {d}')
        if len(d) >= target:
            print(f'First triangle with more than {target} divisors is {t}')
            exit(0)


        n += 1


if __name__ == "__main__":
    main()
