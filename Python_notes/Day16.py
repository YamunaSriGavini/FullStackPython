# scope
def student():
    name = "Teja"
    print(name)
student()
#Global keyword
count = 10
def update():
    global count
    count = 20
update()
print(count)
#LEGB rule
x = 100
def outer():
    x = 50
    def inner():
        x = 20
        print(x)
    inner()
outer()
#Pass by Reference
def update(items):
    items.append("Laptop")
cart = ["Mobile", "Watch"]
update(cart)
print(cart)
#Pass by value
def update(number):
    number = 100
    print("Inside Function:", number)
value = 50
update(value)
print("Outside Function:", value)