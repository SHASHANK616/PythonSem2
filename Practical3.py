#P3 1. Check whether given number is divisible by 3 and 5 both

num=int(input("Enter the number:"))


# If condition to check divisibility

if num%3==0 and num%5==0:
    print("The given number is divisble by 3 and 5")
else:
    print("The given number is not divisble by 3 and 5")
    
#***********************************************************************************

#P3  2. Check whether a given number is multiple of five or not.
num=int(input("Enter the number:"))


if num%5==0:
    print("The number is multiple of 5")
else:
    print("The number is not a multiple of 5 ")
    
#*******************************************************************************

# P3 3. Find the greatest among two numbers. If numbers are equal than print “numbers are equal”
a=input("Enter the number:")
b=input("Enter the number:")


#Applying conditions
if a==b:
    print("Numbers are equal")
elif a>b:
    print(a," is greatest")
else:
    print(b," is greatest")


#*******************************************************************************************

#P3 4. Find the greatest among three numbers assuming no two values are same.

print("Note:- No two values should be same ")
print("-"*35)
#input from user
a=float(input("Enter the first number:"))
b=float(input("Enter the 2nd number:"))
c=float(input("Enter the 3rd number:"))

# applying conditions
if a>b and a>c:
    print(a,"is the greatest")
elif b>a and b>c:
    print(b, "is the greatest")
else:
    print(c,"is the greatest")
    
#****************************************************************************************

#P3 5. Check whether the quadratic equation has real roots or imaginary roots. Display the roots

import math

# Get the coefficients of the quadratic equation from the user
a = float(input("Enter coefficient of x^2: "))
b = float(input("Enter coefficient of x: "))
c = float(input("Enter constant term: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check whether the roots are real or imaginary
if discriminant > 0:
    # Two distinct real roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("The roots are real and distinct.")
    print("Root 1 = {:.2f}".format(root1))
    print("Root 2 = {:.2f}".format(root2))
elif discriminant == 0:
    # One real root (repeated)
    root = -b / (2*a)
    print("The root is real and repeated.")
    print("Root = {:.2f}".format(root))
else:
    # Two complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print("The roots are complex and conjugate.")
    print("Root 1 = {:.2f} + {:.2f}j".format(real_part, imaginary_part))
    print("Root 2 = {:.2f} - {:.2f}j".format(real_part, imaginary_part))
    
#********************************************************************************************************************

# P3 6.Find whether a given year is a leap year or not.

year=int(input("Enter the year:"))


if(year%4==0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
    

#****************************************************************************************************************

# P4 Q7) Count and print all numbers divisible by 5 or 7 between 1 to 100

count=0
print("All numbers divisible by 5 or 7 between 1 to 100 are:")
for i in range(0,100):
    if((i%5==0) and (i%7==0)):
        count+=1
        print(i)
print("total numbers:",count)

#**********************************************************************************************************************

#P3 8. Print the grade sheet of a student for the given range of cgpa. Scan marks of five subjectsand calculate the percentage.
name=input("Enter your name:")
r=input("Enter your Roll No:")
sem=input("Enter your Semester:")
sap=input("Enter your SAPID:")
Course=input("Enter your Course:")

s1=float(input("Enter marks of PDS out of 100:"))
s2=float(input("Enter marks of Pyhon out of 100:"))
s3=float(input("Enter marks of Chemistry out of 100:"))
s4=float(input("Enter marks of English out of 100:"))
s5=float(input("Enter marks of Physics out of 100:"))

percentage=((s1+s2+s3+s4+s5)/5)

cgpa=percentage/10

if (cgpa>0 and cgpa<=3.4):
    CGPA="F"
elif(cgpa>=3.5 and cgpa<=5):
    CGPA="C+"
elif(cgpa>=5.1 and cgpa<=6):
    CGPA="B"
elif(cgpa>=6.1 and cgpa<=7):
    CGPA="B+"
elif(cgpa>=7.1 and cgpa<=8):
    CGPA="A"
elif(cgpa>=8.1 and cgpa<=9):
    CGPA="A+"
elif(cgpa>=9.1 and cgpa<=10):
    CGPA="O"
    
print("-----------------------------------")
print("Name:",name)
print("Roll Number:",r)
print("Sem:",sem)
print("\t\t\t\tSAPID:",sap)
print("\t\t\t\tCourse:",Course)

print("Subject Name: Marks")
print("PDS:",s1)
print("python:",s2)
print("Chemistry:",s3)
print("English:",s4)
print("Physics:",s5)
print("Percentage:",percentage)
print("CGPA:",cgpa,"%")
print("Grade:",CGPA)