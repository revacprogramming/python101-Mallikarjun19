# Loops & Iterators

l=[]

while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    try:
        num = int(inp)
    except:
        print ("Invalid input")
        continue
    l.append(num)    
    

l.sort()
a=len(l)
print ("Maximum is",l[a-1])  
print ("Minimum is",l[0])
    