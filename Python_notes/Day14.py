#Right angle triangle
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

  #Number Triangle
num=1
for i in range(1, 5):
    for j in range(i):
        print(num, end="")
        num = num + 1
    print()
  # Pyramid Pattern
n = 4
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
#Decreasing pattern
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
#Inverted Triangle
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
#same number in each row
for i in range(1, 5):
    for j in range(i):
        print(i, end="")
    print()
#Hollow square
n = 4
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


