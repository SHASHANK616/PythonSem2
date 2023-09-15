# Q1. Create a class of student (name, sap id, marks[phy,chem,maths] ). Create 3 objects by taking
# inputs from the user and display details of all students

class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Marks:", self.marks)

# Create object 1
name1 = input("Enter name of student 1: ")
sap_id1 = input("Enter SAP ID of student 1: ")
phy_marks1 = float(input("Enter Physics marks of student 1: "))
chem_marks1 = float(input("Enter Chemistry marks of student 1: "))
maths_marks1 = float(input("Enter Maths marks of student 1: "))

student1 = Student(name1, sap_id1, [phy_marks1, chem_marks1, maths_marks1])

# Create object 2
name2 = input("Enter name of student 2: ")
sap_id2 = input("Enter SAP ID of student 2: ")
phy_marks2 = float(input("Enter Physics marks of student 2: "))
chem_marks2 = float(input("Enter Chemistry marks of student 2: "))
maths_marks2 = float(input("Enter Maths marks of student 2: "))

student2 = Student(name2, sap_id2, [phy_marks2, chem_marks2, maths_marks2])

# Create object 3
name3 = input("Enter name of student 3: ")
sap_id3 = input("Enter SAP ID of student 3: ")
phy_marks3 = float(input("Enter Physics marks of student 3: "))
chem_marks3 = float(input("Enter Chemistry marks of student 3: "))
maths_marks3 = float(input("Enter Maths marks of student 3: "))

student3 = Student(name3, sap_id3, [phy_marks3, chem_marks3, maths_marks3])

# Display details of all students
student1.display_details()
print("-----------")
student2.display_details()
print("-----------")
student3.display_details()

# #***************************************************************************************************************************

# # Q2. Add constructor in the above class to initialize student details of n students and implement
# # following methods:a) Display() student detailsb) Find Marks_percentage() of each studentc) Display result() 
# # [Note: if marks in each subject >40% than Pass else Fail]Write a Function to find average of the class.

class Student:
    def __init__(self, n):
        self.students = []
        for i in range(n):
            name = input(f"Enter name of student {i+1}: ")
            sap_id = input(f"Enter SAP ID of student {i+1}: ")
            phy_marks = float(input(f"Enter Physics marks of student {i+1}: "))
            chem_marks = float(input(f"Enter Chemistry marks of student {i+1}: "))
            maths_marks = float(input(f"Enter Maths marks of student {i+1}: "))

            student = {
                'name': name,
                'sap_id': sap_id,
                'marks': [phy_marks, chem_marks, maths_marks]
            }
            self.students.append(student)

    def display_details(self):
        for student in self.students:
            print("Name:", student['name'])
            print("SAP ID:", student['sap_id'])
            print("Marks:", student['marks'])
            print()

    def find_marks_percentage(self):
        for student in self.students:
            total_marks = sum(student['marks'])
            percentage = (total_marks / 3) * 100
            print(f"{student['name']}: {percentage}%")

    def display_result(self):
        for student in self.students:
            result = all(mark >= 40 for mark in student['marks'])
            print(f"{student['name']}: {'Pass' if result else 'Fail'}")

    def find_class_average(self):
        total_marks = sum(sum(student['marks']) for student in self.students)
        n = len(self.students)
        class_average = total_marks / (3*n)
        print("Class Average:", class_average)

student_class = Student(3)

student_class.display_details()

student_class.find_marks_percentage()

student_class.display_result()

student_class.find_class_average()

# #***************************************************************************************************************************

# # Q3. Create programs to implement different types of inheritances


# #Single inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display_info(self):
        super().display_info()
        print(f"Roll No: {self.roll_no}")

student = Student("John", 18, 123)
student.display_info()


# Multiple Inheritance

class Math:
    def add(self, a, b):
        return a + b

class Physics:
    def sub(self, a, b):
        return a - b

class Calculation(Math, Physics):
    def mul(self, a, b):
        return a * b

calc = Calculation()
print(calc.add(2, 3))
print(calc.sub(5, 2))
print(calc.mul(2, 4))


#Multilevel Inheritance

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, color):
        super().__init__(make, model)
        self.color = color

    def display_info(self):
        super().display_info()
        print(f"Color: {self.color}")

class ElectricCar(Car):
    def __init__(self, make, model, color, battery_size):
        super().__init__(make, model, color)
        self.battery_size = battery_size

    def display_info(self):
        super().display_info()
        print(f"Battery Size: {self.battery_size}")

car = ElectricCar("Tesla", "Model 3", "Red", "75 kWh")
car.display_info()


# Hierarchical Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return


# #**************************************************************************************************************************

# # Q4. Create a class to implement method Overriding

class Animal:
    def make_sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks.")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows.")

animal = Animal()
dog = Dog()
cat = Cat()

animal.make_sound()
dog.make_sound()
cat.make_sound()


# #*********************************************************************************************************************************

# # Q5. Create a class for operator overloading which adds two Point Objects where Point has x & yvalue

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

point1 = Point(2, 3)
point2 = Point(4, 5)
point3 = point1 + point2

print(point1)
print(point2)
print(point3)



