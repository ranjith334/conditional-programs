n=int(input("enter"))
t=n
sum=0
while n>0:
    d=n%10
    sum+=d
    n//=10
if t%sum==0:
    print("the given number is niven")    
else:
    print("not an nivens nmuber")