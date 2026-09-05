salary=int(input())
performance=int(input())
experience=int(input())
attendance=int(input())
rating=int(input())
if rating==5:
    salary+=salary*0.25
elif rating==4:
    salary+=salary*0.15
elif rating==3:
   salary+=salary*0.1
else :
    print("No performance bonus")
if experience > 10:
    salary+=salary*0.1
elif experience >= 5:
    salary+=salary*0.05
if attendance >= 95:
    salary+=salary* 5000
elif attendance >= 85:
    salary+=salary*2000
print(salary)