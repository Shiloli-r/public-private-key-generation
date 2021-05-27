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
    primes = list(itertools.islice(gen_primes(), 20))
    print(primes, " ==> prime numbers")

    # getting two large prime numbers
    p = choice(primes[5:])
    q = choice(primes[5:])
    print("p = ", p, ", q = ", q)

    # the product of the two large prime numbers, i.e N
    N = p * q
    print("N = ", N)

    # Getting the phi of N
    phi_of_N = (p-1) * (q-1)
    print("Phi of N = ", phi_of_N)

    # getting the value of e
    e = generate_e(N)
    print("e = ", e)

    # getting the value of d
    d = generate_d(e, phi_of_N, 1000)
    print("d = ", d)

    return [[e, N], [d, N]]


# Function to check Co-prime
def are_co_prime(a, b):
    hcf = 1

    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            hcf = i

    return hcf == 1


def generate_e(N):
    half_of_N = N // 2
    primes = []
    co_primes = []
    print("Half of N = ", half_of_N)

    # Getting prime numbers less than half of N
    for num in range(0, half_of_N):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    print(primes, " ==> prime numbers less than half of N")
    for i in range(len(primes)):
        if are_co_prime(N, primes[i]):
            co_primes.append(primes[i])
    print(co_primes, " ==> co-primes")
    return choice(co_primes)  # return a random co-prime


def generate_d(e, phi_of_N, max):
    i = 0
    ds = []
    while i < max:
        i += 1
        if (i * e) % phi_of_N == 1:
            ds.append(i)
    print("possible values of d =", ds)
    return choice(ds)


def encrypt(e_no, e, N):
    return (e_no ** e) % N


def decrypt(d_no, d, N):
    return(d_no ** d) % N


def main():
    keys = generateKeys()
    publicKey = keys[0]
    privateKey = keys[1]
    print("PublicKey = ", publicKey)
    print("PrivateKey = ", privateKey)

    text = int(input("\n Enter a number that represents a letter e.g. 1 for A, 2 for B, etc: "))

    cipher = encrypt(text, publicKey[0], publicKey[1])
    print(text, " Encrypted to ", cipher)

    d = decrypt(cipher, privateKey[0], privateKey[1])
    print(cipher, "Decrypted to ", d)


if __name__ == '__main__':
    main()
