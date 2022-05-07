# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
highest = 0

for a in range(100,999):
    for b in range(100,999):
        val = a*b
        rev = str(val)[::-1]
        if rev == str(val):
            if val > highest: highest = val
print(highest)