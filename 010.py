# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# This takes ages but does the job. Need to find a faster way

primes = [2,3]
isPrime = True

for i in range(3,2000000):
    for prime in primes:
        if i % prime == 0:
            isPrime = False
            break
    if isPrime == True:
        primes.append(i)
    else:
        isPrime = True

total = 0
for prime in primes:
    total += prime
print("Answer:"+str(total))