base=10000
age=int(input("enter the age: "))
health_score=int(input("enter the score: "))
vehicle_type=input("enter the vehicle: ")
if age < 25:
    base *= 1.2
elif age > 50:
    base *= 1.15
if health_score >=80:
    base *= 0.9
elif health_score < 60:
    base *= 1.2
if vehicle_type == "Sports Car":
    base *= 1.3
elif vehicle_type == "SUV":
    base *= 1.15
elif vehicle_type == "Sedan":
    base == base
print(round(base,2))