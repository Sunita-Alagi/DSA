print('Enter the positive integer to get factorial')
n=int(input())
fact=1
if n >0:
    for n in range (1,n+1):
        fact*=n
    print(fact)
else:
    raise ValueError('You must enter a non-negative integer')
