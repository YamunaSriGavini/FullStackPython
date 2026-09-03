#Polymorphism
class Dog:
    def speak(self):
        print("Bark")
class Cat:
    def speak(self):
        print("Meow")
for animal in (Dog(), Cat()):
    animal.speak()
#Operator Overloading
class Book:
    def __init__(self, pages):
        self.pages = pages
    def __add__(self, other):
        return self.pages + other.pages
b1 = Book(100)
b2 = Book(200)
print(b1 + b2)
#Method overloading
class Greet:
    def hello(self, name=None):
        if name:
            print("Hello", name)
        else:
            print("Hello")
g = Greet()
g.hello()          
g.hello("Jhansi")
#Method overridding
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
a = Animal()
d = Dog()
a.speak()  
d.speak() 
#method overloading using operators
class Student:
    def __init__(self, marks):
        self.marks = marks
    def __add__(self, other):
        return self.marks + other.marks
s1 = Student(50)
s2 = Student(40)
print(s1 + s2)



