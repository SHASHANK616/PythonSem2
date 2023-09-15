
#P8 Q1.	Add few names, one name in each row, in “name.txt file”.
# a.	Count no of names
# b.	Count all names starting with vowel
# c.	Find longest name

with open("file1.txt", "r") as f:
    names = f.readlines()
    names = [name.strip() for name in names]

num_names = len(names)
print("Number of names:", num_names)

vowel_count = 0
for name in names:
    if name[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1
print("Number of names starting with a vowel:", vowel_count)
longest_name = max(names, key=len)
print("Longest name:", longest_name)




#*******************************************************************************************************************

# Q2.	Store integers in a file.
# a.	Find the max number
# b.	Find average of all numbers
# c.	Count number of numbers greater than 100


with open("numbers.txt", "r") as f:
    numbers = [int(line.strip()) for line in f]

max_number = max(numbers)
print("Maximum number:", max_number)

avg_number = sum(numbers) / len(numbers)
print("Average of all numbers:", avg_number)

count_gt_100 = sum(1 for num in numbers if num > 100)
print("Number of numbers greater than 100:", count_gt_100)





#*******************************************************************************************************************

# Q3.	Assume a file city.txt with details of 5 cities in given format (cityname population(in lakhs) area(in sq KM) ):
# Example:
# Dehradun 5.78 308.20
# Delhi 190 1484
# ……………
# Open file city.txt and read to:
# a.	Display details of all cities
# b.	Display city names with population more than 10Lakhs
# c.	Display sum of areas of all cities

with open("city.txt", "r") as f:
    cities = [line.strip().split() for line in f]

#a)
print("Details of all cities:")
for city in cities:
    print("City:", city[0])
    print("Population (in lakhs):", city[1])
    print("Area:", city[2])

#b)
print("Cities with population more than 10 Lakhs:")
for city in cities:
    if float(city[1]) > 10:
        print(city[0])

#c)
area_sum = sum(float(city[2]) for city in cities)
print("Sum of areas of all cities:",area_sum)

#*******************************************************************************************************************

# Q4.	 Input two values from user where the first line contains N, the number of test cases. The next N lines contain the space separated values of a and b. Perform integer division and print a/b. Handle exception in case of ZeroDivisionError or ValueError. 
# Sample input
# 1 0
# 2 $
# 3 1 
# Sample Output :
# Error Code: integer division or modulo by zero 
# Error Code: invalid literal for int() with base 10: '$' 3

try:
    n = int(input("Enter the number of test cases:"))
    for i in range(n):
        a, b = input("Enter two values :").split()
        print(a//b)
except ValueError as e:
    print("Error code:", e)
except ZeroDivisionError as v:
    print("Error Code:", v)


#*******************************************************************************************************************

# 
#P8 Q5.	Create multiple suitable exceptions for a file handling program. 

try:
    # FileNotFound error
    with open("filename.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")

try:
    # PermissionError
    with open("file.txt", "r") as file:
        content = file.read()
except PermissionError:
    print("Permission denied")

try:
    # ValueError
    with open(1234, "r") as file:
        content = file.read()
except ValueError:
    print("Value Error")

try:
    # IOError
    with open("file.txt", "r") as file:
        content = file.read()
    with open("file.txt", "w") as file:
        file.write("Hello, World!")
except IOError:
    print("An input/output error occurred.")

