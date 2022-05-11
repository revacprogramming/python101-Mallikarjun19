# Functions
def computepay(hrs,rate):
  if(hrs>40):
    extra=(hrs-40)*(rate*1.5)
    pay=(40*rate)+extra
  else:
    pay=hrs*rate
  return pay  
  
h= float(input("Enter hours:"))
r= float(input("Enter rate:"))
p = computepay(h,r)
print("Pay", p)
