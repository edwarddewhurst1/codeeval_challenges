import sys

def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

primes = set()

for i in range(1, 1000):
    if isprime(i):
        primes.add(i)

result = set()

for i in primes:
    si = str(i)
    if si == si[::-1]:
        result.add(i)



print(max(result))
        
sys.exit(0)
