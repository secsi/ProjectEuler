# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

primes = [2,3]
i = 5
count = 2
isPrime = True
nthPrime = 10001

while(1):
    for prime in primes:
        if i % prime == 0:
            #not prime
            isPrime = False
        if isPrime == False:
            break
    if isPrime == True:
        primes.append(i)
        count += 1
    else:
        isPrime = True
    if count == nthPrime:
        print(i)
        break
    i += 1
