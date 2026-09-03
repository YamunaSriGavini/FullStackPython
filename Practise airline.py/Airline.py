price =5000
seat=input("enter the seat type: ")
days = int(input("enter your booking days: "))
festival=input("enter festive: ")
age=int(input("enter your age: "))
if seat == "Business":
    price *= 1.4
elif seat == "Premium":
    price *= 1.2 
if days > 30:
    price *= price - price * 10/100
elif days < 7:
    price = price + price * 25/100
if festival == "True":
    price = price + price * 20/100
if age >= 60 :
    price = price - price * 15/100
print(price)