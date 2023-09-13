# Q2. Write Python programs to print strings in the given manner:
#     a) Hello Everyone !!!
#     b) Hello
#        World
#     c) Hello
#            World
#     d) ‘ Rohit’ s date of birth is 12\05\1999’

print("Hello Everyone !!!")
print("Hello\nWorld")
print("Hello\n\tWorld")
print("‘ Rohit’ s date of birth is 12\ 05\ 1999’")

#********************************************************************************************************

# Q3) Declare a string variable called x and assign it the value “Hello”.Print out the value of x

x="“Hello”"
print(x)

#********************************************************************************************************

# Q4) Take different data types and print values using print function

a="Hi"
b=5.0
c=20
print(a)
print(b)
print(c)

#**********************************************************************************************************

# Q5) Take two variable a and b. Assign your first name and last name. Print your Name after adding your First name and Last name together.

a="Shashank"
b="Suman"

#concatinating two strings 
c=a+" "+b

#printing the result
print(c)

#*************************************************************************************************************

# Q6) Declare three variables, consisting of your first name, your last name and Nickname. 
#     Write a program that prints out your first name, then your nickname in parenthesis and then your lastname.

a="Shashank"
b="Atul"
C="Suman"
print(a+" "+"("+b+")"+" "+C)

#*************************************************************************************************************

# Q7) Declare and assign values to suitable variables and print in the following way :
# NAME : NIKUNJ BANSAL
# SAP ID : 500069944
# DATE OF BIRTH : 13 Oct 1999
# ADDRESS : UPES
#          Bidholi Campus
#          Pincode : 248007
# Programme : AI & ML
# Semester : 2

name=input("Enter your name:")
Sapid=input("Enter your Sap:")
dob=input("Enter your DOB:")
address=input("Enter your address:")
programme=input("Enter your program:")
sem=input("Enter your semester:")


print("NAME :",name)
print("SAP ID : ",Sapid)
print("DATE OF BIRTH :",dob)
print("ADDRESS :",address)
print("Programme :",programme)
print("Semester :",sem)
