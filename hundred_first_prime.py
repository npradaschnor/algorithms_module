# Write an algorithm that prints the first 100 prime numbers.

# prime is only divisable by 1 and itself


def prime(num):
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            return False

    return True


def first_N_primes(n=100):
    count = 0
    num = 2
    while(count < n):
        if prime(num):
            count += 1
            print(num)
        num += 1


first_N_primes()
