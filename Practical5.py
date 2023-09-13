# 1. Write a program to count and display the number of capital letters in a given string

st=input("Enter the string:")
count=0
for a in st:
    if (a.isupper()):
        count+=1
print("The number of capital letters in the strings are:",count)

#****************************************************************************************************

# P5 2. Count total number of vowels in a given string.

st=input("Enter the String:")
vowel=set("aeiouAEIOU")
count=0
for a in st:
    if a in vowel:
        count+=1
print("The vowel count is string is:",count)

#****************************************************************************************************

# P5 3. Input a sentence and print words in separate lines

st=input("Enter the string:")
words=st.split(" ")
for a in words:
    print(a)


#****************************************************************************************************

# P5 4.. WAP to enter a string and a substring. You have to print the number of times that thesubstring occurs in the given string. String traversal will take place from left to right, notfrom right to left.Sample InputABCDCDCCDCSample Output2

st = input("Enter the string:")
pattern = input("Enter the sub string:")
print(st.count(pattern))

#****************************************************************************************************

# P5 5. Given a string containing both upper and lower case alphabets. Write a Python programto count the number of occurrences of each alphabet (case insensitive) and display thesame

st=input("Enter the string:")
st2=st.lower() # conver the string into lowe case

# for loop to itrate through each letter in string
for i in st2:
  print(i,st2.count(i)) # using Count function to count occurance of each letter
 
 

#****************************************************************************************************

# P5 6. Program to count number of unique words in a given sentence using sets.

sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Count the number of unique words using a set
unique_words = set(words)
count = len(unique_words)

# Display the result
print("Number of unique words:",count)


#****************************************************************************************************

# 7. Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
# a) Fruits which are in both sets s1 and s2
# b) Fruits only in s1 but not in s2
# c) Count of all fruits from s1 and s2

n = int(input("Enter the number of fruits in each set: "))

s1 = set()
print("Enter the fruits in set s1:")
for i in range(n):
    fruit = input()
    s1.add(fruit)

s2 = set()
print("Enter the fruits in set s2:")
for i in range(n):
    fruit = input()
    s2.add(fruit)

common_fruits = s1.intersection(s2)

s1_only_fruits = s1.difference(s2)

total_count = len(s1) + len(s2)

print("Fruits which are in both sets s1 and s2 are:", common_fruits)
print("Fruits only in s1 but not in s2:", s1_only_fruits)
print("Count of all fruits from s1 and s2:", total_count)

#*****************************************************************************************************************************************************

# 8. Take two sets and apply various set operations on them :
# S1 = {Red ,yellow, orange , blue }
# S2 = {violet, blue , purple}

S1 = {"Red" ,"yellow","orange" , "blue" }
S2 = {"violet","blue" , "purple"}

S1.add("apple") #Adds an element to the set
print(S1)

s3=S1.copy() #Returns a copy of the set
print(s3)

z=S1.difference(S2) #Returns a set containing the difference between two or more sets
print(z)

x=S1.difference_update(S2) #Removes the items in this set that are also included in another, specified set
print(x)

S2.discard("voilet") #Remove the specified item
print(S2)

b=S1.intersection(S2) #Returns a set, that is the intersection of two other sets

S1.intersection_update(S2) #Removes the items in this set that are not present in other, specified set(s)

s4=S2.isdisjoint(S1) #Returns whether two sets have a intersection or not

s5=S1.issubset(S2) #Returns whether another set contains this set or not

s6=S1.issuperset(S2) #Returns whether this set contains another set or not

S2.pop() #Removes a random element from the set

S1.remove("Red") #Removes the specified element

s7=S2.symmetric_difference(S1) #Returns a set with the symmetric differences of two sets

S1.symmetric_difference_update(S2) #inserts the symmetric differences from this set and another

s8=S2.union(S1) #Return a set containing the union of sets

S2.update(S1) #Update the set with the union of this set and others

S1.clear() #Removes all the elements from the set
S2.clear()
