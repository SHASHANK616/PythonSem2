# 1. Declare these variables (x, y and z) as integers. Assign a value of 9 to x, Assign a value of 7 to y, 
#    perform addition, multiplication, division and subtraction on these two variables and Print out the result.

#declaring the value of x,y and x
x=9
y=7
z=4

#formula
add=x+y
mul=x*y
sub=x-y

# printing the result
print("Addition of x and y = ",add)
print("Multiplication of x and y = ",mul)
print("Subtraction of x and y = ",sub)

#**********************************************************************************************************************************

#P2 Q2 Write a Program where the radius is taken as input to compute the area of a circle

# taking radius input from user
radius=float(input("Enter the value of Radius:"))
pi=3.14

#Formula
area=pi*radius*radius

#printing the result
print("Area of circle having radius ",radius,"=", area)

#******************************************************************************************************************************

# q3. Write a Python program to solve (x+y)*(x+y)Test data : x = 4 , y = 3 Expected output: 49


#Taking user input
x = float(input("Enter the value of x:")) 
y = float(input("Enter the value of Y:"))

#formula
solve =(x+y)*(x+y)
print(solve)

#********************************************************************************************************************************

# 4. Write a program to compute the length of the hypotenuse (c) of a right triangle using Pythagoras theorem.

#taking the values of perpendicular and base from user
p=float(input("Enter the value of Perpendicular:"))
b=float(input("Enter the value of base:"))

#formula
c=((p**2)+(b**2))**0.5

# Printing the result
print("The length of the hypotenuse is: ",c)

#**********************************************************************************************************************************

# 5. Write a program to find simple interest.

# Taking user input
p=float(input("Enter the principle amount:"))
t=float(input("Enter the time duration:"))
r=float(input("Enter the interest rate:"))

#formula
si=(p*r*t)/100

#printing the result
print("Simple interest=",si)

#***********************************************************************************************************************************

#  Q6.Write a program to find area of triangle when length of sides are given.


a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  
  
# calculate the semi perimeter  
s = (a + b + c) / 2  
  
# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  

print('The area of the triangle is %0.2f' %area) 

#***************************************************************************************************************************************

# 7. Write a program to convert given seconds into hours, minutes and remaining seconds.

seconds=int(input("Enter the seconds"))
seconds = seconds % (24 * 3600)
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print(hour,":",minutes,":",seconds)

#**********************************************************************************************************************************

# 8. Write a program to swap two numbers without taking additional variable

x=int(input("Enter x:"))
y=int(input("Enter y:"))

print("Before swaping x=",x,"and y=",y)

#swaping the numbers
x,y=y,x

print("After Swaping X=",x,"and y=",y)

#*********************************************************************************************************************************

# 9. Write a program to find sum of first n natural numbers

num=int(input("Enter the upper limit:"))
sum = 0
# useing while loop to iterate until zero
while(num>0):
    sum +=num
    num -=1
print("The sum is =",sum)

#*********************************************************************************************************************************

# 10. Write a program to print truth table for bitwise operators( & , | and ^ operators)

# Truth table for bitwise AND operator
print("Bitwise AND (&) operator:")
print("a\tb\ta & b")
print("-"*22)
for a in (0, 1):
    for b in (0, 1):
        print(f"{a}\t{b}\t{a & b}")
print("\n")

# Truth table for bitwise OR operator
print("Bitwise OR (|) operator:")
print("a\tb\ta | b")
print("-"*22)
for a in (0, 1):
    for b in (0, 1):
        print(f"{a}\t{b}\t{a | b}")
print("\n")

# Truth table for bitwise XOR operator
print("Bitwise XOR (^) operator:")
print("a\tb\ta ^ b")
print("-"*22)
for a in (0, 1):
    for b in (0, 1):
        print(f"{a}\t{b}\t{a ^ b}")


#**********************************************************************************************************************

# 11. Write a program to find left shift and right shift values of a given number.

num=int(input("Enter the number:"))
ls=int(input("Enter the position for left shift:"))
Rs=int(input("Enter the position for Right shift:"))

#left shift
print("After Left shift the value is:",num<<ls)

# Right shift
print("After right shift the value is:",num>>Rs)

#**************************************************************************************************************************

# 12. Using membership operator find whether a given number is in sequence (10,20,56,78,89)

l1=[10,20,56,78,89]

num=float(input("Enter the number you want to find:"))

x=num in l1

if x==True:
    print("Number is present in the sequence ")
else:
    print("Number is not present in the sequence")

#*********************************************************************************************************************************

# P2 13. Using membership operator find whether a given character is in a string

s="This is python programming"
q=input("Enter the character yo want to find:")

x=q in s

if x==True:
    print("This Character is present in the string ")
else:
    print("This Character is not present in the string")
