#P4 Q1) Find a factorial of given number
num=int(input("Enter The number:"))
fact=1
if(num<0):
    print("Invalid input (factorial does not exist for negative numbers)")
elif(num==0):
    print("Factorial=0")
else:
 for i in range(1,num+1):
    fact=fact*i
 print("Factorial=",fact)
 
 #*********************************************************************************************
 
 #P4 Q2) Find whether the given number is Armstrong number

number = int(input("Enter the number:"))
temp = number
sum = 0
while temp != 0:
    k = temp % 10
    sum += k*k*k
    temp = temp//10
if sum == number:
    print('Given number is   Armstrong Number')
else:
    print('Given number is not Armstrong Number')

#***************************************************************************************************
# P4 Q3) Print Fibonacci series up to given term.
num = int(input("Enter the number:"))
n1=0
n2 =1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()

#***************************************************************************************************

# P4 4) Write a program to find if given number is prime number or not.

num = int(input("Enter the number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
    
    

#***************************************************************************************************

# P4 Q5) Check whether given number is palindrome or not

num=input("Enter the number:")

if (num==num[::-1]):
    print("The number is palindrome")
else:
    print("The number is not palindrome")
    

#***************************************************************************************************

#P4 Q6) Write a program to print sum of digits

num = input("Enter Number: ")
sum = 0
for i in num:
    sum = sum + int(i)
print("Sum of the number is:",sum)



#***************************************************************************************************

# P4 Q7) Count and print all numbers divisible by 5 or 7 between 1 to 100

count=0
print("All numbers divisible by 5 or 7 between 1 to 100 are:")
for i in range(0,100):
    if((i%5==0) and (i%7==0)):
        count+=1
        print(i)
print("total numbers:",count)

#***************************************************************************************************


#P4 Q8. Convert all lower cases to upper case in a string
st=input("Enter the string:")
print("The Uppercase of the given string is: ",st.upper())

#***************************************************************************************************

# P4 Q9) Print all prime numbers between 1 and 100
r=100  
print("Prime numbers between 1 to 100 are:")
for a in range(2,101):  
    k=0  
    for i in range(2,a//2+1):  
        if(a%i==0):  
            k=k+1  
    if(k<=0):  
        print(a, end = " ")
    


#***************************************************************************************************

# P4 Q10) Print the table for a given number:5 * 1 = 55 * 2 = 10.

num=int(input("Enter the number:"))
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)


#***************************************************************************************************
