# primes' generator

from math import sqrt, modf

def prime_generator(n):
    primes = [2]
    while len(primes) <= n:
        yield primes[-1]
        num = primes[-1] + 1
        while num:
            frac = 0
            for prime in primes:
                frac, whole = modf(num / prime)
                if not frac:
                    num += 1
                    break
            if frac:
                primes.append(num)
                break


# generator of primes
def primes1(n_max):

    p, num, cnt = list(), 2, 0

    while cnt < n_max:

        should_add = True

        for prime in p:
            if num % prime == 0:
                should_add = False
                break

            # the first way - checking squares each time
            if prime * prime > num:
                break

        if should_add:
            p.append(num)
            cnt += 1
            yield num

        num += 1

# sqrt(num)
def primes2(n_max):

    p, num, cnt = list(), 2, 0

    while cnt < n_max:

        # recomputing square root - time consuming operation
        should_add, sqrt_num = True, int(sqrt(num))

        for prime in p:

            if num % prime == 0:
                should_add = False
                break

            if prime > sqrt_num:
                break

        if should_add:
            p.append(num)
            cnt += 1
            yield num

        num += 1


def primes3(n_max):
    p, num, cnt = list(), 2, 0
    next_square, sqrt_num = 4, 1

    while cnt < n_max:

        should_add = True

        for prime in p:

            if num % prime == 0:
                should_add = False
                break

            if prime > sqrt_num:
                break


        if should_add:
            p.append(num)
            cnt += 1
            yield num

        if num == next_square:
            next_square += 2 * sqrt_num + 1
            sqrt_num += 1

        num += 1


# no should_add boolean
def primes4(n_max):
    p, num, cnt = [2], 2, 1
    next_square, sqrt_num = 4, 1

    yield num

    while cnt < n_max:
        num += 1

        for prime in p:
            if num % prime == 0:
                break

            if prime > sqrt_num:
                p.append(num)
                cnt += 1
                yield num
                break

        # TODO: analyze situation when num is a square - may it be optimized?
        if num == next_square:
            next_square += 2 * sqrt_num + 1
            sqrt_num += 1


primes = primes4

# factor function
def factor(n):
    result, current = list(), n

    for prime in primes(n):
        if prime > current:
            break

        counter = 0
        while current % prime == 0:
            current //= prime
            counter += 1

        if counter > 0:
            result.append((prime, counter))

    return result
