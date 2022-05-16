# Files

filename = "dataset/mbox-short.txt"
fname=input("Enter the file name: ")
fname2=open(fname)
l=[]
for line in fname2:
    if line.startswith("X-DSPAM-Confidence:"):
        pos=line.find(":")
        x=line[pos+3:]
        y=float(x)
        l.append(y)
    else:
        continue
        
size=len(l)
total=0
for i in range(0,size):
    total=total+l[i]
avg=total/size
print("Average spam confidence: ",avg)