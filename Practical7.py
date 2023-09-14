

# P7 1.Write a Python function to find the maximum and minimum numbers from a sequence ofnumbers

def find_max_min(numbers):   
    min = max = numbers[0]

    for number in numbers:
        if number < min:
            min = number
        elif number > max:
            max = number

    return (min, max)

numbers = []
n=int(input("Enter the the upper limit:"))
print("Enter the numbers:")
for x in range(0,n):
    k=input()
    numbers.append(k)
    
min, max = find_max_min(numbers)
print("Minimum number:", min)
print("Maximum number:", max)


#*****************************************************************************************************************************

# P7 2. Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.

def sum_cubes(n):
 n -= 1
 total = 0
 while n > 0:
   total += n * n * n
   n -= 1
 return total

n=int(input("Enter a positive number:"))
print("Sum of cubes smaller than the specified number: ",sum_cubes(n))


#*****************************************************************************************************************************

# p7 q3. Write a Python function to print 1 to n using recursion. (Note: Do not use loop)
# python3 program to print 1 to n using recursion

def printNumber(n):
  if n > 0:
    printNumber(n - 1)
    # print n
    print(n, end = ' ')

n = int(input("Enter the limit:"))
printNumber(n)

#*****************************************************************************************************************************

# P7 4. Write a recursive function to print Fibonacci series upto n terms

def fib_no(n):
   if n <= 1:
       return n
   else:
       return(fib_no(n-1) + fib_no(n-2))

nterms = int(input("Enter the limit(+ve):"))

for i in range(nterms):
       print(fib_no(i))


#*****************************************************************************************************************************

# P7 5. Write a lambda function to find volume of cone.

vol_cone = lambda r, h: (1/3) * 3.14 * r**2 * h

r=float(input("Enter the radius:"))
h=float(input("Enter the height:"))
print("Volume of cone is:",vol_cone(r,h))



#*****************************************************************************************************************************

# P7 6. Write a lambda function which gives tuple of max and min from a list.

max_min = lambda lst: (max(lst), min(lst))

lst=[]
n=int(input("Enter the size of the list:"))
print("Enter the elements:")
for i in range(0, n):
    ele = int(input())
    lst.append(ele) 
 
print(max_min(lst))



#*****************************************************************************************************************************

# P7 7 . Write functions to explain mentioned concepts:
# a. Keyword argument.
# b.Default argument 
# c. Variable length argument


# Keyword argument
def greet(name, message):
    print(f"{message}, {name}!")
greet(name="Shashank", message="Good morning")

# Default argument
def multiply(a, b=1):
    return a * b
print(multiply(9))
print(multiply(9, 2)) 

# Variable length argument
def print_values(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_values("apple", "Kiwi", "Mango", color="green", taste="sweet")



