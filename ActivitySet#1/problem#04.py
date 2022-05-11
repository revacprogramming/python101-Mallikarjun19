# Conditional Execution

hrs = float(input("Enter hours: "))
rate=float(input("enter rate: "))
if(hrs>40):
  extra_pay=(hrs-40)*(rate*1.5)
  pay=(40*rate)+extra_pay
else:
  pay=hrs*rate
print("pay=",pay)  
  
  