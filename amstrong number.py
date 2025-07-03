n=int(input("enter the value"))
temp=n
length=len(str(n))
sum=0
while temp>0:
    d=temp%10
    sum +=d**length
    temp//=10
if sum==n:
    print("amstrong number")    
else:
    print("not an amstrog number")    
