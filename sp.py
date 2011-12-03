import sys

def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

primes = set()
prime_count = 0
i = 0

while prime_count <= 1001:
    if isprime(i):
        prime_count += 1
        primes.add(i)
    i += 1

print(sum(primes)-1)

sys.exit(0)
