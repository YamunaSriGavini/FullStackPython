# reverse the number
n = int(input("Enter n value: "))
original = n
rev = 0
while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10
print(f"The reverse of {original} is:", rev)

#Palindrome using string
n = 121

s = str(n)

if s == s[::-1]:
    print("Number is palindrome")
else:
    print("Number is not palindrome")

# Count even digits in a number
n = 123456
s = str(n)
c = 0
for i in s:
    if int(i) % 2 == 0:
        c = c + 1
print("Count of even digits:", c)
#Factors of a number
n = int(input("Enter number: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
# Armstrong number
n = int(input("Enter number: "))
original = n
total = 0
while n > 0:
    r = n % 10
    total = total + r ** 3
    n = n // 10
if original == total:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
