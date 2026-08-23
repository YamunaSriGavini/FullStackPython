# Adding numbers using lambda
add = lambda a, b: a + b
result = add(10, 20)
print(result)
#Square of a number
square = lambda num : num ** 2
print(square(3))
#Filter function (even numbers)
numbers = [1, 2, 3, 4, 6, 7]
result=list(filter(lambda x: x % 2 == 0,numbers))
print(result)
#login users
users = ["raju", "codegnan", "admin678", "user"]
result=list(filter(lambda user: len(user)>4, users))
print(result) 
#Map function(multiply number)
num = [1, 4, 3, 6]
result=list(map(lambda x: x * 2,num))
print(result)
#upper case
names = ["raju", "yamuna", "yagna", "mouni"]
result=list(map(lambda name: name.upper(), names))
print(result)
#reduce function
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda a, b: a + b, numbers)
print(result)

