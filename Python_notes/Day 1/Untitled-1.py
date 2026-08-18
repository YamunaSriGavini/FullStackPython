Units = int(input("enter the number of units: "))
age = int(input("enter the age: "))
if 0<unit<100:
    rate=1.5
elif 101<unit<200:
    rate=2.5
elif 201<unit<500:
    rate=4
else:
    rate=6
bill=units*rate
if age>60:
    subsidy=bill*0.10
    bill=bill-subsidy
if Units>800
    surcharge=bill*0.05
    bill=bill+surcharge
print(bill)