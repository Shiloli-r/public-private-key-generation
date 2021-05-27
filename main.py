import itertools
from random import choice


def gen_primes():
    # Sieve of Eratosthenes
    # Code by David Eppstein, UC Irvine, 28 Feb 2002
    # http://code.activestate.com/recipes/117119/
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def generateKeys():
    primes = list(itertools.islice(gen_primes(), 10))
    print(primes, len(primes))

    # getting two large prime numbers
    p = choice(primes[0:])
    q = choice(primes[0:])
    print("p = ", p, ", q = ", q)

    # the product of the two large prime numbers, i.e N
    N = p * q
    print("N = ", N)

    # Getting the phi of N
    phi_of_N = (p-1) * (q-1)
    print("Phi of N = ", phi_of_N)


def main():
    generateKeys()


if __name__ == '__main__':
    main()
