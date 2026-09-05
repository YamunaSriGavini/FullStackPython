creditScore=int(input())
income=int(input())
liabilities=int(input())
'''if credit score =>750:
    print("Eligible")
elif credit score 650<= credit score<=749:
    print("Conditional Eligibility")
else:
    print("Rejected")
if income >= 50000:
    print("Eligible")
else:
    print("Not Eligible")
if credit score and income and liabilities:
    print("Approved")
elif credit score or income and liabilities:
    print("Approved with Conditions")
else:
    print("Rejected")'''
if creditScore >= 750 and income >= 50000 and liabilities <= 20000:
    print("Approved")
elif 650<= creditScore <= 749 and income < 50000 and liabilities > 20000:
    print("Approved with Conditions")
else:
    print("Rejected")
