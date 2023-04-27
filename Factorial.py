print("Print the integer to get factorial")
n=int(input())
fact=1
if n >0:
    for  n in range (1,n+1):
        fact=fact*n
        n=n-1
    print(fact)
else:
    print("Please enter positive integer")
