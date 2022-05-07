# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

# numbers only needed up to square root
num = 600851475143
root = round(sqrt(600851475143))
primes = [2,3]
isPrime = True
highest = 0

# get primes up to "root"
for i in range(3,root):
    for prime in primes:
        if i % prime == 0:
            #not prime
            isPrime = False
        if isPrime == False: break
    if isPrime == True:
        primes.append(i)
        if num % i == 0 and num > highest:
            highest = i
            print(highest)
    else:
        isPrime = True
