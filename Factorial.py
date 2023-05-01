print('Enter the positive integer to get factorial')
n=int(input())
fact=1
if n >0:
    for n in range (1,n+1):
        fact*=n
    print(fact)
else:
    raise ValueError('You must enter a non-negative integer')
#using recusion
# Factorial of a number using recursion

print('Enter the positive integer to get factorial')
n=int(input())
if n < 0:
    raise ValueError('You must enter a non-negative 
else:
    def fact(n):
        if n == 1:
            return n
        else:
            return n*fact(n-1)

