#nested if else statements 
num=int(input("enter"))
if num>0:
    print("positive number")
    if num%2==0:
        print("even")
    else:
        print("Odd")    
else:
    print("negative")                