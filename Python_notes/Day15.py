#Function
#Call a function
def Greet():
    print("Welcome to Functions")
Greet()
#Positional Arguments
def Greet(name, age):
    print(f"My name is {name} and age is {age}")
Greet("Raju", 23)
#Using Retrun
def Add(a, b):
    return a + b

result = Add(10, 20)
print(result)
#Keyword Arguments
def create_student(name, age, course):
    pass
create_student(
    name="Ravi",
    age=22,
    course="Python"
)
#Default parameters
def CountryDetails(country="India"):
    print("My country is:", country)
CountryDetails("USA")
CountryDetails()
#Using *args
def ItemBillCal(*items):
    print("All items:", items)
    print("Total:", sum(items))
ItemBillCal(100, 200, 300, 400)
# Using **Kargus
def create_profile(**details):
    print(details)
create_profile(
    name="Jani",
    age=21,
    city="Hyderabad",
    course="Python"
)
#Student result combine parameters
def calculate_total(m1, m2, m3):
    return m1 + m2 + m3
total = calculate_total(80, 75, 90)
print("Total:", total)
# login function
def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"
    else:
        return "Invalid username or password"
result = login("admin", "1234")
print(result)


