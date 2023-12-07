# Getting Started Activity

print("Hello, World!")

""" Basics: Activity 1
Write a Python program to print the result of the following operations.

 
a. -5 + 8 * 6
 expected output 43 
 
"""
a = -5
b = 8
c = 6
print(a + b * c)

""" b. (55+9) % 9 
 expected output 1 """
a = 55
b = 9
print((a + b) % b)


""" c. 20 + -3*5 / 8 
 expected output 18.125 """

a = 20
b = -3
c = 5
d = 8
print(a + b * c / d)

""" d. 5 + 15 / 3 * 2 - 8 % 3
    expected output 13.0 """
a = 5
b = 15
c = 3
d = 2
e = 8
print(a + b / c * d - e % c)

""" 
    Basics - Activity 2 
    Write a Python program to divide two numbers, using the input from the user, 
    and print the result on the screen.
    Expected Output :
    Input the first number: 6
    Input the second number: 2
    The division of the first number and the second number is: 3
"""

num1 = int(input("Input the first number: "))
num2 = int(input("Input the second number: "))
num3 = int(num1/num2)
print("The division of the first number and the second number is: ", num3)

""" 
    Control Statements - Activity 1 
Write a Python program that accepts three numbers and prints "All numbers are equal" 
if all three numbers are equal, 
"All numbers are different" if all three numbers are different and 
"Neither all are equal or different" otherwise.
"""

num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))
num3 = int(input("Input third number: "))

if num1 == num2 and num1 == num3:  # compare if all numbers are same
    print("All numbers are equal")
elif num1 != num2 and num1 != num3 and num2 != num3:  # compare to see if all numbers are different
    print("All numbers are different")
else:
    print("Neither all are equal or different")   # numbers are neither all same or different

"""
    Control Statements - Activity 2
Write a Python program that accepts three numbers from the user and prints 
"Increasing order" if the numbers are in the increasing order,
 "Decreasing order" if the numbers are in the decreasing order, 
 and "Neither increasing or decreasing order" otherwise.

"""

a = int(input('Input first number: '))
b = int(input('Input second number: '))
c = int(input('Input third number: '))

if a < b < c:  # compare if numbers are in increasing order
    print('Increasing order')
elif a > b > c:  # compare to see if number are in decreasing order
    print('Decreasing order')
else:
    print('Neither increasing or decreasing order')


""" 
    Python Loops - Activity 1
    Write a Python program to get the Fibonacci series between 0 to 50. 
"""

x,i = 0,1

print(x)

while i < 50:
  print(i)
  if i == 50:
    break
  x,i = i,x+i

"""
    Python Loops - Activity 2
    Write a Python program to create the multiplication table (from 1 to 10) of a number.
"""

a = int(input('Input a number: '))
for i in range(1, 11):
    print(a, "x", i, "=", i * a)

"""
    Python Collections - Activity 1
    Write a Python program to sum values of a list.
    
"""

mylist = [1,2,3,4,5,6,7,8,9,10]
print(sum(mylist))

"""
    Python Collections - Activity 2
    Write a Python program to calculate the average value of a list elements.
"""

mylist = [20, 30, 25, 35, -16, 60, -100]
average = sum(mylist)/len(mylist)
print(f"{average:0,.1f}")

""" 
  Python Collections - Activity 3
  Write a Python program to find the maximum and minimum value of a list.
"""

mylist = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]
print("Original List: ", mylist)
print("Maximum value for the above list = ", max(mylist))
print("Minimum value for the above list = ", min(mylist))

"""
    Python Functions - Activity 1
    Write 2 Python functions to: 
        show the list content. 
        find the max value in the list.
"""
def list_Function(myList):
    print("The content of the list is: ", myList)
def max_function(maxList):
    print("The max value in the list: ", max(maxList))


list_Function([10, 2, 3, 4, 7])
max_function([10, 2, 3, 4, 7])

"""
    Python Functions - Activity 2 
    Write a Python function to calculate the factorial of a number 
    (a non-negative integer n ). The function accepts the number as an argument.

"""
def my_fact(x):
	if x == 0:
		return 1
	else:
		return x * my_fact(x-1)

x=int(input("Please input a number to calculate the factior: "))
print(my_fact(x))


"""

    Python Functions - Activity 3
    Write a Python function that takes a number as a parameter and 
    check the number is prime or not. 

"""
def prime_function(n):

# check if given number is greater than 1
  if n > 1:
  	# Iterate from 2 to n / 2
  	for i in range(2, int(n/2)+1):
  		# If num is divisible by any number between
  		# 2 and n / 2, it is not prime
  		if (n % i) == 0:
  			print(n, "is not a prime number")
  			break
  	else:
  		print(n, "is a prime number")
  else:
  	print(n, "is not a prime number")

n=int(input("Please input a number to check if prime: "))
print(prime_function(n))