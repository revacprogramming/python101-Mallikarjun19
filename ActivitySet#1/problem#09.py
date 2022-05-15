# Lists

filename = "dataset/romeo.txt"
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    x=line.split()
    for element in x:
        if element in lst:
        	continue
        else:
            lst.append(element)
            
lst.sort()            
print(line.rstrip())