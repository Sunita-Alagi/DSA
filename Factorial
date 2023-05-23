# Factorial of a number using Iteration
print('Enter the positive integer to get factorial')
num=int(input())
fact=1
if n >0:
    for num in range (1,num+1):
        fact*=num
    print('The Factorial of',num,'is' fact)
else:
    raise ValueError('You must enter a non-negative integer')

# Factorial of a number using Recursion 
print('Enter the positive integer to get factorial')
num=int(input())
def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

# Check if the number is negative
if num < 0:
   print('Sorry, factorial does not exist for negative numbers')
elif num == 0:
   print('The factorial of 0 is 1')
else:
   print('The factorial of', num, 'is', factorial(num))
