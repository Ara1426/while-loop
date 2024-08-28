x=int(input("write a num"))

sum=0
temp=x

while temp>0:
    reminder=temp%10
    sum=sum+(reminder**3)
    temp=temp//10

if x==sum:
    print("armstong number")
else:
    print("it is not an armstong number")